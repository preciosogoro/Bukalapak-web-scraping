import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# c-product-card__name

Homepage = Function("https://www.bukalapak.com/u/dnblawbookstore")   
Homepage.getLink()

Done = False
while not Done:
    try: 
        href = driver.find_element(by=By.CLASS_NAME, value="c-product-card__name")
        href.click()
        driver.back()

        
    except:
        pass

    # except:
    #     print('There is no website!')
    #     # break


# while True:





# Done = False
# while not Done:
#     try:
   
#         bookTitle = driver.find_element(by=By.CLASS_NAME, value="c-main-product__title")
#         print(bookTitle.text)

#         bookPrice = driver.find_element(by=By.CLASS_NAME, value="c-product-price")
#         print("HARGA BUKU : " + bookPrice.text)

#         bookCondition = driver.find_element(by=By.CLASS_NAME, value="c-label")
#         print("KONDISI BUKU : " + bookCondition.text)

#         bookDescription = driver.find_element(by=By.CLASS_NAME, value="c-information__description-txt")
#         print(bookDescription.text)
        
#         Done = True
#         if Done == True:
#             driver.back()
#     except:
#         print("There is no element to be found")














# x = driver.find_elements(by=By.CLASS_NAME, value="{Link}")
# for i in x:
#   print(i.text)