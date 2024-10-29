from setuptools import setup, find_packages

setup(
    name="is-seven",
    version="0.1.0",
    packages=find_packages(),
    description="A library to check if a number is seven",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Brian Chan",
    author_email="chanwingho94@gmail.com",
    url="https://github.com/cwingho/is-seven",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7", 
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="seven, number, validation",
    project_urls={
        "Bug Reports": "https://github.com/cwingho/is-seven/issues",
        "Source": "https://github.com/cwingho/is-seven",
    },
    python_requires=">=3.6",
    install_requires=[],
)