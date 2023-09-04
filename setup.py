from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event/__init__.py
from event import __version__ as version

setup(
	name="event",
	version=version,
	description="event",
	author="frappe",
	author_email="frappe@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
