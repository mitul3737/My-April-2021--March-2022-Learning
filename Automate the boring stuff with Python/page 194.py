import pyinputplus as pyip
"""Creating a function that will take digits whose sum is not more than 10"""
def addsUptoTen(numbers):
    numbersList=list(numbers)
    for i,digit in enumerate(numbersList):
        numbersList[i]=int(digit)
    if sum(numbersList)!=10:
        raise Exception('The digits must add up to 10, not %s .'%(sum(numbersList)))
    return int(numbers)

"""Main part"""
response=pyip.inputCustom(addsUptoTen)
print(response)
