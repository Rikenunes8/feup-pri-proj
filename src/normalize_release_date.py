from sys import argv

if len(argv) != 3:
    raise Exception()

filename_from = argv[1]
filename_to = argv[2]

def to_year(date):
    return date.split('-')[0]

file = open(filename_from, 'r', encoding='utf-8')

line = file.readline()
if not line:exit()
with open(filename_to, 'w', encoding='utf-8') as f:
        f.write(line)

while True:
    line = file.readline()
    if not line:break

    fields = line.split(';')
    fields[2] = to_year(fields[2])

    with open(filename_to, 'a',  encoding='utf-8') as f:
        f.write(';'.join(fields))

file.close()