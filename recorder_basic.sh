#!/bin/bash
timeout 5s rosrun kinect2_viewer kinect2_viewer qhd both
mv ~/catkin_ws/*.pcd ~/recordings/trials/pcd
mv ~/catkin_ws/*.png ~/recordings/trials/depth_color
mv ~/catkin_ws/*.jpg ~/recordings/trials/camera

#delete the pcd and rgb images as we are not using them
rm -r ~/recordings/trials/pcd/*.pcd
rm -r ~/recordings/trials/camera/*.jpg