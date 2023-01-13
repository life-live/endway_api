# -*- coding: utf-8 -*-
from unittest import TestCase, main

from endway_api import EndWayApi


class EndWayApiTests(TestCase):
    def setUp(self):
        self.ewApi = EndWayApi("xf_user")

    def test_post_thread(self):
        result = self.ewApi.post_thread(131, "Test", "Test")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_add_reply(self):
        result = self.ewApi.add_reply(1236, "Test")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_member_post(self):
        result = self.ewApi.member_post(366, "Test")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_add_comment(self):
        result = self.ewApi.add_comment(513, "Test")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_account_details(self):
        result = self.ewApi.account_details(location="Test", about_html="Test User")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_security(self):
        result = self.ewApi.security("qwerty", "qwerty123")
        print(result.json())
        self.assertEqual(result.status_code, 200)

    def test_signature(self):
        result = self.ewApi.signature("Test User")
        print(result.json())
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    main()
