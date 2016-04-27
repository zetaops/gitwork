# Zetaops Development Workflow

## Issues

- First create an issue in Redmine, containing a descriptive title and detailed explanations. Please do not leave empty  **assignee**, **time estimation**, and **target version**. And also please provide **watchers**, **start** and **due date** and other necessary fields whenever needed. 

- You should give a proper name to your issues. We don't accept [whatthecommit](http://whatthecommit.com/) based bullsh*t issue names. The issue name should explain, the status of the issue, main purpose of the issue and should be descriptive.

- The issue should be small enough. You can create more then one issue for the same task. 

- If you want github integration to create a pair issue,  mark your issue with github repo tags such as #ulakbus, #zengine, #pyoko etc.. at the and of description field.

- Please open issues as new and report progress by commenting it and increasing progress status, also remember writing development log times (mark your ***spent time***).

- Commit messages should refer issue or issue pairs in Redmine and Github. Also it is possible to mark issue progress in commit messages, detailed informations are below.

- If your issue blocks others or it has special 'Priority', do not forget set 'Priority'.

- When you finish your work, mark your issue as ***'Resolved'***, never close it.

- In case you'll need another dev to check your work or your work is still incomplete because of any reason, mark your issue as resolved and change ***Assignee*** name to your supervisor name.

- When you are creating an issue, if the issue estimation is greater then ***5 hour***, you should notify your supervisor to discuss why you'll need this time. 

- Any issues greater then ***10 hours*** will be threated as architectural interference and should have detailed documentation to be attached to relevant project. You should have at least one meeting with team!

## Git Flow

### Git Flow Installation

Install these two packages on top of your git and git completions packages:

* https://github.com/petervanderdoes/gitflow-avh
* https://github.com/petervanderdoes/git-flow-completion

Please see the installation instructions for each package in its own documentation


### Commit Labels for Pretty Changelogs
(see: http://keepachangelog.com/)

Use labels below to mark commits as what they are for:

- **ADD** - Added for new features.
- **CHANGE** - Changed for changes in existing functionality.
- **DEPRECATE** - Deprecated for once-stable features removed in upcoming releases.
- **REMOVE** - Removed for deprecated features removed in this release.
- **FIX** - Fixed for any bug fixes.
- **SECURITY** - Security to invite users to upgrade in case of vulnerabilities.
- **REFACTOR** - Refactor code do not change any feature

- **UNIVERSE** - The rest whatever you do! When you use this label, this site[1] automatically will trigger and one dove silently going to die somewhere in UNIVERSE!

[1] http://www.nooooooooooooooo.com/

### Redmine Referers
Use patterns below in commit messages to close, fix, refer or report progress for issues:

- **rclose #123**: mark issue number 123 resolved and set issue progress %100

- **rfix #123**: mark issue number 123 resolved and set issue progress %100 (same with close, fix is especially for bugs)

- **rref #123**: refers issue number 123,

- **p70 #123**: mark issue number 123 resolved and set issue progress %100. It must be one of between p10 and p90 incrementing by 10.


### Github Referers
Github will understand you when you type in your comments:

- **closes GH-123**: close issue 123 of Github origin repo.
- **closes zetaops/ulakbusGH-123**: close issue 123 of Github zetaops/ulakbus repo. This is the way to close issues between cross repos.
- **fixes GH-123**: same with closes, choose this one if you work on a bug.
- **refs GH-123**: refers issue 123 of Github origin repo.

Cross repo operations in commit messages must be explicit as in "closes zetaops/ulakbusGH-123" and fixes, refs are valid.

**Warning 1:**
GitHub rewrites commit messages to show us prettier without changing original ones. It transforms:

  * GH-123 into #123
  * zetaops/ulakbusGH-123 into zetaops/ulakbus#123

**Warning 1:**
Github sets main branch as master unless you pick another one in repo settings. We use GitFlow branching model, so develop branch should be set as main branch. Otherwise your issue refs wont work.

### Commit Message Samples
The commit message below means:

  - commit will take place in ADD section of CHANGELOG

```bash
  git commit -m 'ADD, Get and sync methods were added for new staff workflow'
```

The commit message below means:

  - commit will take place in ADD section of CHANGELOG
  - closes issue number 78 of Github origin repo

```bash
  git commit -m 'ADD, closes GH-78. Get and sync methods were added for new staff workflow'
```

The commit message below means:

  - commit will take place in ADD section of CHANGELOG
  - closes issue number 78 of Github origin repo
  - and changes progress status of issue number #481 to 60% and switches state to "in progress" in redmine

```bash
  git commit -m 'ADD closes GH-78, p60 #481. Get and sync methods were added for new staff workflow'
```


The commit message below means:

  - commit will take place in BUG FIXES section of CHANGELOG
  - closes issue number 78 of Github origin repo and issue number 13 of zetaops/ulakbus repo
  - changes progress status of issue number #481 to 60% and switches state to "in progress" in redmine
  - changes progress status of issue number #490 to 40% and switches state to "in progress" in redmine
  - refers issue number 492 and 493 in redmine

```bash
  git commit -m 'ADD closes GH-78, zetaops/ulakbusGH-13, p60 #481, p40 #490, rref #492, #493. Get and sync methods were added for new staff workflow'
```


The commit message below means:

  - commit will take place in BUG FIXES section of CHANGELOG
  - closes issue number 78 of Github origin repo and issue number 13 of zetaops/ulakbus repo
  - changes progress status of issue number #481 to 60% and switches state to "in progress" in redmine
  - changes progress status of issue number #490 to 40% and switches state to "in progress" in redmine
  - refers issue number 492 and 493 in redmine
  - closes issue number 485 and 486 in redmine

```bash
  git commit -m 'ADD closes GH-78, zetaops/ulakbusGH-13, rclose #485, #486, p60 #481, p40 #490, rref #492, #493. Get and sync methods were added for new staff workflow'
```

### Working with Git Flow

#### Implementing a new feature
Just create a new feature branch:

```bash
# delete_user_workflow is our new feature name
git flow feature start delete_user_workflow
```

Start development, regular git add / commit cycle:

```bash
# write some good codes
git add some_files
git commit -m 'ADD rref #48. Initial'
```
Don't forget to mention related issues and do not forget to use commit message convention above.

Publish your work to keep a remote copy and to collaborate with others or yourself in elsewhere you need your code.

```bash
git flow feature publish delete_user_workflow
```

The next day first of all rebase your work with develop branch to keep your work more compatible. You need to take 3 steps. First step is update your local develop branch with origin.

```bash
git checkout develop && git pull --rebase origin develop
```

Second step is rebase your work with updated local develop:

```bash
git flow feature rebase delete_user_workflow develop
```

And finally the third step is rebase your work with your origin branch in case of any changes pushed by your colleagues:

```bash
git pull --rebase origin delete_user_workflow
```

Fix conflicts if you encounter any by iteration of ``git add conflict_files`` && ```git rebase --continue```

And then turn your development cycle back (step 2)

Finally, finish your work:
```bash
git flow feature finish delete_user_workflow
```
