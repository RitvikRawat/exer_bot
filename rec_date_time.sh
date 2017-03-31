#!/bin/bash

# mkdir -p ~/recordings/`date '+%y%m%d'`/{1,2,3} 

current_date_time="`date '+%y-%m-%d-%H:%M:%S'`"

mkdir -p ~/recordings/$current_date_time/{pcd,depth_color,camera}

timeout 5s rosrun kinect2_viewer kinect2_viewer qhd both
mv ~/catkin_ws/*.pcd ~/recordings/$current_date_time/pcd
mv ~/catkin_ws/*.png ~/recordings/$current_date_time/depth_color
mv ~/catkin_ws/*.jpg ~/recordings/$current_date_time/camera

#delete the pcd and rgb images as we are not using them

rm -r ~/recordings/$current_date_time/pcd/*.pcd
rm -r ~/recordings/$current_date_time/camera/*.jpg