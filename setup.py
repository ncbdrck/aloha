from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    name='aloha',
    packages=['aloha'],
    package_dir={'': 'src'},

    description="ALOHA: A Low-cost Open-source Hardware System for Bimanual Teleoperation",

    author='Tony Zhao',
    author_email='tonyzhao@stanford.edu',
)

setup(**setup_args)