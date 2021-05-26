def spam():
    global eggs #declared eggs as global variable
    eggs = 'spam'  # this is the global


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(eggs)  # this is the global  #here it will see eggs and looks for local variable and as thereis no local variable here, it will look for global varibale which is in the spam() and it's alue is 'spam'


eggs = 42  # this is the global
spam()  #goes to spam() and returns
print(eggs) # looks fr global eggs value and gets it from spam() as it was declared as global