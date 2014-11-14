from math import radians, cos, sin, asin, sqrt
import re

def output_distances():
    new = []
    new.extend(get_distances('new_antenna1'))
    new.extend(get_distances('new_antenna2'))
    new.extend(get_distances('new_antenna3'))
    new = sorted(list(set(new)))
    print '-----------------break-------------------'
    old = []
    old.extend(get_distances('old_antenna1'))
    old.extend(get_distances('old_antenna2'))
    old.extend(get_distances('old_antenna3'))
    old = sorted(list(set(old)))

    newfile = open('new_data_greater', 'w')
    oldfile = open('old_data_greater', 'w')
    
    for i in range(len(new)):
        newfile.write(`len(new)-1 - i` + '\t' + `new[i]` + '\n')
    
    for i in range(len(old)):
        oldfile.write(`len(old)-1 - i` + '\t' + `old[i]` + '\n')
        
    newfile.close()
    oldfile.close()

def output_distances_histogram(increment):
    new = []
    new.extend(get_distances('new_antenna1'))
    new.extend(get_distances('new_antenna2'))
    new.extend(get_distances('new_antenna3'))
    new = sorted(list(set(new)))
    old = []
    old.extend(get_distances('old_antenna1'))
    old.extend(get_distances('old_antenna2'))
    old.extend(get_distances('old_antenna3'))
    old = sorted(list(set(old)))

    newfile = open('new_data_greater_histogram', 'w')
    oldfile = open('old_data_greater_histogram', 'w')
    
    current = increment

    for i in range(len(new)):
        if new[i] >= current:
            newfile.write(`len(new)-1 - i` + '\t' + `new[i]` + '\n')
            current += increment
            
    current = increment

    for i in range(len(old)):
        if old[i] >= current:
            oldfile.write(`len(old)-1 - i` + '\t' + `old[i]` + '\n')
            current += increment

    newfile.close()
    oldfile.close()


def get_distances(filename):
    f = open(filename, 'r')
    out = open(filename + '_coords', 'w')
    
    lats = []
    lngs = []
    dists = []
    
    lats.append(40.6082624)
    lngs.append(-75.3807168)
    dists.append(0)
    f.readline()
    
    for line in f:
        cols = line.split('\t')
        lats.append(cols[1])
        lngs.append(cols[2])
        out.write('_,_,' + lats[-1] + ', ' + lngs[-1] + '\n')
        if len(lats) > 1:
            dist = haversine(lats[0], lngs[0], lats[-1], lngs[-1])
            print `lats[-1]` + ' ' + `lngs[-1]` + ' ' + `dist`
            dists.append(dist)
    out.close()
    return dists
            

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

output_distances()
#output_distances_histogram(5)
#print sorted(list(set(get_distances('data_goodman'))))

#print haversine(-75.3563712, 40.5845696, -75.3567808, 40.58402888)
