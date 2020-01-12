# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

long_description = """
Map tile toolkits

- coordinate convert
- crawler
- map image concat

地图瓦片工具包 

- 坐标系转换
- 地图爬虫
- 地图拼接
"""
    
setup(
    name='mttk',

    description='Map tile toolkits (地图瓦片工具包）',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    version='0.1.1',

    license='GNU General Public License v3.0',
    author='anhenghuang',
    author_email='contact@anhenghuang.com',
    url='https://github.com/anhenghuang/MapTileToolKits',

    packages=['mttk'],
    install_requires=[
        "numpy",
        "opencv-python",
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],

)
