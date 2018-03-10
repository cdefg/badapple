framenum=2192
for i in $(seq 1 $framenum)
do
	cat ./${i}.txt
	sleep 0.05
	clear
done

