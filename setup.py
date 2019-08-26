cCode = input("Enter course code (e.g. INF234): ")
cName = input("Enter cource name (e.g. Advanced alg.): ")
dName = input("Enter Document title (e.g. Obligatory ass. 1): ")

innFile = open("uib_frontpage.tex", "r+")

old = innFile.read()
fix = old.replace("--#1--", cCode).replace("--#2--", cName).replace("--#3--", dName)

innFile.write(fix)
innFile.close()
