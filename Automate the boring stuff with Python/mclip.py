import pyperclip
#! python3
#mclip.py - A multi-clipboard program.

TEXT={'agree':"""Yes, I agree. That sounds fine to me.""",
      'busy':"""Sorry, can we o this later this week or next week""",
      'upsell':"""Would you consider making this a monthly donation?"""
      }

import sys
if len(sys.argv)<2:
    print('Usage: python mclip.py [keyphrase]- copy phrase text')
    sys.exit()
keyphrase=sys.argv[1] #first command line arg s the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ',keyphrase,' copied to clipboard ')
else:
     print('There is no text for ', keyphrase)