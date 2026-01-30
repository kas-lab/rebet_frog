#!/bin/bash
source ~/.bashrc
source install/setup.bash
source /venv/bin/activate
export PYTHONPATH=$PYTHONPATH:/venv/lib/python3.10/site-packages/
ros2 launch rebet_frog adaptation_engine_launch.py
