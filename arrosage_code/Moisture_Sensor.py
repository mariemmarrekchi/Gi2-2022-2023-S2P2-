#https://www.freva.com/fr/capteur-de-temperature-et-humidite-dht11-avec-raspberry-pi/
#https://www.bujarra.com/midiendo-la-presion-atmosferica-con-raspberry-pi/?lang=fr
#https://github.com/Thaldos/Raspberry-solenoid-valve
#https://peppe8o.com/capacitive-soil-moisture-sensor-with-raspberry-pi-pico-wiring-code-and-calibrating-with-micropython/
#https://www.instructables.com/Soil-Moisture-Sensor-Raspberry-Pi/
import smbus2 as smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
	global address
	address = Addr

def read(chn): #channel
	try:
		if chn == 0:
			bus.write_byte(address,0x40)
		if chn == 1:
			bus.write_byte(address,0x41)
		if chn == 2:
			bus.write_byte(address,0x42)
		if chn == 3:
			bus.write_byte(address,0x43)
		bus.read_byte(address) # dummy read to start conversion
	except Exception as e:
		print ("Address: %s" % address)
		print (e)
	return bus.read_byte(address)

def write(val):
	try:
		temp = val # move string value to temp
		temp = int(temp) # change string to integer
		# print temp to see on terminal else comment out
		bus.write_byte_data(address, 0x40, temp)
	except Exception as e:
		print ("Error: Device address: 0x%2X" % address)
		print (e)
		temp=False
	return (temp)

def get_moisture_sensor():
	setup(0x48)
	#https://github.com/Miceuz/i2c-moisture-sensor/blob/master/README.md
	#https://github.com/modmypi/Moisture-Sensor/blob/master/moisture.py
	#print ('AIN0 = ', read(2))
	print ('AIN1 = ', read(1))
	tmp = read(1)
	
	return tmp

