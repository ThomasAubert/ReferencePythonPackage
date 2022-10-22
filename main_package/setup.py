from setuptools import setup, find_packages

setup(
    author="Thomas Aubert",
    description="A dummy package to reference best practices.",
    name="main_package",
    version="0.1.0",
    packages=find_packages(include=["main_package", "main_package.*"]),
#    install_requires=["pandas>=1.0", "scipy"],
    python_requires=">=3.7.*"
)
