in_modes = open('modes', 'r')
in_speeds = open('speeds', 'r')
out_manual_speeds = open('manual_speeds', 'w')
out_auto_speeds = open('auto_speeds', 'w')

manual_times = []
manual_speeds = []

start_time = 0
end_time = 0

prevline = in_modes.readline().split('\t')
for line in in_modes:
    line = line.split('\t')
    if int(prevline[2]) < 1000 and int(line[2]) > 2000:
        start_time = line[0]
        end_time = 0    
    if int(prevline[2]) > 2000 and int(line[2]) < 1000:
        end_time = line[0]
        manual_times.append((start_time, end_time))
        start_time = 0
        end_time = 0
    prevline = line

print manual_times

for line in in_speeds:
    line = line.split('\t')
    manual_mode = False
    for time_range in manual_times:
        if line[0] >= time_range[0] and line[0] < time_range[1]:
            manual_mode = True
            break
    if manual_mode:
        out_manual_speeds.write('\t'.join(line))
        manual_speeds.append(float(line[1]))
    else:
        out_auto_speeds.write('\t'.join(line))

out_auto_speeds.close()
out_manual_speeds.close()
in_modes.close()
in_speeds.close()

print max(manual_speeds)
