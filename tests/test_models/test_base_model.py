#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8
from os import getenv


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel._doc_)
        self.assertIsNotNone(BaseModel._init.doc_)
        self.assertIsNotNone(BaseModel._str.doc_)
        self.assertIsNotNone(BaseModel.save._doc_)
        self.assertIsNotNone(BaseModel.to_dict._doc_)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "_init_"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "Using DB")
    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base._class.name_, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if _name_ == "_main_":
    unittest.main()
