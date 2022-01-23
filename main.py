import requests
import json
import csv

#fpath = "/home/kijada/studia/os/" # for ubuntu
fpath = "" # for wid10 + pycharm

#   CONFIG  #
with open(fpath+"config", 'r') as fconfig:
    config = []
    while True:
        line = fconfig.readline()
        if line == "": break
        else:
            config.append(line.split('\t'))
#print('read config: ', config)

#   STATION #
for i in range(len(config)):
    if len(config[i]) > 5:
        config[i].pop(len(config[i])-1)
        g = False
        break
    else: g = True
    config[i].pop(len(config[i])-1)
    for j in range(1, len(config[i])):
        if int(config[i][j]) < 1000:
            aq_sensor = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/sensors/' + config[i][j])
            config[i].append(len(json.loads(aq_sensor.text)))
            for s in range(len(json.loads(aq_sensor.text))):
                config[i].append(int(json.loads(aq_sensor.text)[s]['id']))
if g:
    with open(fpath+"config", 'w') as fconfig:
        for i in range(len(config)):
            for j in range(len(config[i])):
                fconfig.write(str(config[i][j]) + '\t')
            fconfig.write('-1\n')
    print('overwrite')

print('config', config)

# GET DATA  #
# WEATHER #
data = []
for i in range(len(config)):
    print('station:', i+1)


    #   WEATHER   #
    weather = requests.get("https://danepubliczne.imgw.pl/api/data/synop/id/" + config[i][0])
    raw = json.loads(weather.text)
    key = list(raw.keys())
    data.clear()
    for j in range(len(raw)):
        value = ['', '']
        value[0] = key[j]
        value[1] = raw[key[j]]
        data.append(value)


    #   AIR QUALITY #
    stations = []
    for j in range(1, len(config[i])):
        if int(config[i][j]) > 100: stations.append(config[i][j])
        else: break
    #print(stations)

    sensor = []
    for j in range(len(stations), len(config[i])):
        sensor.clear()
        if int(config[i][j]) < 100:
            for l in range(j+1, j+1+int(config[i][j])): sensor.append(config[i][l])
        for l in range(len(sensor)):
            aq_data = ['', '']
            aq = requests.get('https://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(sensor[l]))
            aq_data[0] = json.loads(aq.text)['key']
            aq_data[1] = json.loads(aq.text)['values'][0]['value']
            data.append(aq_data)
            #print(sensor[l], aq_data)




    print(data)
