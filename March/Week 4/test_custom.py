import unittest
from proxydict import ProxyDict


class MyTestCase(unittest.TestCase):
    def test_item_assignment(self):
        user_data = {'name': 'Trey Hunner', 'active': False}
        proxy_data = ProxyDict(user_data)
        self.assertEqual(proxy_data['name'], 'Trey Hunner')
        with self.assertRaises(Exception):
            proxy_data['name'] = 'Robin chacko'
        with self.assertRaises(Exception):
            proxy_data['active'] = True

    def test_keys(self):
        user_data = {'name': 'Trey Hunner', 'active': False}
        proxy_data = ProxyDict(user_data)
        self.assertEqual(user_data.keys(), proxy_data.keys())

    def test_proxy(self):
        user_data = {'name': 'Trey Hunner', 'active': False}
        proxy_data = ProxyDict(user_data)
        user_data['active'] = True
        self.assertEqual(user_data['active'], proxy_data['active'])


if __name__ == '__main__':
    unittest.main()
