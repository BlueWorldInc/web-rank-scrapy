from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://battledev.blogdumoderateur.com/?utm_source=email&utm_campaign=22h00__fin_de_la_BattleDev&utm_medium=email')

NUMBER_PARTICIPANT = 4000
PARTICIPANT_PER_PAGE = 25
TOTAL_PAGE = NUMBER_PARTICIPANT // PARTICIPANT_PER_PAGE

cookieChoice = browser.find_element_by_id('cookieChoiceDismiss')
cookieChoice.click()
timeout = 60

pageNum = 1

def save_to_file(pageNum, content):
    fileToSave = open('./pages/battle_dev'+str(pageNum)+'.html', 'w', encoding='utf-8')
    fileToSave.write(content)

def wait_for_data_load(driver):
    # print("Page ready: ", driver.execute_script("return jQuery.active == 0"))
    return driver.execute_script("return jQuery.active == 0")

for i in range(TOTAL_PAGE):
    print("Page actuel:", pageNum, " percentage: ", str(pageNum / TOTAL_PAGE * 100), "%")
    content = browser.page_source
    save_to_file(pageNum, content)
    pageNum += 1
    WebDriverWait(browser, timeout).until(wait_for_data_load)
    linkElems = browser.find_elements_by_class_name('page-link')
    for e in linkElems:
        if (int(e.get_attribute('data-page-num')) == pageNum):
            e.click()
            break

