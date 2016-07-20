#!/bin/bash 
VERSION=$1
git flow release start $VERSION
echo "v$VERSION" > VERSION
git add VERSION
sed -ie "s/version=.*/version='$VERSION',/" setup.py
git add setup.py
git commit -m "bump version $VERSION"
python setup.py register -r pypi     # register new version first
python setup.py sdist upload -r pypi # upload dist as tar archive
git flow release finish $VERSION
git push
git push --tags
git checkout master
git push

