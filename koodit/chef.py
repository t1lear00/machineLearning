
class chef():
    def __init__(moi, nameofchef):
        moi.name = nameofchef
    
    def printName(moi):
        print(moi.name)
    def    makesoup(moi):
            print(moi.name, "making soup")
    def    makeSalad(moi):
            print(moi.name, "making salad")        

class italianchef(chef):
    def __init__(moi, nameofchef):
        moi.name = nameofchef
    def makepasta(moi):
        print(moi.name, "making pasta")
        
chef1 =chef("Gordon Ramsey")
chef1.printName()
chef1.makesoup()

chef2 = italianchef("James cook")
chef2.makeSalad()
