__author__ = 'colinmacrae'

import os

spx_file = open('/Users/colinmacrae/Documents/Programming/untitled_tests_py3/navtest/032PA025.spx')

for shots in spx_file:
    eachshot = shots.split('$')

for i,shot in eachshot:
    s = open(str(i+100)+'.spx','w')
    s.write('$'+shot)