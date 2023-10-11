
# GitHub API SDK

The githubapi-sdk is a Python package that provides a simple SDK (Software Development Kit) for accessing the GitHub API. You can use this package to retrieve information about a GitHub user's public repositories.

## Installation
To use the **githubapi-sdk** package, you can download the distribution package file (**'githubapi-sdk-0.1.tar.gz'**) and install it using **'pip'**. Here's how you can do it:

1. **Download the Package:**

You can obtain the distribution package from dist. Save the file as githubapi-sdk-0.1.tar.gz.

2. **Install the Package:**

Open your terminal and navigate to the directory where you saved the **'githubapi-sdk-0.1.tar.gz'** file. Then, use pip to install the package:
```python
pip install githubapi-sdk-0.1.tar.gz
```
## Usage

After installing the package, you can use it in your Python code as follows:
```python
from githubapisdk import GitHubAPIClient

github_client= GitHubAPIClient()
github_client.set_api_token('your_token')

username= 'DripYeager'

repo_count= github_client.get_repository_count(username)

print(f'{username} has {repo_count} public repositories on GitHub')
```
This code imports the **'get_repository_count'** function from the **'githubapisdk'** package and uses it to retrieve the number of public repositories for a specified GitHub user.

