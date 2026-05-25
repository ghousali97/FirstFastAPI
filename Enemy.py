class Enemy:
    type: str
    health: int = 10 #we can set a default value for an attribute in a class, so that it will be set by default. 
    damage: int #we need to define the type of attribute in a class, otherwise it will be treated as a class variable and shared across all instances of the class. 
  
    def __init__(self, type: str, health: int = 100, damage: int = 10): # constructor
        self.type = type
        self.health = health
        self.damage = damage


    def talk(self):
        print(f"I am a {self.type}. Be prepared to fight!")

    def walk_forward(self):
        print(f"The {self.type} moves closer to you.")

    def attack(self):
        print(f"The {self.type} attacks you for {self.damage} damage!")

       