from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as rm:
    long_description = rm.read()

setup(
    name="aws-snappy",
    version="2.1.0",
    author="Mervin Hemaraju",
    author_email="th3pl4gu33@gmail.com",
    description="Snappy is a Python library that facilitates taking root volume snapshots from EC2 as well as other EBS volumes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mervinhemaraju/snappy",
    packages=find_packages(exclude=('tests')),
    install_requires=[
          'boto3'
      ],
    test_suite="tests",
    python_requires=">=3.7",
)