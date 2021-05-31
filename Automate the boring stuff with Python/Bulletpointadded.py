#! python 3
#bullentpointadded.py     - Adds Wikipedia bullet points to the start of each line of text pn the clipboard

import pyperclip
text=pyperclip.paste() # returns all the text on the clipboard as one big string

#Separating lines and adding stars
lines=text.split('\n')      #spliting texts on basis of \n
for i in range(len(lines)): #Loops through alll indexes of "lines" list
    lines[i]='* '+lines[i] #(Main part) #adding start to each string in "lines" list
text= '\n'.join(lines)      #pyperclip.copy() is expecting a single string value and thus using join() method to get a single string
pyperclip.copy(text)