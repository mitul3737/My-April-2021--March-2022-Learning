#Creating code to run fromo command line or clipboard

import webbrowser,sys,pyperclip
if len(sys.argv)>1: #The sys.argv variable stores a list of the program's filename and command line arguments. If this list has more than just the
                    #just the filename in it, then len(sys.argv) evaluats to an integer greater than 1"""
    address=' '.join(sys.argv[1:]) # if we give command " <filename.py> Tongi Bazar " in command line, then sys.argv will be ['<filename.py>','Tongi','Bazar'] and it will cut the first file name and send it to address by doing
                                  # address=' '.join(sys.argv[1:]) and thus cutting first element and address will get a string 'Tongi Bazar'
else:
    address=pyperclip.paste()     # if user does not gve any command then we will check for clipboard and we will use pyperclip.paste() to get the clipboard value


webbrowser.open('https://www.google.com/maps/place/'+address) # code to run the browser
