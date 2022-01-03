from datetime import datetime
import time
from webdriver_manager.firefox import GeckoDriverManager

import json
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import os
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def job0():
    for i in range(22, 27):
        tag = buttons[i]
        desired_y = (tag.size['height'] / 2) + tag.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        # driver.execute_script("arguments[0].scrollIntoView();", tag)
        time.sleep(3)
        tag.click()
        c = buttons[i].find_elements_by_xpath("//button[@class='euiContextMenuItem']")
        time.sleep(3)
        c[1].click()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        downloads = driver.find_element_by_xpath("//button[@class='euiButton euiButton--primary euiButton--small']")
        downloads.click()
        time.sleep(3)
        csv = downloads.find_element_by_xpath("//button[@class='euiContextMenuItem']")
        csv.click()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)

        f = glob.glob(path + "*.csv")
        for file in f:
            shutil.move(file, path + '/')
        time.sleep(2)


def job(value, inp):
    inp.send_keys(value)
    time.sleep(1)
    inp.send_keys(Keys.DOWN)
    time.sleep(1)
    inp.send_keys(Keys.RETURN)
    time.sleep(2)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)
    apply = driver.find_element_by_xpath("//button[@data-test-subj='inputControlSubmitBtn']")
    time.sleep(3)
    apply.click()
    time.sleep(3)
    for i in range(22, 27):
        tag = buttons[i]
        desired_y = (tag.size['height'] / 2) + tag.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        # driver.execute_script("arguments[0].scrollIntoView();", tag)
        time.sleep(3)
        tag.click()
        c = buttons[i].find_elements_by_xpath("//button[@class='euiContextMenuItem']")
        time.sleep(3)
        c[1].click()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        downloads = driver.find_element_by_xpath("//button[@class='euiButton euiButton--primary euiButton--small']")
        downloads.click()
        time.sleep(3)
        csv = downloads.find_element_by_xpath("//button[@class='euiContextMenuItem']")
        csv.click()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)


def job0():


    time.sleep(3)
    for i in range(22, 27):
        tag = buttons[i]
        desired_y = (tag.size['height'] / 2) + tag.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        # driver.execute_script("arguments[0].scrollIntoView();", tag)
        time.sleep(3)
        tag.click()
        c = buttons[i].find_elements_by_xpath("//button[@class='euiContextMenuItem']")
        time.sleep(3)
        c[1].click()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        downloads = driver.find_element_by_xpath("//button[@class='euiButton euiButton--primary euiButton--small']")
        downloads.click()
        time.sleep(3)
        csv = downloads.find_element_by_xpath("//button[@class='euiContextMenuItem']")
        csv.click()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element = driver.find_element_by_tag_name("body")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)


today = datetime.now()
file_path="/home/souid/Desktop/inkyfada_evax/" + today.strftime('%Y' + '-' + '%m' + '-' + '%d')
import  os, shutil



if os.path.exists(file_path):
    # removing the file using the os.remove() method
    files_in_dir = os.listdir(file_path)  # get list of files in the directory

    #for file in files_in_dir:  # loop to delete each file in folder
     #   os.remove(f'{file_path}/{file}')  # delete file

    #os.rmdir(file_path)
    shutil.rmtree(file_path, ignore_errors=False)
    print("exist")
    os.mkdir(file_path)
    print('mkdir')
else:
    os.mkdir(file_path)


