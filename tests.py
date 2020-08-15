import unittest
import json
import geocoding

RADIUS = 50
VALID_USER = json.loads('{"latitude":51.6553959, "longitude": 0.0572553}')
INVALID_USER = json.loads('{"latitude":-6.7098551, "longitude": 111.3479498}')
EXACT_USER = json.loads('{"latitude":52.1092851, "longitude": 0.5352174}')

class TestRadius(unittest.TestCase):
    
    def test_in_radius(self):
        user_list = [VALID_USER]
        result = geocoding.users_in_radius(user_list, RADIUS)

        self.assertEqual(len(result), 1)
    
    def test_not_radius(self):
        user_list = [INVALID_USER]
        result = geocoding.users_in_radius(user_list, RADIUS)

        self.assertEqual(len(result), 0)

    def test_exact_radius(self):
        user_list = [EXACT_USER]
        result = geocoding.users_in_radius(user_list, RADIUS)

        self.assertEqual(len(result), 1)

    def test_multiple_users(self):
        user_list = [VALID_USER, INVALID_USER, EXACT_USER]
        result = geocoding.users_in_radius(user_list, RADIUS)

        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()