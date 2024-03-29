import random

class Creature:
    def __init__(self, name):
        self.name = name
        self.moves = ["Twirl", "Leap", "Spin"]
        self.current_move_index = 0

    def dance(self):
        if self.name == "Lox":
            moves = ["Twirl", "Twirl", "Spin", "Leap", "Leap"]
            move = moves[self.current_move_index]
            self.current_move_index = (self.current_move_index + 1) % len(moves)
            return move
        elif self.name == "Drako":
            moves = ["Spin", "Spin", "Leap", "Spin", "Twirl"]
            move = moves[self.current_move_index]
            self.current_move_index = (self.current_move_index + 1) % len(moves)
            return move
        else:
            move = self.moves[self.current_move_index]
            self.current_move_index = (self.current_move_index + 1) % len(self.moves)
            return move


class Forest:
    def __init__(self):
        self.state = "Normal"

    def change_state(self, move1, move2):
        if move1 == "Twirl" and move2 == "Twirl":
            self.state = "Fireflies light up the forest"
        elif (move1 == "Leap" and move2 == "Spin"):
            self.state = "Gentle rain starts falling"
        elif move1 == "Spin" and move2 == "Leap":
            self.state = "A rainbow appears in the sky"
        elif move1 == "Leap" and move2 == "Leap":
            self.state = "Ground starts to colour in purple"
        elif move1 == "Twirl" and move2 == "Spin":
            self.state = "Flowers bloom in vibrant colors"
        elif move1 == "Spin" and move2 == "Spin":
            self.state = "Stars twinkle and fill the sky"
        else:
            self.state = "A rainbow appears in the sky"

    def display_state(self):
        print(f"The state of the forest is: {self.state}")


def encounter_creature():
    lox = Creature("Lox")
    drako = Creature("Drako")
    forest = Forest()

    for _ in range(5):
        lox_move = lox.dance()
        drako_move = drako.dance()
        forest.change_state(lox_move, drako_move)
        print(f"{lox.name} dances: {lox_move}")
        print(f"{drako.name} dances: {drako_move}")
        forest.display_state()


def main():
    print('Welcome to the Magical Forest of Algora!')
    print('Enter your name:')
    name = input('> ')
    print(f'Hello, {name}! You are now in the Magical Forest of Algora.')

    while True:
        print('What would you like to do?')
        print('1. Explore the forest')
        print('2. Encounter a creature')
        print('3. Exit')
        choice = input('> ')

        if choice == '1':
            explore_forest()
        elif choice == '2':
            encounter_creature()
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


def explore_forest():
    print('You are exploring the forest...')


if __name__ == '__main__':
    main()