path = "/home/souid/Desktop/inkyfada_evax/" + today.strftime('%Y' + '-' + '%m' + '-' + '%d') + '/'
dic = {'Ariana': ['ARIANA MEDINA',
                  'ETTADHAMEN',
                  'KALAAT LANDLOUS',
                  'MNIHLA',
                  'RAOUED',
                  'SIDI THABET',
                  'LA SOUKRA'],
       'Béja': ['AMDOUN',
                'BEJA NORD',
                'BEJA SUD',
                'GOUBELLAT',
                'MEJEZ EL BAB',
                'NEFZA',
                'TEBOURSOUK',
                'TESTOUR',
                'THIBAR'],
       'Ben Arous': ['BEN AROUS',
                     'BOU MHEL',
                     'EL MOUROUJ',
                     'EZZAHRA',
                     'FOUCHANA',
                     'HAMMAM CHATT',
                     'HAMMAM LIF',
                     "MOHAMADIA",
                     'NOUVELLE MEDINA',
                     'MEGRINE',
                     'MORNAG',
                     'RADES'],
       'Bizerte': ['BIZERTE NORD',
                   'BIZERTE SUD',
                   'JOUMINE',
                   'EL ALIA',
                   'GHAR EL MELH',
                   'GHEZALA',
                   'MATEUR',
                   'MENZEL BOURGUIBA',
                   'MENZEL JEMIL',
                   'RAS JEBEL',
                   'SEJNANE',
                   'TINJA',
                   'UTIQUE',
                   'ZARZOUNA'],
       'Gabès': ['GABES MEDINA',
                 'GABES OUEST',
                 'GABES SUD',
                 'GHANNOUCHE',
                 'EL HAMMA',
                 'MARETH',
                 'MATMATA',
                 'NOUVELLE MATMATA',
                 'MENZEL HABIB',
                 'METOUIA'],
       'Jendouba': ['AIN DRAHAM',
                    'BALTET BOU AOUENE',
                    'BOU SALEM',
                    'FERNANA',
                    'GHARDIMAOU',
                    'JENDOUBA',
                    'JENDOUBA NORD',
                    'OUED MLIZ',
                    'TABARKA'],
       'Gafsa': ['BELKHIR',
                 'MOULARES',
                 'ZANNOUCH',
                 'GAFSA NORD',
                 'GAFSA SUD',
                 'EL GUETTAR',
                 'EL KSAR',
                 'EL MDHILLA',
                 'METLAOUI',
                 'REDEYEF',
                 'SNED',
                 'SIDI BOUBAKER',
                 'SIDI AICH'],
       'Kairouan': ['EL ALA',
                    'Aïn Jloula',

                    "Menzel M'Hiri",
                    'BOU HAJLA',
                    'CHEBIKA',
                    'CHERARDA',
                    'HAFOUZ',
                    'HAJEB EL AYOUN',
                    'KAIROUAN NORD',
                    'KAIROUAN SUD',
                    'NASRALLAH',
                    'OUESLATIA',
                    'SBIKHA'],
       'Kasserine': ['EL AYOUN',
                     'EZZOUHOUR',
                     'FERIANA',
                     'FOUSSANA',
                     'HASSI EL FRID',
                     'HAIDRA',
                     'JEDILIANE',
                     'KASSERINE NORD',
                     'KASSERINE SUD',
                     'MEJEL BEL ABBES',
                     'SBEITLA',
                     'SBIBA',
                     'THALA'],
       'Kebili': ['DOUZ NORD',
                  'DOUZ SUD',
                  'EL FAOUAR',
                  'KEBILLI NORD',
                  'KEBILLI SUD',
                  'SOUK EL AHAD',
                  'RJIM MAATOUG',
                  ],
       'Le Kef': ['DAHMANI',
                  'LE SERS',
                  'JERISSA',
                  'KALAA EL KHASBA',
                  'KALAAT SINANE',
                  'LE KEF EST',
                  'LE KEF OUEST',
                  'EL KSOUR',
                  'NEBEUR',
                  'SAKIET SIDI YOUSSEF',
                  'TAJEROUINE',
                  'TOUIREF'],
       'Mahdia': ['BOU MERDES',
                  'LA CHEBBA',
                  'CHORBANE',
                  'EL JEM',
                  'HBIRA',
                  'KSOUR ESSAF',
                  'MAHDIA',
                  'MELLOULECH',
                  'OULED CHAMAKH',
                  'SIDI ALOUENE',
                  'SOUASSI'],
       'Mannouba': ['BORJ EL AMRI',
                    'DOUAR HICHER',
                    'EL BATTAN',
                    'JEDAIDA',
                    'LA MANNOUBA',
                    'MORNAGUIA',
                    'OUED ELLIL',
                    'TEBOURBA'],
       'Médenine': ['MEDENINE NORD',
                    'MEDENINE SUD',
                    'SIDI MAKHLOUF',
                    'ZARZIS',
                    'BEN GUERDANE', 'BENI KHEDACHE'],
       'Médenine-Djerba': [
           'DJERBA AJIM',
           'DJERBA MIDOUN',
           'DJERBA HOUMT ESSOUK',
       ],
       'Monastir': ['BEKALTA',
                    'BEMBLA',
                    'BENI HASSEN',
                    'JEMMAL',
                    'KSAR HELAL',
                    'KSIBET EL MEDIOUNI',
                    'MOKNINE',
                    'MONASTIR',
                    'OUERDANINE',
                    'SAHLINE',
                    'SAYADA-LAMTA-BOU-HJAR',
                    'TEBOULBA',
                    'ZERAMDINE'],
       'Nabeul': ['BENI KHALLED',
                  'BENI KHIAR',
                  'BOU ARGOUB',
                  'DAR CHAABANE ELFEHRI',
                  'EL MIDA',
                  'GROMBALIA',
                  'HAMMAM EL GHEZAZ',
                  'HAMMAMET',
                  'EL HAOUARIA',
                  'KLIBIA',
                  'KORBA',
                  'MENZEL BOUZELFA',
                  'MENZEL TEMIME',
                  'NABEUL',
                  'SOLIMAN',
                  'TAKELSA'],
       'Sfax': ['AGAREB',
                'BIR ALI BEN KHELIFA',
                'EL AMRA',
                'GHRAIBA',
                'EL HENCHA',
                'ESSKHIRA'
                'JEBENIANA',
                'KERKENAH',
                'MAHRAS',
                'MENZEL CHAKER',
                'SAKIET EDDAIER',
                'SAKIET EZZIT',
                'SFAX EL MEDINA',
                'SFAX OUEST',
                'SFAX SUD',
                'SKHIRA',
                'TINA'],
       'Sidi Bouzid': ['BIR EL HAFFEY',
                       'JILMA',
                       'MAZZOUNA',
                       'MAKNASSY',
                       'MENZEL BOUZAINE',
                       'OULED HAFFOUZ',
                       'REGUEB',
                       'CEBALET OULED ASKER',
                       'SIDI ALI BEN AOUN',
                       'SIDI BOUZID EST',
                       'SIDI BOUZID OUEST',
                       'SOUK JEDID'],
       'Siliana': ['BARGOU',
                   'BOU ARADA',
                   'BOU ROUIS',
                   'LE KRIB',
                   'EL AROUSSA',
                   'GAAFOUR',
                   'KESRA',
                   'MAKTHAR',
                   'EL ROUHIA',
                   'SIDI BOUROUIS',
                   'SILIANA NORD',
                   'SILIANA'],
       'Sousse': ['AKOUDA',
                  'BOU FICHA',
                  'ENFIDHA',
                  'HAMMAM SOUSSE',
                  'HERGLA',
                  'KALAA EL KEBIRA',
                  'KALAA ESSGHIRA',
                  'KONDAR',
                  "M'SAKEN",
                  'SIDI BOU ALI',
                  'SIDI EL HENI',
                  'SOUSSE JAWHARA',
                  'SOUSSE MEDINA',
                  'SOUSSE RIADH',
                  'SOUSSE SIDI ABDELHAMID',
                  'ZAOUIT-KSIBET-THRAYET'],
       'Tataouine': ['BIR LAHMAR',
                     'DHIBA',
                     'GHOMRASSEN',
                     'REMADA',
                     'SMAR',
                     'TATAOUINE NORD',
                     'TATAOUINE SUD'],
       'Tozeur': ['DEGUECHE (DEGACHE)', 'HAZOUA', 'NEFTA', 'TAMAGHZA', 'TOZEUR'],
       'Tunis': ['BAB BHAR',
                 'BAB SOUIKA',
                 'BARDO',
                 'BOUHAIRA',
                 'CARTHAGE',
                 'EL KHADRA',
                 'EL MENZAH',
                 'EL OUARDIA',
                 'EL TAHRIR',
                 'EZZOUHOUR',
                 'HRAIRIA',
                 'JEBEL JELLOUD',
                 'KABARIA',
                 'LA GOULETTE',
                 'LA MARSA',
                 'LE KRAM',
                 'MEDINA',
                 'OMRANE',
                 'OMRANE SUPERIEUR',
                 'SIDI EL BECHIR',
                 'SIDI HASSINE',
                 'SIJOUMI'],
       'Zaghouan': ['BIR MCHERGUA',
                    'FAHS',
                    'NADHOUR',
                    'SAOUAF',
                    'ZAGHOUAN',
                    'ZRIBA']}

