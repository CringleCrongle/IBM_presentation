import pyfiglet
import time
import os

clear = lambda: os.system('cls')

hello_banner = pyfiglet.figlet_format("Hello, I am Chris!")
print(hello_banner)
time.sleep(5)
why_banner = pyfiglet.figlet_format("Why did I choose IBM?")
print(why_banner)
time.sleep(3)
print("")