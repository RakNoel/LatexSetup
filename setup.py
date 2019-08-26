#!/usr/bin/env python3

import os

# Setup location
os.remove('.gitignore')
os.remove('.git/')
os.remove('README.md')

# Read Innput
cCode = input("Enter course code (e.g. INF234): ")
cName = input("Enter cource name (e.g. Advanced alg.): ")
dName = input("Enter Document title (e.g. Obligatory ass. 1): ")

# Static var
fileName = "uib_frontpage.tex"

# Change text
innFile = open(fileName, "r+")
old = innFile.read()
fix = old.replace("--#1--", cCode).replace("--#2--", cName).replace("--#3--", dName)
innFile.close()

# Save file
outFile = open(fileName, "w+")
outFile.write(fix)
outFile.close()

# Finaly remove self
os.remove('setup.py')
