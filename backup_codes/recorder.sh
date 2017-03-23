#!/bin/bash
timeout 2s rosrun kinect2_viewer kinect2_viewer qhd image
mv ~/catkin_ws/*.pcd ~/recordings/trials/pcd
mv ~/catkin_ws/*.png ~/recordings/trials/depth_color
mv ~/catkin_ws/*.jpg ~/recordings/trials/color+depth
