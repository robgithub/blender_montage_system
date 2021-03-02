#! /bin/bash
#
# render animation from montage frames
# requests sequential itteration numbers
#
# took 2:34
#
# example
#   ./render_animation.sh "../attempt 003/" "skull A3 "

# path to the blender files 
BPATH=$1

#the prefix of the name excluding the itteration number
PREFIX=$2

# number of itterations found
TOTAL=$(ls -l "$BPATH" | egrep "[0-9]{4}\.blend$" | wc -l)

for (( n=1; n<=$TOTAL; n++ ))
do
    ITTERATION=$(printf "%04d" $n)
    ./render_4x8_montage.sh "$BPATH$PREFIX" $ITTERATION
done

ffmpeg -framerate 1 -i tmp/skulls/montage_%04d.png -codec copy output.mkv 
