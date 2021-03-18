class Player:
    def __init__(self): # dunder -> dabble underscores
            self.fname = ''
            self.lname = ''
            self.number = ''


class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

class Player3:
    #Attribute
    eyes='Blue'
    age=22

    #Method
    def thisMethod(self):
        print("hello this is Method.")

# obj=Player3()
# print(obj.eyes)
# obj.thisMethod()
class Player4:
    def createName(self,name):
        self.name=name
    def displayName(self):
        print('Hello :',self.name)

py4_1=Player4()
py4_2=Player4()
py4_1.createName('Player4_1')
py4_2.createName('Player4_2')
py4_1.displayName()
py4_2.displayName()

if __name__== '__main__':
    p1 = Player()
    p1.fname = 'Loris'
    p1.lname = 'Karius'
    p1.number = 1

    p2 = Player()
    p2.fname = 'Alex'
    p2.lname = 'Manninger'
    p2.number = 13

    p1a = Player2('Loris', 'Karius', 1)
    p2a = Player2('Alex', 'Manninger', 13)
    # print(p1a.fname)
    # print(p2a.lname)