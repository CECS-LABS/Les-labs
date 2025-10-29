'''
LAB 10 - SINGLETON
Lesley Burgueno
Douglas Sam
10/27/2025

'''

from hero import Hero
from enemy import Enemy 
import check_input
import random
from map import Map

def monster_encounter(hero):
    
    enemy = Enemy()
    print(f'A wild {enemy.name} appears!')
    print(enemy)

    while hero.current_hp > 0 and enemy.current_hp > 0:
        print('\nWhat will you do?')
        choice = check_input.get_int_range('1. Attack\n2. Run\nEnter choice:', 1, 2)
        
        if choice == 1:
            print(hero.attack(enemy))
            if enemy.current_hp <= 0:
                print(f'The {enemy.name} has been defeated!')
                return True
            print(enemy.attack(hero))
            if hero.current_hp <= 0:
                print(f'{hero.name} has been defeated! Game Over.')
                return False
            
        elif choice == 2:
            print('You ran away!')
            directions = [hero.go_north, hero.go_south, hero.go_east, hero.go_west]
            move = random.choice(directions)
            move()
            
            return True
        
def item_room(hero):
    
    if hero.current_hp == hero.max_hp:
        print('You found a health potion, but your health is already full.')
    else:
        hero.heal()
        print('You found a Health Potion! You drink it to restore your health.')





def main():
    user_name = input('What is your name, traveler?')
    game_map = Map()
    hero = Hero(user_name)
    game_map.reveal(hero.location)
    quit_game = False

    while hero.current_hp > 0 and not quit_game:
    
        print(f'{hero.name}\'s HP: {hero.current_hp}/{hero.max_hp}')
        print(game_map.show_map(hero.location))
        print('1. Go North')
        print('2. Go South')
        print('3. Go East')
        print('4. Go West')
        print('5. Quit')
        choice = check_input.get_int_range('Enter choice:', 1, 5)
        
        result = None
        if choice == 1:
            result = hero.go_north()
            if result == 'o':
                print('You cannot go that way...')
        elif choice == 2:
            result = hero.go_south()
            if result == 'o':
                print('You cannot go that way...')
        elif choice == 3:
            result = hero.go_east()
            if result == 'o':
                print('You cannot go that way...')
        elif choice == 4:
            result = hero.go_west()
            if result == 'o':
                print('You cannot go that way...')
        elif choice == 5:
            quit_game = True
            print('Thanks for playing!')
            break
        game_map.reveal(hero.location)
        
        if result == 'm':
            alive = monster_encounter(hero)
            if alive > 0:
                game_map.remove_at_loc(hero.location)
            else:
                break
                
        if result == 'i':
            item_room(hero)
            game_map.remove_at_loc(hero.location)

if __name__ == '__main__':
    main()