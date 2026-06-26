import random
class Character:
    def __init__(self, name , health):
        self.name = name
        self.health = health

    def attack(self,opponent):
        opponent.health -= self.damage
        print(f"{self.name} attacks {opponent.name} damage: {self.damage}")
        print(f"Remained health of {opponent.name}:{opponent.health}")
    
    def show_status(self,opponent):
        print(f"{self.name} Health:{self.health}|{opponent.name} Health:{opponent.health}")
    
#charcter subclass
class Warrior(Character):
    def __init__(self , name):
        super().__init__(name , 100)
        self.damage = 20
        self.reduce = 10

    def skill(self):
        self.health += self.reduce
        print(f"Damage Taken reduced by {self.reduce}")
class Mage(Character):
    def __init__(self , name):
        super().__init__(name , 100)
        self.damage = random.randint(10,30)
        self.mana = 8

    def attack(self,opponent):
        self.damage = random.randint(10,30)
        super().attack(opponent)
    
    def skill(self):
        self.health += self.mana
        print(f"Healing skil used and healed by {self.mana}")
        
class Archer(Character):
    def __init__(self , name):
        super().__init__(name , 100)
        self.damage = 15
        self.dodge = 20

    def skill(self):
        if random.random < 0.3:
            self.health += self.dodge
            print(f"Dodge successful! Recovered {self.dodge} health!")

        else:
            print("Dodge failed this time!")
    



        
        
