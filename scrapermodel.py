import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Chrome()

class Function:
    def __init__(self, link):
        self.link = link

    def getLink(self):
        # driver.implicitly_wait(3)
        driver.get(f"{self.link}")
        time.sleep(2)

    def clickLink(self):
        href = driver.find_element(by=By.CLASS_NAME, value=f"{self.link}")
        href.click()

    def clickLinks(self):
        href = driver.find_elements(by=By.CLASS_NAME, value=f"{self.link}")
        for hypertext in href:
            hypertext.click()
            time.sleep(2)

    def findElement(self, classname):
        self.classname = classname
        driver.find_element(by=By.CLASS_NAME, value=f"{self.classname}")


template = '''
{
    "DATA" : [
        {
            "BOOK-ID" : "1",
            "BOOK-INFO" : [
            {
                "TITLE" : "MAATSCHAP FIRMA Dan PERSEKUTUAN KOMANDITER",
                "PRICE" : "Rp154.900",
                "STOCKS" : "",
                "CONDITION" : "BEKAS",
                "IMAGE" : ["", "", ""],
                "DESCRIPTION" : [""]
            }
        ]
        }
    ]
}

'''

data = json.loads(template)




Homepage = Function("https://www.bukalapak.com/u/dnblawbookstore")   
Homepage.getLink()
driver.implicitly_wait(10)

Done = False
while not Done:
    try:
        loopTime = 0
        for loopTime in range(64):
            driver.implicitly_wait(10)           
            itemLocation = driver.find_element(by=By.CSS_SELECTOR, value='div[class="o-layout o-layout--responsive"]')
            driver.implicitly_wait(2)
            href = itemLocation.find_elements(by=By.CLASS_NAME, value="c-product-card__name")
            for url in href:
                driver.implicitly_wait(2)
                url.click()
                try:
                    bookTitle = driver.find_element(by=By.CLASS_NAME, value="c-main-product__title")
                    print(bookTitle.text)

                    bookPrice = driver.find_element(by=By.CLASS_NAME, value="c-product-price")
                    print("HARGA BUKU : " + bookPrice.text)

                    bookCondition = driver.find_element(by=By.CLASS_NAME, value="c-label")
                    print("KONDISI BUKU : " + bookCondition.text)

                    bookDescription = driver.find_elements(by=By.XPATH, value='//div[@class="c-information__description-txt"]')
                    for description in bookDescription:
                        print("Exp : " + description.text)
                except:
                    print("Book scraping error")                      
                finally:
                    print("SUCCESFULL!!")
                    driver.implicitly_wait(2)
                    driver.back()
        if driver == driver.quit():
            break
    except:
        print("Going to next page!")

    else:
        print("While loop going correctly")
    finally:
        nextPage = driver.find_element(by=By.XPATH, value='//span[@class="c-ghostblock-pagination__next"]')
        nextPage.click()
        driver.implicitly_wait(10)
        continue


