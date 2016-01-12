# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

import datetime
from redmine import Redmine
from github3 import login
import os

__author__ = 'Ali Riza Keles'

# get enviroment variables
github_username = os.environ.get('GITHUB_USERNAME', None)
github_password = os.environ.get('GITHUB_PASSWORD', None)
redmine_key = os.environ.get('REDMINE_KEY', None)
redmine_url = os.environ.get('REDMINE_URL', None)
redmine_project = os.environ.get('REDMINE_PROJECT', None)
repo_tags = os.environ.get('REPO_TAGS', None)

# if any of envs hasn't been set, raise exepction
envs = [github_username, github_password, redmine_key, redmine_url, redmine_project]
if not all(envs):
    raise Exception('Please be sure all enviroment variables were set %s' % ','.join(envs))

# redmine and github clients
redmine = Redmine(redmine_url, key=redmine_key)
gh = login(username=github_username, password=github_password)


def create_issue_github(redmine_issue, github_repo):
    """
    create new redmine issue on github repo

    :param redmine_issue:
    :param github_repo:
    :return:
    """
    print(redmine_issue.subject, github_repo)
    owner, repository = github_repo.split('/')
    title = '%s #%s' % (redmine_issue.subject, redmine_issue.id)
    new_github_issue = gh.create_issue(owner=owner, repository=repository, title=title,
                                       body=redmine_issue.description)
    if new_github_issue:
        redmine_issue.description += '\n#GH-%s : %s\n\n' % (new_github_issue.number, new_github_issue.html_url)
        redmine_issue.save()


# redmine project
project = redmine.project.get(redmine_project)

# repo tags explains which redmine keyword points to which github repo
repo_tag_list = repo_tags.split(',')
repo_map = {}
for tag in repo_tag_list:
    tag_list = tag.split(':')
    repo_map.update({tag_list[0]: tag_list[1]})

# grab latest 20 issue from redmine

# limit last week
now = datetime.datetime.now()
week_ago = now - datetime.timedelta(weeks=1)
last_week_filter_string = "><{:%Y-%m-%d}|{:%Y-%m-%d}".format(week_ago, now)

issues = redmine.issue.filter(
        project_id=project.id,
        sort='created_on:desc',
        created_on=last_week_filter_string,
        limit=20
)

for issue in issues:
    for tag, repo in repo_map.items():
        if issue.description.find('#%s' % tag) > 0 and issue.description.find('#github') == -1:
            create_issue_github(issue, repo)
    if issue.description.find('#github') == -1:
        issue.description += ' \n\n#github\n'
        issue.save()
