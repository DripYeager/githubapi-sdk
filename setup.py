from setuptools import setup, find_packages

setup(
    name='githubapi-sdk',
    version='0.1',
    description='SDK for accessing GitHub API',
    author='Saransh Jaiswal',
    author_email='saranshjaiswal09@gmail.com',
    packages=find_packages(),  # Automatically find all packages in your project
    install_requires=[
        'requests',
    ],
)
