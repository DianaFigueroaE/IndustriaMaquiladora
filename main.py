import unittest
from selenium import webdriver
from TestCases.TC001 import TC001
from selenium.webdriver.chrome.service import Service
from Locators.Locators import MyLocators

import HtmlTestRunner

class indistriaMaquiladora(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting Test")
        myServie =  Service(MyLocators.DriverPath)
        cls.driver = webdriver.Chrome(service= myServie)
        
        
    def test_indistriaMaquiladora(self):
      driver= self.driver 
      tc_01 = TC001(driver)
      tc_01.start()
      
    @classmethod
    def tearDownClass(cls):
      cls.driver.close()
      cls.driver.quit()
      print("Test Completed")
 

if __name__== '__main__':  #if the main code execue from unitmain
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/Evidences/Reports'))
    