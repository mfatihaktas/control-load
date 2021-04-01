#!/bin/bash
echo $1 $2 $3

PY=python3

if [ $1 = 'i' ]; then
  $PY model.py
elif [ $1 = 'ts' ]; then
  $PY test_sim.py
else
  echo "Arg did not match!"
fi
