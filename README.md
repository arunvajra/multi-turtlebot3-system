# 10 Turtlebot3 System with Obstacle Avoidance

Spawning 10 turtlebot 3 robots in Gazebo simulator, the turtlebots move around freely and avoids collisions through the use of planar laser range-finder.

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

```
roslaunch turtlebot3_gazebo ten_obstacle_turtlebot3.launch
```

## Demo
![dd](https://github.com/arunvajra/multi-turtlebot3-system/blob/main/demo/demo.gif)
