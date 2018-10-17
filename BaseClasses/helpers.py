__author__ = 'Sajjad'
import uuid
import faker
from BaseClasses.const import BASE_URL


def get_random_company_names():
    """
    Get random company names.
    """
    company_name = 'company{}'.format(str(uuid.uuid4().node))
    return company_name


def get_random_credential():
    fake = faker.Faker()
    account_manager_name = fake.name()
    work_email = fake.email()
    return account_manager_name, work_email


def get_registration_fields(
    work_email="", company_name="", country="", your_insly_address="", terms_and_condition=False,privacy_policy=False,
    phone="",password="", company_profile="", number_of_employees="", describe_yourself="", account_manager_name="",
    repeat_password="", agree_data_processing=False, fields_to_be_removed=None):

    get_company_name = get_random_company_names()
    get_account_manager_name, get_work_email = get_random_credential()
    registration_fields = {
        'company_name': company_name or get_company_name,
        'country': country or "IN",
        'insly_address': your_insly_address or get_company_name,
        'company_profile': company_profile or "SDC",
        'number_of_employees': number_of_employees or "30",
        'describe_yourself': describe_yourself or "tech",
        #Admin Account Details
        'work_email': work_email or get_work_email,
        'account_manager_name': account_manager_name or get_account_manager_name,
        'password': password,
        'suggest_secure_password': "click",
        'repeat_password': repeat_password,
        'phone': phone or "3006532211",
        'terms_and_condition': terms_and_condition,
        'privacy_policy': privacy_policy,
        'privacy_policy_link': "click",
        'terms_condition_link': "click",
        'agree_data_processing': agree_data_processing
    }
    if fields_to_be_removed is not None:
        for field in fields_to_be_removed:
            registration_fields.pop(field)
    return registration_fields


def select_val_from_drop_down(page, parent_css, child_css, use_jquery=False):
    #parent_object = page.browser.find_element(parent_css)
    #child_element = page.browser.find_element('{} option[value="{}"]'.format(parent_css, child_css))
    if use_jquery:
        page.browser.execute_script('$("{}").val("{}");'.format(parent_css, child_css))


def open_link(page, parent_css, child_css,):
    page.browser.execute_script('$("{}").trigger("{}")'.format(parent_css, child_css))


def capture_screens(self):
    self.screenshot(BASE_URL, 'SignUp_form.png')