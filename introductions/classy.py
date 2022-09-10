"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []


    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        rankings = {"tophat": 2, "bowtie": 4, "monocle": 5 }
        classiness = 0
        for item in self.items:
            if item in rankings.keys():
                classiness += rankings[item]
        return classiness


# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

def show_excitement():
    # Your code goes here!
    sentence = "I am super excited for this course! "
    return sentence * 5
