import datetime as datetime
from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6367000 * c
    return km 

def get_telem_rate(filename):
    fin = open(filename, 'r')
    prev_time = 0
    telem_rate = 0
    count = 0
    
    for line in fin:
        line = map(int, line.split('\t'))
        time = datetime.datetime(2014, 11, 10, line[0], line[1], line[2], line[3])
        if prev_time != 0:
            dif = (time - prev_time).microseconds/1000
            if dif != 0:
                telem_rate += dif
                count += 1
        prev_time = time
    
    telem_rate /= float(count)
    telem_rate = 1000/telem_rate
    return telem_rate

def parse_csv(filename, gs_lat, gs_lon):
    fin = open(filename, 'r')
    current_distance = 0
    prev_time = 0
    for line in fin:
        line = line.split(',')
        time = line[0].split('T')[1].split(':')
        time = datetime.datetime(2014, 11, 10, int(time[0]), int(time[1]), int(time[2].split('.')[0]), int(time[2].split('.')[1])*1000)
        if 'lat' in line and 'lon' in line:
            lat = float(line[line.index('lat')+1])/10000000
            lon = float(line[line.index('lon')+1])/10000000
            current_distance = haversine(gs_lat, gs_lon, lat, lon)
        if prev_time != 0:
            dif = (time - prev_time).microseconds/1000
            print `current_distance` + ' ' + `dif`
        prev_time = time

def parse_csv_gps(filename, gs_lat, gs_lon):
    fin = open(filename, 'r')
    current_distance = 0
    prev_time = 0
    telem_rate = 0
    count = 0
    
    for line in fin:
        line = line.split(',')
        time = line[0].split('T')[1].split(':')
        time = datetime.datetime(2014, 11, 10, int(time[0]), int(time[1]), int(time[2].split('.')[0]), int(time[2].split('.')[1])*1000)
        if 'lat' in line and 'lon' in line:
            lat = float(line[line.index('lat')+1])/10000000
            lon = float(line[line.index('lon')+1])/10000000
            current_distance = haversine(gs_lat, gs_lon, lat, lon)
            if prev_time != 0:
                dif = (time - prev_time).microseconds/1000
                if dif != 0:
                    telem_rate += dif
                    count += 1
            prev_time = time
    telem_rate /= float(count)
    telem_rate = 1000/telem_rate
    return telem_rate

def packets_sec_hist(filename):
    fin = open(filename, 'r')
    fout = open('packets_sec', 'w')
    prev_time = 0
    seconds_dict = {}
    
    for line in fin:
        line = line.split(',')
        time = line[0].split('T')[1].split(':')
        time = datetime.datetime(2014, 11, 10, int(time[0]), int(time[1]), int(time[2].split('.')[0]), int(time[2].split('.')[1])*1000)
        key = str(time.hour) + str(time.minute) + str(time.second)
        if time != prev_time:
            if not key in seconds_dict.keys():
                seconds_dict[key] = 0
            seconds_dict[key] += 1
        
        prev_time = time
    
    packets_dict = {}
    for key, value in seconds_dict.iteritems():
        if not value in packets_dict:
            packets_dict[value] = 0
        packets_dict[value] += 1
    
    for key, value in packets_dict.iteritems():
        fout.write(`key` + '\t' + `value` + '\n')

print get_telem_rate('times')
print parse_csv_gps('2014-11-10 14-07-20.csv', 40.6258732, -75.4600782)
packets_sec_hist('2014-11-10 14-07-20.csv')
