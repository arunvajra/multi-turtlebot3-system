# 10 Turtlebot3 System with Obstacle Avoidance

Spawning 10 turtlebot 3 robots in Gazebo simulator, the turtlebots move around freely and avoids collisions through the use of planar laser range-finder. Each turtlebot3 robot has a separate python script that initiates movement and obstacle avoidance. All the scripts are run concurrently using a single 'multi_launch.py' file through the subprocess module.

## Resources
- Ubuntu 20.04
- ROS Noetic Ninjemys
- Gazebo Simulator
- Turtlebot3 'Burger'
- Python 3

## Installation Guide

```
cd ~/catkin_ws/src
git clone https://github.com/arunvajra/multi-turtlebot3-system.git 
cd ~/catkin_ws
catkin_make
```

## Run

- Launch simulator with 10 turtlebot3 robots
```
roslaunch turtlebot3_gazebo ten_obstacle_turtlebot3.launch
```
- Initiate movement and obstacle avoidance <br /> 
In new terminal:
```
cd ~/catkin_ws/src/pyscripts
python3 multi_launch.py
```

## Demo
![dd](https://github.com/arunvajra/multi-turtlebot3-system/blob/main/demo/demo.gif)
