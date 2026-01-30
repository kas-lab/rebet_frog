#!/bin/bash

trap ctrl_c INT

function ctrl_c() {
        echo "Cleaning up.."
	./killall.sh
        echo "Shutting down"
        exit 0
}


for EXPNUM in {1..1}
do
	xterm -hold -e ./YOLO.sh &
	xterm -hold -e ./GZ.sh true 1 &
	sleep 15
	xterm -hold -e ./NOISE.sh &
	sleep 5
	xterm -hold -e ./NAV.sh &
	sleep 15
	xterm -hold -e ./ARB.sh &
	sleep 25
    	xterm -hold -e ./ADX.sh &
	sleep 200
	xterm -hold -e ./AAL.sh &
	sleep 3
	xterm -hold -e ./REFL.sh &
	sleep 5
	xterm -hold -e ./START.sh &

	SECONDS=0 
	while [ ! -f ~/rebet_ws/scripts/mission.done -a $SECONDS -lt 400 ]
	do
	   echo "waiting for mission to be done" $EXPNUM       
	sleep 10 #sustainability!
	done
	echo "mission done"
	rm ~/rebet_ws/scripts/mission.done
	./killall.sh	
done
