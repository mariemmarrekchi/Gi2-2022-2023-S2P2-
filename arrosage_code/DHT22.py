import Adafruit_DHT as dht

def get_humtemp_temperature():

    humidite, temperature = dht.read_retry(dht.DHT22, 23)

    if humidite is not None and temperature is not None:
        return (humidite,temperature)
    else:
        return (-1,-1)