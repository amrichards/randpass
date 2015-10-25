# Quick word-based passwords from a file with added break characters
# By: Adam M Richards 
# Use: in conjunction with a wordlist, create random passwords including break characters in between words
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

import random

# Create Break Characters and output string
bc = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', '~', '<', '>', '?', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
pwd = ''
# Import word list into an array
def wordlist(file):
	w = []
	f = open(file, 'r')
	for line in f:
		w.append(line.rstrip())
	return w
# Use wordlist.txt to output to an array and request the word length
wo = wordlist('wordlist.txt')
y = input("\nSelect the password length: ")

# Loop through to add a word and a break character to pwd
while y > 0:
	pwd += random.choice(wo)
	pwd += random.choice(bc)
	y -= 1
#Print output
print "\nPlease keep in mind that capitalization should be added as user needs."
print "Password: " + pwd + "\n"