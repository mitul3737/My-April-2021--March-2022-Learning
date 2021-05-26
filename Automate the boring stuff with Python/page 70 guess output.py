def spam():
    print(eggs)  # ERROR!    # here python thinks that this eggs is actually the local 'eggs'
    # that was on line 3 and thus gives erroring thinking that we want
    # output before assigning it .
    # python does not consider the global eggs value within the spam() function in this case

    eggs = 'spam local'  # local variable


eggs = 'global'  # global variable
spam()