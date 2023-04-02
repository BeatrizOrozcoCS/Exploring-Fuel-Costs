import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



url = "https://ev-database.org/imp/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~600|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=60~260|range-slider-battery:prev~next=10~200|range-slider-towweight:prev~next=0~2500|range-slider-fastcharge:prev~next=0~1100|paging:currentPage=0|paging:number=all"
# 
driverpath = r"C:\Users\Orozc\OneDrive\My Documents\Projects\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(driverpath)
driver.get(url)


#data to webscrape
url = []
make = []
model = []
useableBattery = []
dateAvaiblible = []

towing =[]
towingweight = []

driveTransmission = []
plugtype = []
bodyType = []
seats=[]

howfast_0_62 = []
topSpeed = []
Range = []
efficiency =[]
fastcharge = []

priceGermany =[]
priceNeatherlands = []
priceUK = []

i=0 #counter
# get the results
cars = driver.find_elements(By.CLASS_NAME,"list-item")

for car in cars:
     i+=1
     try:
         carMake = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[2]/h2/a/span[1]').get_attribute("innerHTML")
         carModel = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[2]/h2/a/span[2]').get_attribute("innerHTML")
         carUrl = car.find_element(By.TAG_NAME, "a").get_attribute("href")
        
         carUseableBattery = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[2]/div/span[1]').get_attribute("innerHTML")
         carDateAvaiblible = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[2]/div/span[2]').get_attribute("textContent").split(" ")
         carDate = carDateAvaiblible[-2] + " " + carDateAvaiblible[-1]
         
         carTowing = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[1]').get_attribute("innerHTML")
         
         if carTowing == "":
            carTowingweight = ""
            carDriveTransmission = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[2]').get_attribute("title")
            carPlugtype = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[3]').get_attribute("textContent")
            carBodyType =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[4]').get_attribute("textContent")
            carSeats =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[7]').get_attribute("textContent")
            carHowfast_0_62 = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")            
            carTopSpeed = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")           
            carRange = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")           
            carEfficiency = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")           
            carFastcharge = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")   
          
         else:
            carTowingweight = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[3]/span[3]').get_attribute("innerHTML")
            carDriveTransmission = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[4] ').get_attribute("title")
            carPlugtype =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[5]').get_attribute("textContent")
            carBodyType =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[6]').get_attribute("textContent")
            carSeats =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[3]/span[9]').get_attribute("textContent")
             
         carHowfast_0_62 = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[4]/p[1]/span[2]').get_attribute("textContent").strip(" sec")            
         carTopSpeed = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[4]/p[2]/span[2]').get_attribute("textContent").strip(" mph")           
         carRange = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[4]/p[3]/span[2]').get_attribute("textContent").strip(" mi")           
         carEfficiency = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[4]/p[4]/span[2]').get_attribute("textContent").strip(" Wh/mi")            
         carFastcharge = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div[' +str(i) +']/div/div[4]/p[5]/span[3]').get_attribute("textContent")   

         carPriceGermany =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[5]/span[1]/span[1]').get_attribute("textContent")                 
         carPriceNeatherlands =car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[5]/span[2]/span[1]').get_attribute("textContent")               
         carPriceUK = car.find_element(By.XPATH, '//*[@id="evdb"]/main/div[2]/div[3]/div['+ str(i) +']/div/div[5]/span[3]/span[1]').get_attribute("textContent")           
          
         #print(carPriceGermany +" "+ carPriceNeatherlands +" " +carPriceUK)
     except:
         print("missinng")
     url.append(carUrl)
     make.append(carMake)
     model.append(carModel)
     useableBattery.append(carUseableBattery)
     dateAvaiblible.append(carDate)

     towing.append(carTowing)
     towingweight.append(carTowingweight)

     driveTransmission.append(carDriveTransmission)
     plugtype.append(carPlugtype)
     bodyType.append(carBodyType)
     seats.append(carSeats)

     howfast_0_62.append(carHowfast_0_62)
     topSpeed.append(carTopSpeed)
     Range.append(carRange)
     efficiency.append(carEfficiency)
     fastcharge.append(carFastcharge)

     priceGermany.append(carPriceGermany)
     priceNeatherlands.append(carPriceNeatherlands)
     priceUK.append(carPriceUK)  
    


data = pd.DataFrame(zip(make,model,
useableBattery,dateAvaiblible,
towing,towingweight,
driveTransmission,plugtype,
bodyType,seats,howfast_0_62,
topSpeed,Range,efficiency,
fastcharge,priceGermany,
priceNeatherlands,priceUK,url),
columns = ["make","model",
           "useableBattery","date Avaiblible", "towing?",
           "towing Weight", "Transmission", "plug Type",
           "body Type", "seats", "how fast 0-60 (s)",
           "Top Speed (mph)", "Range (mi)", "efficiency (Wh/mi)",
           "fast Charge (mph)", "priceGermany", "priceNeatherlands", "priceUK", "url"])


data.to_excel("Electrical Car Data Set.xlsx")



