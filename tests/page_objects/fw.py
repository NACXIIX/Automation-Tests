import HtmlTestRunner
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from behave import Given, when, then
import time

class Chrome():
    
    def chrome_driver():
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))