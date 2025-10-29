import random
from entity import Entity


class Enemy(Entity):
    
    def __init__(self):
        
        name = random.choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie'])
        hp = random.randint(4, 8)
        super().__init__(name, hp)
        
        
    def attack(self, entity):
        
        
        attack_damage = random.randint(1, 4)
        entity.take_damage(attack_damage)
        return f'{self.name} attacks {entity.name} for {attack_damage} damage'