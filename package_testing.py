from githubapisdk import get_repository_count

username = 'DripYeager'  # Replace with a valid GitHub username
repo_count = get_repository_count(username)
print(f'{username} has {repo_count} public repositories on GitHub.')
