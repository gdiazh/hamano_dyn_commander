from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hamano_dyn_commander'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('*.py')),
        ('share/' + package_name, ['launch/joy_control_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='moonshot',
    maintainer_email='g.hernan.diaz@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server_commander = hamano_dyn_commander.server_commander:main',
            'server_multicommander_m2 = hamano_dyn_commander.server_multicommander_module2:main',
            'server_multicommander_m3 = hamano_dyn_commander.server_multicommander_module3:main',
            'client_multicommander = hamano_dyn_commander.client_multicommander:main'
        ],
    },
)
