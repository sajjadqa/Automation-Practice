__author__ = 'Sajjad'
import os
TARGET_URL = os.getenv("URL", "insly.com")
SIGNUP_URL = os.getenv("SIGNUP", 'signup')
BASE_URL = "https://{}.{}".format(SIGNUP_URL, TARGET_URL)