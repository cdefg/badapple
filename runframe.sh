framenum=2192
framerate=0.1
for i in $(seq 1 $framenum)
do
	cat ./${i}.txt
	sleep $framerate
	clear
done

