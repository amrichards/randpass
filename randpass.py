# Quick word-based passwords from a file with added break characters
# By: Adam M Richards
# Use: in conjunction with a word list, create random passwords including
# break characters in between words
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
from os.path import exists
from random import shuffle, SystemRandom
from string import digits, punctuation
from sys import argv


def load_word_list(filename):
    if not exists(filename):
        raise IOError('\'{}\' does not exist!'.format(filename))
    with open(filename, 'r') as f:
        words = [line.rstrip() for line in f]
    if not words:  # empty file
        raise IOError('\'{}\' does not seem to have any words!')
    shuffle(words)
    return words


def generate_password(total_words):
    pwd_list = []
    for _ in range(total_words):
        pwd_list.append(CHOICE(WORD_LIST))
        pwd_list.append(CHOICE(punctuation))
    pwd = ''.join(pwd_list[:-1])  # skip last break character?
    return '{}\n{}\n{}\n{}\n'.format(pwd.lower(), pwd.upper(),
                                     pwd.title(), pwd.title().swapcase())


BREAK_CHARS = digits + punctuation
CHOICE = SystemRandom().choice
FILENAME = 'wordlist.txt'
MAX_WORDS = 10
MIN_WORDS = 2

if __name__ == '__main__':
    try:
        # try to load custom word list from command line argument
        # loads default word list if that fails (empty or doesn't exist)
        # example: python randpass.py wordlist2.txt
        WORD_LIST = load_word_list(argv[1])
    except (IndexError, IOError):
        # example: python randpass.py
        WORD_LIST = load_word_list(FILENAME)

    while True:
        try:
            num_words = int(raw_input(
                'Enter # of words ({} - {}): '.format(MIN_WORDS, MAX_WORDS)))
            if MIN_WORDS <= num_words <= MAX_WORDS:
                print(generate_password(num_words))
                break
        except ValueError:
            pass  # print('Error! Must be an integer!')
