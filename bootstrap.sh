#!/usr/bin/env bash

git init .
git remote add origin git@github.com:RakNoel/LatexSetup.git
git pull origin master

rm -rf .git/
rm -rf .gitignore
rm -rf README.md

rm -rf bootstrap.sh
