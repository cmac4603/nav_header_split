__author__ = 'colinmacrae'

import os

spx_file = open('/Users/colinmacrae/Documents/Programming/untitled_tests_py3/navtest/032PA025.spx')
shotlist = list(spx_file)

fullshot = iter(shotlist)
map(str.__add__, fullshot, fullshot)
print(list(fullshot))