__author__ = 'colinmacrae'

spx_file = open(r'/Users/colinmacrae/Documents/Programming/untitled_tests_py3/navtest/032PA025.spx')
shotlist = list(spx_file)

first = shotlist[0]
first2 = tuple(first)

print(first, file='101.spx')