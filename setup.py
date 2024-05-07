from setuptools import find_packages, setup

package_name = 'ros2_rpi_imu'

i2clibraries = 'ros2_rpi_imu/i2clibraries'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name, i2clibraries],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mich1342',
    maintainer_email='michaeljonathan664@gmail.com',
    description='A simple ros2 package to interface IMU directly with Raspberry Pi',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'ros2_rpi_imu = ros2_rpi_imu.publish_imu:main'
        ],
    },
)
