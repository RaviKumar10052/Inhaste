import requests
import re
from bs4 import BeautifulSoup
import os

def requests_start_url(start_url):
    try:
        response = requests.get(start_url)
        html = response.text
        #print(html)
        return html
    except Exception:
        print('Opps! Occurred error')
        return None
def find_photo_url(requests_url):
    soup = BeautifulSoup(requests_url,  "html.parser")
    photo_url = soup.find("meta", property="og:image")
    #print(photo_url)
    #print(photo_url['content'])
    return photo_url["content"]


def downloader(photo_url,username,value):
    requests_url = requests.get(photo_url)
    val=str(value)
    f = open(os.path.join('inHaste/'+username, val+'.jpg'), 'wb')
    f.write(requests_url.content)
    print('Downloading image'+val)
    f.close()


def find_img_url(request_url):
    img_url=re.findall(r"display_url\":\"([^\"]*)" ,request_url)
    #print(img_url)
    return img_url

def img_downloader(photo_url,username,value):
    i = value
    var = 'Pic' + str(i)
    i = i + 1
    print('Photo name is: ' + var)
    requests_url = requests.get(photo_url)
    f = open(os.path.join('inHaste/' + username, var + '.jpg'), 'wb')
    f.write(requests_url.content)
    print('Downloading image'+str(i))
    f.close()
    print('Download complete')

def inhaste_public(username,photo_url,value):

    requests_url = requests_start_url(photo_url)
    photo_url = find_photo_url(requests_url)
    downloader(photo_url, username,value)