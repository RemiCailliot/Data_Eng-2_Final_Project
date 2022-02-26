import calc
import unittest
import app
from flask import Flask
from app import create_app
from flask_testing import TestCase

class TestCalc(TestCase):

    def create_app(self):
        return create_app()

    def test_assert_200(self):
        self.assert200(self.client.get("/"))

    def mean_test(self):
        self.assertEqual(calc.mean(5,6),5.5)