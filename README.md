# sea rabbit
Readme goes here.  
note to self: finish ASAP!  

# dependencies
- [bno055](https://github.com/flynneva/bno055)
- [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) (Install this with `sudo apt install ros-humble-slam-toolbox`)
- [velodyne driver](https://github.com/ros-drivers/velodyne)

# nodes
`ros2 run sea_rabbit {node name here}`  
- odom_to_baselink
    - publishes an odom to baselink transformation using IMU odometry

# launch files
`ros2 launch sea_rabbit {Launchfile name here}.launch.py`  
- all_nodes.launch.py
    - launches bno055 driver, odom_to_baselink, rviz, slam toolbox, and velodyne driver.
    - this is just a really conveniant way to run all the nodes you need for developing
