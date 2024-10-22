from setuptools import find_packages, setup

package_name = 'hamano_dyn_commander'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'server_commander = hamano_dyn_commander.server_commander:main'
        ],
    },
)
