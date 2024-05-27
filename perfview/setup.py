# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com


from setuptools import setup, find_packages

package_name = 'perfview'

setup(name='perfview',
      version='1.0',
      description='perf view app',
      author='zhangxiaoan',
      author_email='zhangxiaoan_v@didiglobal.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      entry_points={
            'console_scripts': [
                  'perfview=perf_processor.data_pb:main'
            ]
      }
     )