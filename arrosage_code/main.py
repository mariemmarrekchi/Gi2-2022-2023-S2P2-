import time
import bme280
import Moisture_Sensor as MS
import realy as relay
import DHT22 as DH
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account Firebase.
cred = credentials.Certificate('pharmacie-projet-firebase-adminsdk-pz7us-c7ffb189fd.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
i=0
while True:
    watering=0
    pressure  = bme280.get_pressure()
    #temperature, pressure, humidity = baro.get_temperature_pressure_humidity()
    humidity,temperature  = DH.get_humtemp_temperature()
    Moisture_Sensor=MS.get_moisture_sensor() 
 
    print('Temperature:',(temperature))
    print('Pressure:', pressure)
    print('Humidity:', humidity)
    print('Moisture_Sensor:', (Moisture_Sensor))
    data={
            'hmidity':humidity,
            'pression':pressure,
            'temperature':humidity,
            'moisture_Sensor':Moisture_Sensor,
            "timestamp":datetime.datetime.now()
        }
    db.collection(u'm2m').document(u'autoincrement'.join(str(i))).set(data)



#les valeurs sont variables
    if ((temperature>18 and temperature<31 ) and (Moisture_Sensor >200) and (pressure >1000 and humidity > 50)) :
            relay.vanne_on()
            watering+=1
            print('vanne on')
            time.sleep(5)
            relay.vanne_off()
            print('vanne off')
    i+=1
    time.sleep(3)



