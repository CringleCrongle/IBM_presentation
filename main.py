import sys

import pyfiglet
import time
import os

clear = lambda: os.system('cls')

list_of_reasons = ["1. I love problem solving and coding! \n",
                   "2. I have always loved space and astronomy! \n",
                   "3. IBM is at the cutting edge of research in fields such as applying AI and cloud computing to fight climate change \n"]

hello_banner = pyfiglet.figlet_format("Hello, I am Chris!")
why_banner = pyfiglet.figlet_format("Why did I choose IBM?")

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)


print(hello_banner)
time.sleep(5)

print(why_banner)
time.sleep(3)


for counter in range(0, len(list_of_reasons)):
    currentText = list_of_reasons[counter]
    typingPrint(currentText)
    time.sleep(2)