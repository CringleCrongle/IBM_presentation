import pyfiglet
import os

listOfReasons = ["1. I love problem solving and coding! \n",
                 "2. I have always loved space and astronomy! \n"
                 "3. Local company - family lives just outside Basingstoke  \n",
                 "4. IBM is at the cutting edge of using AI and cloud computing to try and solve environmental and climate challenges \n"]

listOfGoals = ["1. To learn new skills and improve existing ones by working with the experienced engineers at IBM \n",
               "2. To get to apply my knowledge to solve real world problems! \n",
               "3. I have always wanted to work on satellites - links my interests in programming and space - I can see a clear path to achieving this through IBM"]

helloBanner = pyfiglet.figlet_format("Hello, I am Chris!")
whyBanner = pyfiglet.figlet_format("Why did I choose IBM?")
goalsBanner = pyfiglet.figlet_format("What do I want to achieve at IBM?")


def print_list(nameOfList):
    for counter in range(0, len(nameOfList)):
        print(nameOfList[counter])
        input()


def presentation_flow():
    print(helloBanner)
    input()
    print(whyBanner)
    input()
    print_list(listOfReasons)
    input()
    print(goalsBanner)
    input()
    print_list(listOfGoals)


presentation_flow()
