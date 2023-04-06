#!/bin/bash
#
# simple bash script to move up a directory
# because im too lazy
#

LEVEL=$1
for ((i = 0; i < LEVEL; i++)); do
	echo $i
	CDIR=../$CDIR
done
cd $CDIR
echo "you are in: "$PWD
sh=$(which $SHELL)
exec $sh