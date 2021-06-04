import requests,sys,bs4,webbrowser
print('Searching...') #  Display text while search result page
res=requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=',' '.join(sys.argv[1:]))
res.raise_for_status()


soup=bs4.BeautifulSoup(res.text,'html.parser') #Retrieve the top search result links
linkElems=soup.select('.package-snippet')      #Open a browser tab for each result



numOpen=min(5,len(linkElems))

for i in range(numOpen):
    urlToOpen='https://pypi.org'+linkElems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)

