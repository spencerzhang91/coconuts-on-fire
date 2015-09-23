# clarified code for extract name of organizations
import csv

old_names = open(r'E:\work.csv', newline='')
new_names = open(r'E:\\result.csv', 'w', newline='')

def cuttail_c(name):
    new = ''
    
    if '司' not in name and '团' not in name and '厂' not in name:
        new = 'UNRECOGNIZED'
    else:
        for char in name:
            if char != '司' and char != '团' and char != '备' and char != '厂':
                new += char
            else:
                break
    return new

def clean(origin, destin):
    temps1 = []
    cnt = 0

    for name in origin:
        temps1.append(cuttail_c(name))
    origin.close()
    writer = csv.writer(destin)
    for item in temps1:
        if item[-1] == '公':
            item += '司'
        elif item[-1] == '集':
            item += '团'
        elif item[-1] == 'D':
            item += ''
            cnt += 1
        else:
            item += '厂'
        writer.writerow([item])
    destin.close()
    print("%d ommited names." % cnt)


clean(old_names, new_names)

