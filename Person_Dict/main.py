# Kyle Zarzana KJZ190000
# CS 4395.001
# Professor Karen Mazidi


import os  # used by method 1
import pickle
import re
import sys  # to get the system parameter


class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("\nEmployee with id: " + self.id)
        print(self.first + " " + self.mi + " " + self.last)
        print(self.phone)


# This method reads in the file at specified filepath
def method1(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        f.readline()
        text_in = f.read()

    return text_in


# This method processes the data given in the file and places them in a dictionary to be looked up later
def process_file(text_in):
    personDict = {}

    for line in text_in.split("\n"):
        s = line.split(",")

        lastName = s[0]
        firstName = s[1]
        mi = s[2]
        id = s[3]
        phone = s[4]

        # modify last and first name to be in capital case
        lastName = lastName.upper()
        firstName = firstName.upper()

        # modify mi to be capital
        if mi == "":
            mi = "X"

        mi = mi.upper()

        # modify id
        x = re.search("^[A-Za-z]{2}\d{4}", id)
        # loop until valid id is entered
        while not x:
            print("\nID Invalid: " + id)
            print("Valid ID is two letters followed by four digits.")
            id = input("Enter new ID for " + firstName + " " + lastName + ": ")
            x = re.search("^[A-Za-z]{2}\d{4}", id)

        # reformat phone number
        y = re.sub("[^0-9]", "", phone)
        y = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', y)
        print("\nPhone Number: " + phone + " reformated to: " + y)
        phone = y

        # add person data to dictionary
        newPerson = Person(lastName, firstName, mi, id, phone)
        personDict[newPerson] = id

    return personDict


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        text_in = method1(fp)

        personDict = process_file(text_in)

        pickle.dump(personDict, open('personDict.p', 'wb'))  # write binary
        dict_in = pickle.load(open('personDict.p', 'rb'))  # read binary
        for i in dict_in:
            i.display()
