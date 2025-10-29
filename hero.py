from entity import Entity
import random
from map import Map

class Hero(Entity):
    
    
    def __init__(self, name):
        super().__init__(name, 25)
        self.row = 0
        self.col = 0

    @property
    def location(self):
        return (self.row, self.col)


    def attack(self, entity):
        
        attack_damage = random.randint(2, 5)
        entity.take_damage(attack_damage)
        return f'{self.name} attacks a {entity.name} for {attack_damage} damage'
    
    def go_north(self):

        if self.row > 0:
            self.row -= 1
            return Map()[self.row][self.col]
        return 'o'
    
    def go_south(self):
        
        if self.row < len(Map()) - 1:
            self.row += 1
            return Map()[self.row][self.col]
        return 'o'
    
    def go_east(self):
        if self.col < len(Map()[self.row]) - 1:
            self.col += 1
            return Map()[self.row][self.col]
        return 'o'
    
    def go_west(self):
        if self.col > 0:
            self.col -= 1
            return Map()[self.row][self.col] 
        return 'o'