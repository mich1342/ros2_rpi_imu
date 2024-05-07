# ros2_rpi_imu

A simple package made to interface IMU with Raspberry PI. Tested using GY-85 IMU and Raspberry Pi 5. PR for additional IMU supports are wellcomed.

## Instructions
1. Ensure your Raspberry Pi i2c enabled. [References](https://pi3g.com/enabling-and-checking-i2c-on-the-raspberry-pi-using-the-command-line-for-your-own-scripts/)
2. `cd ros2_ws`
3. `git clone https://github.com/mich1342/ros2_rpi_imu.git ./src/ros2_rpi_imu`
4. `colcon build --symlink-install`
5. `source install/setup.bash`
6. `ros2 run ros2_rpi_imu ros2_rpi_imu`