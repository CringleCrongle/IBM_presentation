import pyfiglet

listOfReasons = ["1. I love problem solving and coding! \n",
                 "2. Local company - family lives just outside Basingstoke \n",
                 "3. I have always loved space and astronomy! - IBM has been working in this field for over 50 years "
                 "& helped with landing on the Moon \n",
                 "4. IBM's Space Situational Awareness Project -  helping to try and solve the issue of space debris "
                 "and overcrowding \n"]


listOfGoals = ["1. To learn new skills and improve existing ones by working with the experienced engineers at IBM \n",
               "2. To get to apply my knowledge to solve real world problems! \n",
               "3. I have always wanted to work on satellites - links my interests in programming and space - I can "
               "see a clear path to achieving this with IBM"]

helloBanner = pyfiglet.figlet_format("Hi, I'm  Chris!")
whyBanner = pyfiglet.figlet_format("Why did I choose IBM?")
goalsBanner = pyfiglet.figlet_format("What do I want to achieve at IBM?")
q_and_aBanner = pyfiglet.figlet_format("Any questions?")


def print_list(name_of_list):
    for counter in range(0, len(name_of_list)):
        print(name_of_list[counter])
        input()


def presentation_flow():
    print(helloBanner)
    print("I'm a second year Computer Science student at Swansea University")
    input()
    print(whyBanner)
    input()
    print_list(listOfReasons)
    print(goalsBanner)
    input()
    print_list(listOfGoals)
    print(q_and_aBanner)
    print("This presentation is available to view on my Github, under the name 'IBM_presentation'")


presentation_flow()
