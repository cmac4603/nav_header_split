
spx_file = open('/Users/colinmacrae/Documents/Programming/untitled_tests_py3/nav_head_split_v6/032PA025.spx')
shotslist = list(spx_file)
a = 0
b = 1
f = 101

for x in range(101,931):
    first = shotslist[a]
    second = shotslist[b]
    fix_filenum = str('000%i_SPX.txt' % f)
    fix = open(fix_filenum, 'w')
    fix.write(first)
    fix.write('/n')
    fix.write(second)
    a = a + 2
    b = b + 2
    f = f+1

__author__ = 'colinmacrae'