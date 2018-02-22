class Parent():
    def __init__(self, lastName, eyeColor):
        #print("Parent Constructor Called")
        self.lastName = lastName
        self.eyeColor = eyeColor

    def showInfo(self):
        print("Last Name - " + self.lastName)
        print("Eye Color - " + self.eyeColor)

class Child(Parent):
    def __init__(self, lName, eColor, number):
        Parent.__init__(self, lName,eColor) #this is like calling super()
        self.number = number

    #METHOD OVERRIDING
    def showInfo(self):
        print("Last Name - " + self.lastName)
        print("Eye Color - " + self.eyeColor)
        print("Number of toys - " + str(self.number))

nick = Parent("Guinand", "Hazel")
child = Child("Tickle", "red", "6")
#print(nick.lastName)
child.showInfo()