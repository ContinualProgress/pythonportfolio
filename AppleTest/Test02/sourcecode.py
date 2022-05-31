#!/usr/bin/python3

# 1) Write a script to calculate the frequency of each word in a text file file.txt.

# For simplicity sake, you may assume:

# file.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.
# Assume that file.txt has the following content:

#apple products are iphones macbooks
#macbooks are apple products
#iphones are iphones


# Your script should output the following, sorted by descending frequency:

#iphones 3
#are 3
#products 2
#macbooks 2
#apple 2

teststring ="apple products are iphones macbooks \
macbooks are apple products \
iphones are iphones"


from pprint import pprint
import operator

frequency = {}

words = teststring.split()
print(words)

for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1


#pprint(frequency)
pprint(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True) )


#2: Assume two unordered arrays of strings, expected, and actual:
expected = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
actual = ["zero", "two", "apple", "eight", "ten"]

#1) Determine which expected strings are not found in actual.
#2) Determine which actual strings were not (in) expected.

setExpected = set(expected)
setActual = set(actual)

print("No. 1: {}".format( setActual.difference(setExpected) ) )
print("No. 2: {}".format( setExpected.difference(setActual) ) )
