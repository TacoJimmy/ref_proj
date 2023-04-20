'''
Created on 2023年4月20日

@author: infilink
'''
import codecs
import json
import ssl
import paho.mqtt.client as mqtt
import time
import random
import schedule
import json


Comsumption_taipei = 0
Comsumption_taichung = 0
Comsumption_kaohsiung = 0


def tb_mqtt_taipei():
    global Comsumption_taipei
    Power = random.randint(180,240)
    PowerComsumption = Power/ 60
    Comsumption_taipei = Comsumption_taipei + PowerComsumption
    RoomTemperature = random.randint(2.0,4.0)
    CondTermperature = random.randint(36,40)
    HighPressure = random.randint(200,226)
    LowPressure = random.randint(21,35)
    client = mqtt.Client()
    client.on_connect
    client.username_pw_set('bGopZ1xrqCqYbpkEfH9O','XXX')
    client.connect('thingsboard.cloud', 1883, 60)
    payload_iaq = {"RoomTemperature":RoomTemperature,
                   "CondTermperature":CondTermperature,
                   "HighPressure":HighPressure,
                   "LowPressure":LowPressure,
                   "Power":Power,
                   "Comsumption":Comsumption_taipei}
    print(client.publish("v1/devices/me/telemetry", json.dumps(payload_iaq)))
    time.sleep(5)
    
def tb_mqtt_taichung():
    global Comsumption_taichung
    Power = random.randint(180,240)
    PowerComsumption = Power/ 60
    Comsumption_taichung = Comsumption_taichung + PowerComsumption
    RoomTemperature = random.randint(2.0,4.0)
    CondTermperature = random.randint(36,40)
    HighPressure = random.randint(200,226)
    LowPressure = random.randint(21,35)
    client = mqtt.Client()
    client.on_connect
    client.username_pw_set('HvnyhQTiGKQ1w5af8hxb','XXX')
    client.connect('thingsboard.cloud', 1883, 60)
    payload_iaq = {"RoomTemperature":RoomTemperature,
                   "CondTermperature":CondTermperature,
                   "HighPressure":HighPressure,
                   "LowPressure":LowPressure,
                   "Power":Power,
                   "Comsumption":Comsumption_taichung}
    print(client.publish("v1/devices/me/telemetry", json.dumps(payload_iaq)))
    time.sleep(5)
    
def tb_mqtt_kaohsiung():
    global Comsumption_kaohsiung
    Power = random.randint(180,240)
    PowerComsumption = Power/ 60
    Comsumption_kaohsiung = Comsumption_kaohsiung + PowerComsumption
    RoomTemperature = random.randint(2.0,4.0)
    CondTermperature = random.randint(36,40)
    HighPressure = random.randint(200,226)
    LowPressure = random.randint(21,35)
    client = mqtt.Client()
    client.on_connect
    client.username_pw_set('orrUtTx7G4E4piMp1VLl','XXX')
    client.connect('thingsboard.cloud', 1883, 60)
    payload_iaq = {"RoomTemperature":RoomTemperature,
                   "CondTermperature":CondTermperature,
                   "HighPressure":HighPressure,
                   "LowPressure":LowPressure,
                   "Power":Power,
                   "Comsumption":Comsumption_kaohsiung}
    print(client.publish("v1/devices/me/telemetry", json.dumps(payload_iaq)))
    time.sleep(5)

schedule.every(1).minutes.do(tb_mqtt_taipei)
schedule.every(1).minutes.do(tb_mqtt_taichung)
schedule.every(1).minutes.do(tb_mqtt_kaohsiung)

if __name__ == '__main__':

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except:
            pass
