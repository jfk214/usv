import datetime as datetime

fin = open('times', 'r')
prev_time = 0
telem_rate = 0
count = 0

for line in fin:
    line = map(int, line.split('\t'))
    time = datetime.datetime(2014, 11, 10, line[0], line[1], line[2], line[3])
    if prev_time != 0:
        dif = (time - prev_time).microseconds/1000
        if dif != 0:
            #print dif
            telem_rate += dif
            count += 1
    prev_time = time

telem_rate /= float(count)
telem_rate = 1000/telem_rate
print telem_rate
