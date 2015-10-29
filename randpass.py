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
from argparse import ArgumentParser
from os.path import exists
from random import SystemRandom
from string import digits, punctuation


def generate_password(total_words):
    pwd_list = []
    for _ in range(total_words):
        pwd_list.append(CHOICE(WORD_LIST))
        pwd_list.append(CHOICE(BREAK_CHARS))
    pwd = ''.join(pwd_list[:-1])  # skip last break character?
    return '{}\n{}\n{}\n{}\n'.format(pwd.lower(), pwd.upper(),
                                     pwd.title(), pwd.title().swapcase())


def load_word_list(filename):
    if not exists(filename):
        raise IOError('\'{}\' does not exist!'.format(filename))
    with open(filename, 'r') as f:
        words = [line.rstrip() for line in f]
    if not words:  # empty file
        raise IOError('\'{}\' does not seem to have any words!')
    SHUFFLE(words)
    return words


def pwd_range(total_passwords):
    return MIN_PWDS <= total_passwords <= MAX_PWDS


def word_range(total_words):
    return MIN_WORDS <= total_words <= MAX_WORDS


def write_shuffled_word_list(filename):
    with open(filename, 'w') as f:
        for word in WORD_LIST:
            f.write('{}\n'.format(word))


# default break characters: 0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
BREAK_CHARS = digits + punctuation
CHOICE = SystemRandom().choice
FILENAME = 'wordlist.txt'
MAX_PWDS = 20   # maximum passwords to generate
MIN_PWDS = 1    # minimum passwords to generate
MAX_WORDS = 10  # maximum words per password
MIN_WORDS = 2   # minimum words per password
SHUFFLE = SystemRandom().shuffle

if __name__ == '__main__':
    # For help with command line args: python randpass.py -h
    parser = ArgumentParser(
        description='Quick word-based passwords from a file with '
                    'added random break characters')
    parser.add_argument('-c', action='store', dest='word_list',
                        help='Use a custom word list, by path',
                        default='')
    parser.add_argument('-b', action='store', dest='break_char',
                        help='Use a single custom break character '
                             '(certain characters need to be inside quotes, '
                             '\' \', \'*\', \'`\')',
                        default='')
    parser.add_argument('-w', action='store', dest='num_words',
                        help='Total words used to generate passwords '
                             '({} - {})'.format(MIN_WORDS, MAX_WORDS),
                        default=0, type=int)
    parser.add_argument('-p', action='store', dest='num_pwds',
                        help='Total passwords to generate '
                             '({} - {}) (default = 1)'
                        .format(MIN_PWDS, MAX_PWDS),
                        default=MIN_PWDS, type=int)
    parser.add_argument('-s', action='store_true', dest='write_shuffled',
                        help='Overwrite given word list after randomly '
                             'shuffling the words', default=False)

    args = parser.parse_args()  # command line arguments
    try:
        # try to load custom word list from command line argument
        # loads default word list if that fails (empty or doesn't exist)
        # example: python randpass.py -c wordlist2.txt
        WORD_LIST = load_word_list(args.word_list)
        FILENAME = args.word_list
    except (IndexError, IOError):
        WORD_LIST = load_word_list(FILENAME)

    if args.break_char:
        BREAK_CHARS = args.break_char

    num_words = args.num_words
    while True:
        try:
            if word_range(num_words):
                break
            num_words = int(raw_input('Enter # of words ({} - {}): '
                                      .format(MIN_WORDS, MAX_WORDS)))
        except ValueError:
            pass

    num_pwds = args.num_pwds if pwd_range(args.num_pwds) else MIN_PWDS
    for _ in range(num_pwds):
        print(generate_password(num_words))

    if args.write_shuffled:
        write_shuffled_word_list(FILENAME)
