import unittest
from githubapisdk import get_repository_count

class TestGitHubAPISDK(unittest.TestCase):
    def test_get_repository_count(self):
        # Test cases for your SDK functions
        self.assertEqual(get_repository_count('DripYeager'), 5)  # Replace 'your_username' and 10 with actual values
        self.assertEqual(get_repository_count('MihirVangani17'), 6)
if __name__ == '__main__':
    unittest.main()
