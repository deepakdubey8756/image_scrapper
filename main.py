#importing required modules
import os
import requests
from bs4 import BeautifulSoup
import json


#folder in which image will be saved
SAVE_FOLDER = "images/"

# Link to scrape my images
GOOGLE_IMAGES = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


#header container
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

#our main function
def main():
    #this will create image folder if not exists
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()




def download_images():
    """function to scrape and download images.."""

    data = input("What are you looking for? ")
    n_image = int(input("How many images you want? :  "))

 
    print("Start Searching... ")


    # Search url that will be used as a data
    searchUrl = GOOGLE_IMAGES + 'q='+ data

    # scraping page
    response = requests.get(searchUrl, headers=usr_agent)

    #scraping html content
    html = response.text


    soup = BeautifulSoup(html, 'html.parser')

    #parsing image source
    requiredContainer = soup.find_all("img", limit=n_image+2)

    # extracting and saving every url from parsed container
    image_url = []
    i = False

    for container in requiredContainer:
        if i == True:
            image_url.append(container['src'])
        
        else:
            i = True


    j = 1
    for image_link in image_url:
        req = requests.get(image_link)
        file_name = SAVE_FOLDER + data + str(j) + '.jpeg'
        with open(file_name, 'wb') as f:
            f.write(req.content)
        j += 1

    print("Done....")
    
if __name__ == "__main__":
    main()