print('@ ------ The Amazing Name List ------ @')
fname = ['Michael','Beth','George']
lname = ['Morris','Bushen','Lucas']
print()
print('Pick a number between 1 and ' + str(len(fname)))
userselect = int(input())
userselect = userselect - 1
print(fname[userselect] + ' ' + lname[userselect])
print('@ ------------- THE END ------------- @')