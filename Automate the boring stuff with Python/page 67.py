
def spam():
    eggs = 99 #eggs=99
    bacon()  #goes to bacon() and there eggs=0
    print(eggs)  # comes to spam() and here the previous eggs=0 will not work as that is not this functions property. here eggs=99 will work

def bacon():
    ham = 101
    eggs = 0

spam()