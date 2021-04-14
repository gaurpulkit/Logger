import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Logger-Zuj3brusu",
    version="2.0",
    author="Zuj3brusu",
    description="Create logs on Discord, Telegram or a local file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zuj3brusu/Logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
