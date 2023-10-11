import  requests
class GitHubAPIClient:
    def __init__(self):
        self.api_token= None
        self.base_url='https://api.github.com/'

    def set_api_token(self,api_token):
        self.api_token=api_token

    def get_repository_count(self, username):
        if self.api_token is None:
            raise ValueError("API token is not set. Use set_api_token to provide valid token.")
        if not username or not isinstance(username,str):
            raise ValueError("Invalid username. Provide a non empty string as the username.")

        url= f'{self.base_url}users/{username}'
        headers= {'Authorization': f'Bearer {self.api_token}'}
        response= requests.get(url,headers=headers)
        if response.status_code == 200:
            user_data= response.json()
            return user_data.get('public_repos',0)
        else:
            return None