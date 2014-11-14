import  matplotlib.pyplot as py

def get_dicts(filename):
    fin = open(filename, 'r')
    dicts = []
    keys = fin.readline().split('\t')
    for line in fin:
        values = line.split('\t')
        dictionary = {}
        for i in range(len(keys)):
            dictionary[keys[i]] = values[i]
        dicts.append(dictionary)
    return dicts

def get_automode_gps_coords(data):
    count = 0
    fout = open('auto0', 'w')
    
    for d in data:
        if d['mode'] == "'Manual'":
            if not fout.closed:
                count += 1
            fout.close()
        elif d['mode'] == "'Auto'":
            if fout.closed:
                fout = open('auto' + str(count), 'w')
            fout.write(d['lat'] + ',' + d['lng'] + '\n')
    fout.close()

def get_automode_rudder_accel(data):
    fout = open('rudder_accel', 'w')
    
    for d in data:
        if d['mode'] == "'Auto'":
            fout.write(d['groundspeed'] + '\t' + `float(d['ch1out'])` + '\t' + `float(d['gz'])` + '\n')
    fout.close()

data = get_dicts('boat_data2')
#get_automode_gps_coords(data)
get_automode_rudder_accel(data)