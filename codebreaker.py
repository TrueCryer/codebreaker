""" Code Breaker.

Implementation of Code Breaker game for command line
Copyright (C) 2017  Sergey Ozerov aka TrueCryer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import random


__version__ = '1.0.0'


class Game:
    """ Object to manipulate game
    """

    def __init__(self, length, mode):
        self.length = length
        self.source = self.generate_source(mode)
        self.turn = 0
        self.won = False

    def generate_source(self, mode):
        allowed = '0123456789'
        if mode == 'h':  # Hard. Digits can repeat.
            return ''.join([random.choice(allowed) for i in range(self.length)])
        else:
            return random.sample(allowed, self.length)

    def check(self, combination):
        result = ''
        for index, letter in enumerate(combination):
            if letter == self.source[index]:
                let = '+'
            elif letter in self.source:
                let = '?'
            else:
                let = '_'
            result = result + let
        print('Turn {}'.format(self.turn))
        print('----- ' + result + ' -----')
        print('----- ' + combination + ' -----')
        if result == '+'*self.length:
            return True
        return False

    def start(self):
        while not self.won:
            self.turn += 1
            combination = input('Input combination: ')
            combination = combination[:self.length]
            result = self.check(combination)
            self.won = result


def play_game(args):

    length, mode = args.len, args.mode
    length = min(length, 8)

    g = Game(length=length, mode=mode)
    g.start()

    if input('Play again (y/n): ') in 'Yy':
        return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--len',
        type=int,
        default=5,
        help='Length of code. Default 5 digits',
    )
    parser.add_argument(
        '--mode',
        choices=['n', 'h'],
        default='n',
        help='Game mode: n(ormal) or h(ard).'
    )
    args = parser.parse_args()
    print(args)
    while play_game(args):
        pass
