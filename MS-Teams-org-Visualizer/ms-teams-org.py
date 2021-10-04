#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC




options = webdriver.ChromeOptions()
driver = webdriver.Edge(executable_path = r'C:\Users\RVSB\cloud-utils\edgedriver_win64\msedgedriver.exe')


start_point = 'https://teams.microsoft.com'
driver.get(start_point)



# class Person(object):
#     def __init__(self, handle, name, description, children=None):
#         self.handle = handle
#         self.name = name
#         self.description = description
#         self.children = children
        
    




root = 'Your CEO/TOP level person name on TEAMS'

centric = 'your handle'

# queue = [root]




### init search 
search_bar = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "control-input")))
toast = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="toastbody toast-actions"]'))).click()
import time
time.sleep(5)







def get_org(handle):
    
    global  driver
    
    
    search_bar = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "control-input")))
    try:
        search_bar.click()
    except:
        pass
    

    ActionChains(driver).send_keys(handle.split('~')[0]).perform()

    while not 'Press enter to view all results' in driver.page_source:
        pass
    
    search_bar.send_keys(Keys.ENTER)
    ul_bar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "search-result-tabs")))
    ul_bar.find_elements_by_tag_name('span')[1].click()  #people
    
    if "We didn't find any matches." in driver.find_element(By.CSS_SELECTOR, 'div[class="show-rail active-search app-full-viewport-height left-rail-box-shadow-overlay"]').text:
        search_bar.clear()
        return []

    try:
        people = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'peopleSearchContent-0')))
    except:
        search_bar.clear()
        return []

    
    node = people.find_element_by_class_name('hover-div') #first-person
    
    person = node.text.replace('\n', '~')
    
    node.click()
    
    people_org =  WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID,  "messages-header-v2-tab-group")))
    hidden_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-default overflow-tab-button"]')))
    hidden_button.click()
    
    hidden_args = driver.find_elements(By.CSS_SELECTOR, 'ul[class="app-default-menu-ul"]')
    org  = hidden_args[0].find_elements_by_tag_name('li')[1]  #org
    org.click()
    
    org_container = WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.ID, 'orgdata-container')))
    
    reporters = org_container.find_element(By.CSS_SELECTOR, 'div[class="reportscontainer"]')
    

    colleagues = []
    for person in reporters.find_elements_by_css_selector("div[role='contentinfo']"):
            #print(parse_person(person.text))
        colleagues.append(person.text.replace('\n', '~'))
        
    search_bar.clear()    
    
    
    if handle in colleagues:
        return []    
    
    
    return colleagues




def build_org(search_handle):
    
    
    if 'consultant' in search_handle.lower() or 'analyst' in search_handle.lower() or 'specialist' in search_handle.lower():
        
        return {
                    "name": search_handle,
                    "size": 10
                }   
    
    colleagues = get_org(search_handle)              # 
    
    
    if len(colleagues) == 0 :
        
        return {
                    "name": search_handle,
                    "size": 10
                }   
    

    else:
              
        empty_db = { "name" : search_handle,
                     "children" : []
                   }    
        
        
        for colleague in colleagues:
            
            if '~' not in colleague or '(' not in colleague:  # only humans
                continue
                
            sub_org = build_org(colleague)
            
            empty_db['children'].append(sub_org)
        
        
        return empty_db





tree = build_org(root)  #.copy since attributes are removed in recursions



import json
json.dump(tree, open('flare.json', 'w'))



