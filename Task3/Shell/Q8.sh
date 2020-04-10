read p
read q 
read r
if test $p -eq $r && test $p -eq $r
then
    echo "EQUILATERAL"
elif test $p -eq $r || test $p -eq $q || test $q -eq $r
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
