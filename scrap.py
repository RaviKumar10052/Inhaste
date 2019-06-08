from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import shutil
from main import *
import requests
from collage import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def scrapping_public(username):
    browser = webdriver.Chrome(executable_path='E:\chromedriver.exe')
    browser.get('https://www.instagram.com/' + username + '/?hl=en')
    Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    links = []
    source = browser.page_source
    data = bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com' + link.get('href'))
    # sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
    time.sleep(5)
    Pagelength = browser.execute_script(
        "window.scrollTo(document.body.scrollHeight/1.5, document.body.scrollHeight/3.0);")
    source = browser.page_source
    data = bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com' + link.get('href'))
    #print(links)
    create_dir(username)
    folder = "inhaste/" + username
    downloader(links, username)
    collagein(folder, username)

def downloading_images(all_images,username):
    print(len(all_images))

    for index, image in enumerate(all_images):
        filename = "image_" + str(index+1) + ".jpg"
        image_path = os.path.join("inHaste/"+username, filename)
        #print(image['src'])
        #link = str(image['src'])
        print("Downloading image ", index+1)

        response = requests.get(image['src'], stream=True)
        try:
            with open(image_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        except Exception as e:
            print(e)
            print('Could not download image no.', index+1)

def scrapping_private(username,password):
    driver = webdriver.Chrome(executable_path='E:\chromedriver.exe')
    driver.get('https://www.instagram.com/')
    def log_in(username, password):
        try:
            log_in_button = driver.find_element_by_xpath('//p[@class="izU2O"]/a')
            log_in_button.click()
            time.sleep(3)
            user_name_input = driver.find_element_by_xpath('//input[@aria-label="Phone number, username, or email"]')
            user_name_input.send_keys(username)
            password_input = driver.find_element_by_xpath('//input[@aria-label="Password"]')
            password_input.send_keys(password)
            password_input.submit()
            time.sleep(3)
            Not_Now2 = driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
            Not_Now2.click()
            time.sleep(3)
            log_in_button = driver.find_element_by_xpath('//div[@class="XrOey"][last()]/a')
            log_in_button.click()
            time.sleep(3)
        except Exception as e:
            error = True
            print(e)
    log_in(username,password)
    Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    links = []
    source = driver.page_source
    data = bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com' + link.get('href'))
    # sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
    time.sleep(5)
    Pagelength = driver.execute_script(
        "window.scrollTo(document.body.scrollHeight/1.5, document.body.scrollHeight/3.0);")
    source = driver.page_source
    data = bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com' + link.get('href'))
    #print(links)
    create_dir(username)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    images = soup.findAll('img')

    all_images = images
    last_height = driver.execute_script("return document.body.scrollHeight")
    for win in range(9):
        #print(win)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        images = soup.findAll('img')
        all_images.extend(images[-12:])
        last_height = new_height
    downloading_images(all_images, username)
    folder = "inhaste/" + username
    collagein(folder, username)

def create_project():
    path = "inHaste"
    try:
        os.mkdir(path)
    except OSError:
        print("directory %s is present \n" % path)
    else:
        print("Successfully created the directory %s " % path)

def create_dir(name):
    create_project()
    path = "inHaste/"+name
    try:
        os.mkdir(path)
    except OSError:
        print("directory %s is present \n" % path)
    else:
        print("Successfully created the directory %s " % path)

def downloader(photo_url,username):
    i = 1
    for url in photo_url:
        inhaste_public(username,url,i)
        i=i+1