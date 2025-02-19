from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'sea_rabbit'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name), glob('urdf/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bunnyguy',
    maintainer_email='pipandw@gmail.com',
    description='MHSeals Slam Toolbox/Nav2 programs',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_to_baselink = sea_rabbit.odom_to_baselink:main',
            'odom_to_baselink_test = sea_rabbit.odom_to_baselink_test:main',
        ],
    },
)
