print('Welcome to SPX Navigation Splitter v7.0')
print('This program was written to split the raw navigation SPX file')
print('containing a line with all nav strings in one, into individual fix nav')
print('strings using a 000PA000.spx file and saving as 000000_SPX.txt files')
spx_file = input('Enter the full address of the lines SPX file, including filename --> ')
spx_open = open(spx_file)
shotslist = list(spx_open)
user_firstfix = input('Enter the first fix number (including SOL noise file if created) --> ')
user_lastfix = input('Enter the last fix number (including EOL noise file if created)  --> ')
r1 = int(user_firstfix)
r2 = int(user_lastfix) + 1
print('Creating SPX files for fixes ' + str(r1).zfill(6) + ' to ' + str(r2 - 1).zfill(6))

a = 0
b = 1
f = int(user_firstfix)

for x in range(r1,r2):
    first = shotslist[a]
    second = shotslist[b]
    fix_filenum = '%s_SPX.txt' % str(f).zfill(6)
    fix = open(fix_filenum, 'w')
    fix.write(first + '\n' + second + '\n')
    a = a + 2
    b = b + 2
    f = f+1

print('Process complete')

__author__ = 'colinmacrae'