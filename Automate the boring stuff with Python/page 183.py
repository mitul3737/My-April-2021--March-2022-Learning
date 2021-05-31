#!python3
# phoneAndEmail.py

import pyperclip, re

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-||.)
    (\d{4})
    (\s*(ex|x|ext.)\s*(\d{2,5}))?
''', re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9.%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4}))
''', re.VERBOSE)

# Finding matches in clipbopard
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

    # copy result to the key board
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


