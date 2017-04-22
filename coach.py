#coding:utf-8
def read_coach(file):
    try:
        with open(file) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('open file err: '+str(err))

james = read_coach('james.txt')
julie = read_coach('julie.txt')
mikey = read_coach('micky.txt')
sarah = read_coach('sarah.txt')

print(james,julie,mikey,sarah)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))






























    
    