import os

for key, values in dic.items():
    os.mkdir(path + key)

gouvernorats = ['Ariana', 'Béja', 'Ben Arous', 'Bizerte', 'Gabès', 'Jendouba', 'Kairouan', 'Kasserine', 'Kebili',
                'Le Kef', 'Mahdia', 'Mennouba', 'Médenine', 'Médenine-Djerba', 'Monastir', 'Nabeul', 'Sfax',
                'Sidi Bouzid', 'Siliana', 'Sousse', 'Tataouine', 'Tozeur', 'Tunis', 'Zaghouan']
options = webdriver.ChromeOptions()
#options.add_argument("download.default_directory=C:/Users/inky/Desktop")
prefs = {}
prefs["profile.default_content_settings.popups"] = 0
prefs["download.default_directory"] =path
prefs["profile.default_content_setting_values.automatic_downloads"] = 1

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=r'/home/souid/Downloads/chromedriver_linux64/chromedriver',options=options)
# driver = webdriver.Chrome(options=options)
driver.maximize_window()
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.evax.tn/vaccinationOD.html")
time.sleep(60)
#driver.switch_to_default_content()
frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(frame)

buttons = driver.find_elements_by_xpath("//button[@data-test-subj='embeddablePanelToggleMenuIcon']")
for key, values in dic.items():
    inp0 = driver.find_elements_by_tag_name("input")[0]

    job(key, inp0)
    f = glob.glob(path + "*.csv")
    for file in f:
        shutil.move(file, path + key + '/')
    time.sleep(2)

    time.sleep(1)
    driver.find_elements_by_tag_name("input")[0]
    inp0.send_keys(u'\ue009' + u'\ue003')
    inp0.clear()
time.sleep(3)

job0()
driver.quit()