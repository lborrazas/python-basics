from unittest import TestCase
from mock import patch
from classes import DummyClass

def shout_fake(a):
    return "FAKE"

class DummyTest(TestCase):

    @patch("classes.DummyClass.shout_dummy")
    def test_dummy_func(self, mock_func):
        mock_func.return_value = "HELLO"
        dcls = DummyClass("f")
        a = dcls.shout_dummy()
        print(a)

    @patch("classes.DummyClass.shout_dummy", new=shout_fake)
    def test_dummy_two(self):
        dcls = DummyClass("f")
        a = dcls.shout_dummy()
        print(a)

    @patch("classes.DummyClass.shout_dummy", lambda x: "hola")
    def test_dummy_three(self):
        dcls = DummyClass("f")
        a = dcls.shout_dummy()
        print(a)

    @patch("dummy_test.DummyClass")
    def test_dummy_three(self, dummy_class_mock):
        instance = dummy_class_mock.return_value
        instance.shout_dummy.return_value = "NICE"
        dcls = DummyClass("f")
        a = dcls.shout_dummy()
        self.assertEqual("NICE", a)
