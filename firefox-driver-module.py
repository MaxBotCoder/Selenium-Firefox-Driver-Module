#modules
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

#variables
options_executable = Options()
options_executable.binary_location = "/snap/firefox/7298/usr/lib/firefox/firefox"
gecko_service = Service("/snap/firefox/7298/usr/lib/firefox/geckodriver")
firefox_driver = webdriver.Firefox(service=gecko_service,options=options_executable)
