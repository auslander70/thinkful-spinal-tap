class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Boom", "Crash", "Pssht", "Crack"])
        
    def count(self):
        print("1, 2, 3, 4!")
        
    def combust(self):
        print("BOOOOOOOOOOOOM!!!!1!")
        
        
class Band(object):
    def __init__(self, members):
        self.members = members
    
    def Hire(self, musician):
        self.members.append(musician)
        return self.members
        
    def Fire(self, musician):
        self.members.remove(musician)
        return self.members
        
    def Perform(self):
        for musician in self.members:
            if 'Drummer' in str(type(musician)):
                musician.count()
        for musician in self.members:
            musician.solo(10)
        for musician in self.members:
            if 'Drummer' in str(type(musician)):
                musician.combust()
                
        
if __name__ == '__main__':
    # instantiate band members
    mick_shrimpton = Drummer()
    nigel_tufnel = Guitarist()
    derek_smalls = Bassist()
    david_st_hubbins = Guitarist()
    
    # set up members
    members = [mick_shrimpton, derek_smalls, nigel_tufnel, david_st_hubbins]
    
    # initialize band
    spinal_tap = Band(members)
    
    # play a show
    spinal_tap.Perform()
    
    # fire exploded drummer
    spinal_tap.Fire(mick_shrimpton)
    
    # perform w/o a drummer
    spinal_tap.Perform()
    
    # hire a new drummer
    peter_james_bond = Drummer()
    spinal_tap.Hire(peter_james_bond)
    spinal_tap.Perform()