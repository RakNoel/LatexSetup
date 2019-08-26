#rm -rf .git

read -p "Enter course code (e.g. INF234): "  ccode
read -p "Enter course name (e.g. Advanced Algorithms)" cname
read -p "Enter document Title" dname

SED1="s/--#1--/" + $ccode + "/g"
SED2="s/--#2--/" + $cname + "/g"
DES3="s/--#3--/" + $dname + "/g"

DOCUMENT="uib_frontpage.tex"

sed -i $SED1 $DOCUMENT
sed -i $SED2 $DOCUMENT
sed -i $SED3 $DOCUMENT
