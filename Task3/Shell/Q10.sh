read N 
declare -i sum=0
for ((i=0;i<N;i++))
do 
    read n 
    sum=$((sum + n))
done 
printf '%.3f\n' $(echo "scale=3; $sum/$N" | bc)
