import requests
import json
import csv

print("start")
#------------------------------------------------------------------------------------------
#   SENSORS ID LIST
#------------------------------------------------------------------------------------------
aq_sensor = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/sensors/530')
sensor = []
for s in range(len(json.loads(aq_sensor.text))):
    sensor.append(json.loads(aq_sensor.text)[s]['id'])


def sensors_get():
    aq_sensor = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/sensors/530')
    sensor_new = []
    for s in range(len(json.loads(aq_sensor.text))):
        sensor_new.append(json.loads(aq_sensor.text)[s]['id'])

    name = 'sensors.txt'
    with open(name, 'a') as f:
        for a in range(len(sensor_new)):
            f.write(str(sensor_new[a]) + '\n')
    print('sensors list: ', sensor_new)

def sensors_load():
    sensor = []
    name = 'sensors.txt'
    with open(name, 'r') as f:
        a = 0
        while True:
            f.read(sensor[a])
            a+=1
            break
    print(sensor)

def sensors_check():
    try:
        fs = open("sensors.txt")
        sensors_load()
        print("sensors load")
        fs.close()
    except IOError:
        sensors_get()
        print("sensors get")
        sensors_check()

def get_data():
    #------------------------------------------------------------------------------------------
    #   WEATHER
    #------------------------------------------------------------------------------------------
    weather = requests.get("https://danepubliczne.imgw.pl/api/data/synop/id/12375")
    weather_data = []
    data = json.loads(weather.text)

    weather_data.append(data['data_pomiaru'])
    if int(data['godzina_pomiaru']) >= 10: weather_data.append(data['godzina_pomiaru'] + ':00:00')
    else: weather_data.append('0' + data['godzina_pomiaru'] + ':00:00')
    weather_data.append(' ')
    weather_data.append(data['temperatura'])
    weather_data.append(data['predkosc_wiatru'])
    weather_data.append(data['wilgotnosc_wzgledna'])
    weather_data.append(data['suma_opadu'])
    weather_data.append(data['cisnienie'])

    #------------------------------------------------------------------------------------------
    #   AIR QUALITY
    #------------------------------------------------------------------------------------------
    aq_data = []
    for l in range(len(sensor)):
        url = 'https://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(sensor[l])
        aq = requests.get(url)
        #print(sensor[l])
        #print(weather_data[0] + ' ' + weather_data[1])
        for i in range(len(json.loads(aq.text)['values'])):
            #print(json.loads(aq.text)['values'][i]['date'])
            if json.loads(aq.text)['values'][i]['date'] == weather_data[0] + ' ' + weather_data[1]:
                aq_data.append(json.loads(aq.text)['values'][i]['value'])
                #print(aq_data)
                break
            #else: print('.')


    #------------------------------------------------------------------------------------------
    #   FILE
    #------------------------------------------------------------------------------------------
    name = 'data.csv'
    with open(name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(weather_data + [' '] + aq_data)
    print(weather_data[0] + ' ' + weather_data[1])

#sensors_check()
get_data()