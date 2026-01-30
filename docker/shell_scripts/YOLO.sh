#!/bin/bash
source ~/.bashrc
source install/setup.bash
source /venv/bin/activate
ros2 launch rebet_frog yolo_self_start_launch.py 
