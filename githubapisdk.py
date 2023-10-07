import requests

GITHUB_API_BASE_URL = 'https://api.github.com/'

def get_repository_count(username):
    url = f'{GITHUB_API_BASE_URL}users/{username}'
    headers = {'Authorization': f'Bearer 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'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('public_repos', 0)
    else:
        return None
