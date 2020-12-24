import setuptools


small_desc = "Controller for bot to control your PC through telegram messages"
with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="dspc_bot_ctrl",
    version="1.0.2",
    author="Rojit George",
    author_email="rojitrgeorge@gmail.com",
    description=small_desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/krrgeorges/dspc_bot_ctrl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)
