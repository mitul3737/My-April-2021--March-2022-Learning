catNames = [] #List having 0 values
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':  #if we don't give any value it will break
        break
    catNames = catNames + [name]  # list concatenation   #adding the inputs to the list
print('The cat names are:')
for name in catNames:       #running the loop
    print('  ' + name)