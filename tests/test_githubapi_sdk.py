import unittest
from githubapisdk import GitHubAPIClient

class TestGitHubAPIClient(unittest.TestCase):
    def setUp(self):
        self.github_client= GitHubAPIClient()
        self.github_client.set_api_token('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') #Replacing with the API token

    def test_get_repository_count(self):
        repo_count1= self.github_client.get_repository_count('DripYeager')
        repo_count2= self.github_client.get_repository_count('MihirVangani17')

        self.assertEqual(repo_count1,6)
        self.assertEqual(repo_count2,6)

    if __name__ == '__main__':
        unittest.main()
