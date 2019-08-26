git init .
git remote add origin git@github.com:RakNoel/LatexSetup.git
git pull

rm -rf .git/
rm -rf .gitignore
rm -rf README.md

python setup.py

rm -rf setup.py
