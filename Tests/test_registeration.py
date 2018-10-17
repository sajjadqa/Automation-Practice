__author__ = 'Sajjad'
import unittest
from Tests.base_test import UserBaseClass
from BaseClasses.helpers import get_registration_fields


class TestRegistration(UserBaseClass):
    def setUp(self):
        super(TestRegistration, self).setUp()

    def test_complete_registration_process(self):
        reg_fields = get_registration_fields()
        self.register_user(reg_fields)
        self.dashboard.is_browser_on_page()
        #self.dashboard.get_current_url()
        self.assertEqual(self.dashboard.get_current_url(), self.dashboard.compare_url(reg_fields))
        self.assertIn("/dashboard", self.dashboard.get_current_url())

    def test_registration_email_name_fields_empty(self):
        expected_errors = "Company name: Required field is empty"
        self.register.is_page_title_visible_on_page()
        self.register_user(get_registration_fields(fields_to_be_removed=["company_name"]))
        self.assertEqual(expected_errors in self.register.error_messages(), True)

    def test_registration_invalid_phone_field(self):
        expected_errors = "Phone: Field contains invalid characters (Please enter a valid phone number)"
        self.register.is_page_title_visible_on_page()
        self.register_user(get_registration_fields(fields_to_be_removed=["phone"]))
        self.assertIn(expected_errors, self.register.error_messages(), True)
