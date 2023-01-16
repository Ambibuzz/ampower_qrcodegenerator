from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ampower_qrgenerator/__init__.py
from ampower_qrgenerator import __version__ as version

setup(
	name="ampower_qrgenerator",
	version=version,
	description="An app to generate QR Code",
	author="ithead@ambibuzz.com",
	author_email="buzz.us@ambibuzz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
