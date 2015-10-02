__author__ = 'colinmacrae'

import os

spx_file = open('/Users/colinmacrae/Documents/Programming/untitled_tests_py3/navtest/032PA025.spx')

for shots in spx_file:
    eachshot = shots.split('$')

print(list(enumerate(eachshot, start=101)))