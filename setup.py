import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ais-wordnet-sim',
    version='2.0.0',
    author='Tan Nguyen',
    author_email='livw08@gmail.com',
    description='AIS Wordnet tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://https://github.com/liv1n9/ais-wordnet-sim",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'underthesea',
        'pymongo',
        'dnspython',
        'xlrd'
    ]
)