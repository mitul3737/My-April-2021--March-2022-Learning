import os,bs4,requests
url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True) #os.makedirs creates a a folder named xkcd and exists_ok=True ensures no error if found any folder previously create named 'xkcd'
while not url.endswith('#'): #actually we will be looping till https://xkcd.com/#url as this link is of the home page . For example: go to inspect of that website and check the prev links href which changes if you press it again taking back to https://xkcd.com/#url at the end
           print('Download page %s...'%url)  #Showing people whch link is being downloaded
           res=requests.get(url) #download the url using requests
           res.raise_for_status() # checking if error happens
           soup=bs4.BeautifulSoup(res.text,'html.parser') #creating a BeautifulSoup Object from the text of the downloaded page


           comicElem=soup.select('#comic img')  # we can see that the images are within <div id =comic> <img src="".......> this kind of things and so we have given "#comic" to mean the id and the again the "img" attribute to et into the src to download the images
           if comicElem==[]: #if in the links, they don't get any thing ,then it will return a blank space and thus we will show an error message and repeat the process
               print('Could not find comic image')
           else:
               comicUrl='https:'+comicElem[0].get['src'] # as comicElem will get a value and it will add those to a list named comicElem and thus we are getting the src value of 1st element from comicElem[0].get('src') as we know attributes are there in html like <img src="https://..........> and thus we will eventually get the image url link
               print('Downloading image %s...'%(comicUrl)) #we will tell people which page we are downloading
               res=requests.get(comicUrl) #downloading the image
               res.raise_for_status()

               imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')  #now we will write the image file data to a file on the hard drive
                                                                                     #comicUrl will have links like 'https://imgs.xkcd.com/comics/mitul.jpg" and by using os.path.basename(comicUrl), we can get 'Mitul.jpg" and thus we will create a image file naming this to differentiate each
                                                                                     #now we will add each files to the folder named 'xkcd' and using os.path.join() and it will add \ for windows and / for linux and mac
               for chunk in res.iter_content(100000):        #the code in the for loop over writes out chunk of the image ata (at most 100000 bytes each) to the file and then you close the file . the image is now saved to the hard drive
                    imageFile.write(chunk)
               imageFile.close()

           # Getting the Prev buttons link
           prevLink=soup.select('a[rel="prev"]')[0]
           url='https://xkcd.com'+prevLink.get('href')

