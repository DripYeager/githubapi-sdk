from githubapisdk import GitHubAPIClient

github_client= GitHubAPIClient()
github_client.set_api_token('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')

username= 'DripYeager'

repo_count= github_client.get_repository_count(username)

print(f'{username} has {repo_count} public repositories on GitHub')