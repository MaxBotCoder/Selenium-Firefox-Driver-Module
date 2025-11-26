#modules
import os
import platform
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

#variables
    windows_binary = "C:\Program Files\Mozilla Firefox\"
    linux_binary = "/snap/firefox/7355/usr/lib/firefox/firefox"
    mac_bianry = ""
    
    windows_geckodriver = ""
    linux_geckodriver = "/snap/firefox/7355/usr/lib/firefox/geckodriver"
    mac_geckodriver = ""

#functions
def install_executable_files_windows():
    command = input("Would you like to downlaods executables to dowloads directory for you to manually install? (y/n): ")
    if command == "y":
        command = input("Again are you sure the files will be put in the downloads directory for you to manully install? (y/n):")
        if command == "y":
            options_binary_location = windows_binary
            gecko_service = Service(windows_geckodriver)
            download_driver = webdriver.Firefox(service=gecko_service,options=options_binary_location)
            download_driver.get("https://www.firefox.com/en-CA/download/all/desktop-release/win64/en-CA/")
            time.sleep(10)
            download_driver.find_element("/html/body/div[2]/main/div/div/div[2]/div/p/a").click()
            time.sleep(10)
            download_driver.get("https://github.com/mozilla/geckodriver")
        else:
            print("exiting!")
    else:
        print("exiting!")
    
def install_executable_files_linux():
    command = input("Would you like to get files to manually install required version of firefox within your downlaods directory? (y/n):")
    if command == "y":
        command = input("Are you sure you want them installed within your downloads directory? (y/n): ")
        if command == "y":
            options_binary_location = windows_binary
            gecko_service = Service(windows_geckodriver)
            download_driver = webdriver.Firefox(service=gecko_service,options=options_binary_location)
            download_driver.get("https://snapcraft.io/?_gl=1*1vkfx1b*_gcl_au*MTYzNzA3NDIzOS4xNzYwMTE3MTAy*_ga*NTIxMDQzNzYxLjE3NjAxMTcwOTk.*_ga_5LTL1CNEJM*czE3NjQwOTI2MjQkbzgkZzEkdDE3NjQwOTI2MjQkajYwJGwwJGgw")
            time.sleep(5)
            download_driver.find_element(by=By.XPATH,value="/html/body/dialog/div/div/div/p[4]/button[2]").click()
            time.sleep(3)
            download_driver.find_element(by=By.XPATH,value="/html/body/dialog/div/div/button").click()
        else:
            print("existing!")
    else:
        print("existing!")
    
def windows_firefox_driver():
    options_binary_location = windows_binary
    gecko_service = Service(windows_geckodriver)
    if os.path.exists(windows_binary) and os.path.exists()windows_geckodriver:
        print("Executable detected!")
        windows_driver = webdriver.Firefox(service=gecko_service,options=options_binary_location)
    else:
        install_executable_files_windows()
    
def linux_firefox_driver():
    options_binary_location = linux_binary
    gecko_service = Service(linux_geckodriver)
    if os.path.exists(linux_binary):
        print("Snap Detected!")
        firefox_driver = webdriver.Firefox(service=gecko_service,options=options_binary_location)
    else:
        print("Error snap required!")
        
    
def mac_firefox_driver():

#if system
if platform.system() == "Windows!":
    print("Warning windows may require manual gecko driver and may also require .exe installation of firefox too MICROSOFT STORE FIREFOX IS NOT RECOMMENDED! \n")
    windows_binary = input("Please enter gecko driver location: ")
elif platform.system() == "Linux!":
    linux_firefox_driver()
elif platform.system() == "Mac!"
else:
    print("Error Unsupported System!")
