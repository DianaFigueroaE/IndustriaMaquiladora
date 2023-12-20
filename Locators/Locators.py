
class MyLocators:
    
    URL = "https://industriamaquiladora.com/"
    DriverPath = '/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/WebDrivers/chromedriver'
    
    xpathProveedorsOptionCard = "//h4[contains(text(), 'PROVEEDORES')]"
    #"//*[@id='extFeatures8-9']/div/div/div[2]/div/h4"
    cssProveedorCard= "h4:contains('PROVEEDORES')"
    xpathProveedoresCategoriesList = "//div[@class = 'raya mayusculas']"
    xpathListProviders= "//div[@class = 'col-md-10']"
    xpathProviderDetailsListName = "//div[@class = 'row']/div[@class= 'col-md-4']"
    xpathProviderDetailsList = "//div[@class = 'row']/div[@class= 'col-md-8']"
    root_Excel= "/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/Data/Output.xlsx"
    root_Excel_Results2 = "/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/Data/Output - Sheet1.csv"
    save_screenshotRoot = "/Users/diana.figueroa/Desktop/DianysPersonalAuto/IndustriaMaquiladora/Evidences/screenshot/"
    xpath_CategoryName= "//h2[@class='mbr-section-title mbr-fonts-style display-2 mayusculas']"
    
    #Evidences Table
    list_Columns = ["Estado"] 
 