import random


class Game:
    """ Object to manipulate game
    """

    length = 5

    def __init__(self):
        self.source = self.generate_source()
        self.turn = 0
        self.won = False

    def generate_source(self):
        allowed = '0123456789'
        return random.sample(allowed, self.length)

    def check(self, combination):
        result = ''
        for index, letter in enumerate(combination):
            if letter == self.source[index]:
                let = '#'
            elif letter in self.source:
                let = '?'
            else:
                let = '_'
            result = result + let
        print('Turn {}'.format(self.turn))
        print('----- ' + result + ' -----')
        print('----- ' + combination + ' -----')
        if result == '#####':
            return True
        return False

    def start(self):
        while not self.won:
            self.turn += 1
            combination = input('Input combination: ')
            combination = combination[:self.length]
            result = self.check(combination)
            self.won = result



def play_game():

    g = Game()
    g.start()

    if input('Play again (y/n): ') in 'Yy':
        return True
    return False


if __name__ == '__main__':
    while play_game():
        pass
