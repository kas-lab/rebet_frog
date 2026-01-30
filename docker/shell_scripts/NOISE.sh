#!/bin/bash
source ~/.bashrc
source install/setup.bash
source /venv/bin/activate
ros2 run rebet_frog noisy_camera.py
