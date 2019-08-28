#!/usr/bin/env python3

import os

# Read Innput
cCode = input("Enter course code (e.g. INF234): ")
cName = input("Enter cource name (e.g. Advanced alg.): ")
dName = input("Enter Document title (e.g. Obligatory ass. 1): ")

# Static var
fileName = "uib_frontpage.tex"
docName = "default.tex"

# Change text
innFile = open(fileName, "r+")
old = innFile.read()
fix = old.replace("--#1--", cCode).replace("--#2--", cName).replace("--#3--", dName)
innFile.close()

# Save file
outFile = open(fileName, "w+")
outFile.write(fix)
outFile.close()

os.rename(docName, cCode + "_report.tex")
os.remove("setup.py")
