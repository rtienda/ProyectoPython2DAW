from selenium import webdriver
import json

browser = webdriver.PhantomJS()
browser.maximize_window()
browser.get("http://gundam.wikia.com/wiki/Master_Grade#Lineup")

kits = []
dictionary = {}

for year_release in range(1995, 2022):   
    browser.find_elements_by_link_text(str(year_release))[0].click()
    print ("currently at year ", str(year_release))
    table = browser.find_element_by_css_selector(".tabbertab:not(.tabbertabhide) > .wikitable")
    tds = table.find_elements_by_css_selector("tr > td")
    
    for i in range(len(tds)):
        if(i % 6 == 0):
            try:
                image = tds[i].find_elements_by_css_selector('div > a')[0].get_attribute('href')
            except IndexError:
                image = "No image available"
            dictionary['image'] = image
    
        elif(i % 6 == 1):         
            title = tds[i].text
            link = tds[i].find_element_by_tag_name('a').get_attribute("href")
            print ("title: " + title)
            print ("link: " + link)
            dictionary['title'] = title
            dictionary['link'] = link
            
        elif(i % 6 == 2):   
            series = tds[i].find_element_by_css_selector('a').get_attribute("title")
            dictionary['series'] = series
            
        elif(i % 6 == 3):
            price = tds[i].text
            dictionary['price'] = price
            
        elif(i % 6 == 4):
            release_date = tds[i].text
            dictionary['release_date'] = release_date
            kits.append(dictionary)
            dictionary = {}
print ("==================================")    
browser.close()
print (kits)

for index, kit in enumerate(kits):
    page_to_visit = kit['link']
    print ("connecting to ", page_to_visit)
    minibrowser = webdriver.PhantomJS()
    minibrowser.get(page_to_visit)
    print ("model name: ", kit['title'])
    info_text =  minibrowser.find_elements_by_css_selector("div.mw-content-text > p")[0].text
    print ("info_text: ", info_text)
    kit['info_text'] = info_text
    print (len(kits)-index-1, " remaining...")
    minibrowser.close()

with open('result.json', 'w') as fp:
    json.dump(kits, fp)

print ("program finished successfully")