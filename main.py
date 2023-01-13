from growatt import Growatt
from influxdb2 import InfluxDB2Client
import time

interval = 10

inverter = Growatt('/dev/ttyXRUSB0', 'Growatt SPF5000ES', 1)
inverter.connect()
# print(inverter.read_config())
# print(inverter.read_status())
flux = InfluxDB2Client('http://192.168.8.200:8086', 'j50o1SuEDGTmtr_VAs_FVuWmcmpVxef8q1U1eSp2mOsnpkmWSnyA-hsPAtGp0-jOYd_ZEadU5VEtbjKnAHNOlA==', 'nksl', 'growatt_status')

while True:
    status_data = inverter.read_status()
    print(status_data)
    flux.write({"measurement": "growatt_status", "tags": {"location": "home"}, "fields": status_data})
    time.sleep(interval)
