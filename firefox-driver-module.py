#modules
import os
import platform
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

#variables
windows_binary = "C:\Program Files\Mozilla Firefox\\"
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
    command = input("The following will display required commands to install firefox & geckodriver on linux would you like them to be displayed? (y/n):")
    if command == "y":
        command = input("Are you sure? (y/n): ")
        if command == "y":
            print("!!!ONLY USE THE COMMANDS APPLICABLE TO YOUR DISTRO!!! \n")
            print("Debian commands (apt): sudo apt install snapd && sudo snap install firefox")
            print("Dedora commands (dnf): sudo dnf install snapd && sudo snap install firefox")
            print("Open Suse commands (zypper): sudo zypper install snapd && sudo snap install firefox")
            print("Arch commands (pacman): sudo pacman -S snapd && sudo snap install firefox")
            print("Gentoo commands (portage): Sorry available at the moment!")
        else:
            print("existing!")
    else:
        print("existing!")
    
def windows_firefox_driver():
    options_binary_location = windows_binary
    gecko_service = Service(windows_geckodriver)
    if os.path.exists(windows_binary):
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
        install_executable_files_linux()
    
def mac_firefox_driver():
    print("Your platform is not supported yet!")

#if system
if platform.system() == "Windows!":
    print("Warning windows may require manual gecko driver and may also require .exe installation of firefox too MICROSOFT STORE FIREFOX IS NOT RECOMMENDED! \n")
    windows_binary = input("Please enter gecko driver location: ")
elif platform.system() == "Linux!":
    linux_firefox_driver()
elif platform.system() == "Mac!"
    mac_firefox_driver()
else:
    print("Error Unsupported System!")
