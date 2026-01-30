#!/bin/bash
source ~/.bashrc
source install/setup.bash
source /usr/share/gazebo/setup.bash

GUI_VALUE=${1:-true}       
MYSEED_VALUE=${2:-1}

ros2 launch rebet_frog spawn_tb3.launch.py gui:=$GUI_VALUE myseed:=$MYSEED_VALUE