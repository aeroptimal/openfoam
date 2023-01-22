#!/bin/bash
while true
do
    [ "$(ls -A /home/foam/OpenFOAM/-7/run)" ] && rm -R /home/foam/OpenFOAM/-7/run/*
    python3 create.py
    if [ -f "/home/foam/OpenFOAM/-7/run/request.dat" ]
        then
        cd /home/foam/OpenFOAM/-7/run
        blockMesh
        foamMeshToFluent
        foamToVTK
        checkMesh > meshData.dat
        cd /
        python3 generate.py
    fi
done