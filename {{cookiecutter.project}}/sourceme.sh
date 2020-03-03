#!/usr/bin/env bash 

# Source Toolbox sourceme.sh
cd toolbox; source sourceme.sh; cd ..

# Set PYTHONPATH accordingly
if [ -z "$PYTHONPATH" ]
then
    export PYTHONPATH=$PWD
else
    export PYTHONPATH=$PWD:$PYTHONPATH
fi

# Set MYPYPATH accordingly
if [ -z "$MYPYPATH" ]
then
    export MYPYPATH=$PWD/{{cookiecutter.project}}
else
    export MYPYPATH=$PWD/{{cookiecutter.project}}:$MYPYPATH
fi
