import os
from glob import glob

from setuptools import setup

package_name = 'ros2_numpy'

data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'])
    ]

def glob_recursive(data_files, directory):
    files = glob(directory+'*.*')
    data_files.append((os.path.join('share', package_name, directory), files))
    subdirectories = glob(directory+'*/')
    if (subdirectories == []):
        return
    else:
        for dir in subdirectories:
            glob_recursive(data_files, dir)

data_directories = ['ros2_numpy', 'test']

for directory in data_directories:
    glob_recursive(data_files, directory)


setup(
    name=package_name,
    version='2.0.4',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tom Panzarella',
    maintainer_email='wieser@mit.edu',
    description='A collection of conversion functions for extracting numpy arrays from messages',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
