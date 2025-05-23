from setuptools import setup, find_packages

setup(
    name="ccmd-logger",
    version="0.1.1",
    packages_dir=find_packages(where='src'),
    install_requires=[
        "coloredlogs>=15.0.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple colored logging utility for the ccmd-logger project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ccmd-logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 