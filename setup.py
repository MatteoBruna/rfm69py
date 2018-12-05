from setuptools import setup, find_packages

setup(
    name="rfm69py",
    version="1.0.0",
    install_requires=["spidev", "RPi.GPIO"],
    packages=find_packages()
)
