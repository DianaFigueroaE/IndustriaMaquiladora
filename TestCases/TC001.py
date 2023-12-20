from selenium import webdriver
from Locators.Locators import MyLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd1
from selenium.webdriver.common.action_chains import ActionChains
import unittest



class TC001():
    
    
    def __init__(self,driver):
        #defining the locators and driver
        self.driver = driver
        self.xpathProveedorsCard = MyLocators.xpathProveedorsOptionCard
        self.cssProveedorCard = MyLocators.cssProveedorCard
        self.xpathProveedoresCategoriesList = MyLocators.xpathProveedoresCategoriesList
        self.xpathProvidersList = MyLocators.xpathListProviders
        self.list_Columns = MyLocators.list_Columns
        self.save_screenshotRoot = MyLocators.save_screenshotRoot
        self.xpathCategoryName = MyLocators.xpath_CategoryName
        self.xpathProviderDetailsListName = MyLocators.xpathProviderDetailsListName
        
          
    def start(self):  
        #row counter for the dataset that will be writting the outputs
        global int_currentRow
        int_currentRow = 1
        #Row counter for providers iteration
        global i
        #Dataframe definition
        global dfi 
        dfi= pd1.DataFrame()
        #Counter for number of providers in output
        global outputnumberRecords 
        
        #Get to main URL
        self.driver.get(MyLocators.URL)
        time.sleep(3)
        
        #Go to providers card/option after verify the option is available
        try: 
            webwaitmsg = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    (By.XPATH,self.xpathProveedorsCard)))
            self.xpathProviderDetailsList = MyLocators.xpathProviderDetailsList 
        except TimeoutException  as toe:
            print("Error, the card/option Providers is not available right now", toe)  
            
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.xpathProveedorsCard).click()
    
        #Get the number of categories to iterate later on
        categoriesList = self.driver.find_elements(By.XPATH, self.xpathProveedoresCategoriesList)
        length_of_elements = len(categoriesList)
        print("There are this number of categories: ", length_of_elements)
        outputnumberRecords=1
        #Iteration on categories
        for i in range(length_of_elements):
            time.sleep(2)
            print("This the iteration number:  ", str(i), " Category:  ", self.xpathProveedoresCategoriesList[i])
            self.driver.find_elements(By.XPATH, self.xpathProveedoresCategoriesList)[i].click()
            time.sleep(2)
            #Call the local method to verify the number of providers by Category
            self.TC_001(self) 
            #if (outputnumberRecords<10):
                
            #else : break
                       
    #This method get the provides list, 
    # Save the detailed provider information in an excel file 
    #for the provider number 3
    # Only for categories with more than three providers listed
    def TC_001(self ,  x):
        
        #Evidences screenshot for category
        endrootScreenProviders= "image"+ str(i) + ".png"
        self.driver.save_screenshot(self.save_screenshotRoot+endrootScreenProviders)  
        category = self.driver.find_element(By.XPATH, self.xpathCategoryName).text
        #Get providers list  
        time.sleep(2)
        providersList = self.driver.find_elements(By.XPATH, self.xpathProvidersList)

        #Write in the output excel file when there are more tahn tree vendors 
        #Only for the vendor number 3 in the vendors list
        if(len(providersList)>2):
            int_currentRow=i
            provider = self.driver.find_elements(By.XPATH, self.xpathProvidersList)[2].text
            print("Provider #3 is  :  ", provider)
            self.driver.find_elements(By.XPATH, self.xpathProvidersList)[2].click()
            time.sleep(2)
            providerDetailsListName = self.driver.find_elements(By.XPATH, self.xpathProviderDetailsListName)
            elementDetailsList = self.driver.find_elements(By.XPATH, self.xpathProviderDetailsList)
            
            for j in range(len(providerDetailsListName)):
                dfi.loc[int_currentRow, providerDetailsListName[j].text] = elementDetailsList[j].text
                
            dfi.loc[int_currentRow, "Proveedor"] = provider
            dfi.loc[int_currentRow, "Categoria"] = category       
            
            dfi.to_excel("/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/Data/Output.xlsx")
            self.driver.back()    
            
            
        time.sleep(2)
        self.driver.back()
        time.sleep(2)