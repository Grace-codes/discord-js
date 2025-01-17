from setuptools import setup

version = "1.0.5"

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.readlines()

setup(
    name="discord.js",
    version=version,
    description="The Python module for discord.js.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    py_modules=["discordjs"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)
