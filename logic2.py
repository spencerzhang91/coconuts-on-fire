# rubish code to handle excel names
import csv
old_names = open(r'E:\work.csv')
text = open(r'E:\work.txt', 'w')

def cuttail_c(name):
    new = ''
    
    if '司' not in name and '团' not in name and '厂' not in name:
        new = 'asshole'
    else:
        for char in name:
            if char != '司' and char != '团' and char != '备' and char != '厂':
                new += char
            else:
                break
    # new += '司'
    return new

def cuttail_f(name):
    new = ''
    for char in name:
        if char != '厂':
            new += char
        else:
            break
    # new += '厂'
    return new


def clean(origin, destin):
    temps1 = []
    temps2 = []
    reader = csv.reader(origin) 
    for name in origin:
        temps1.append(cuttail_c(name))
    origin.close()
    #for name in temps1:
        #temps2.append(cuttail_f(name))
    for item in temps1:
        destin.write(item + '\n')


clean(old_names, text)
text.close()

old_text = open(r'E:\work.txt', 'r')
new_text = open(r'E:\finalwork.txt', 'w')
cnt = 0
for item in old_text:
    if item[-2] == '公':
        new_text.write(item.rstrip() + '司' + '\n')
    elif item[-2] == '集':
        new_text.write(item.rstrip() + '团' + '\n')
    elif item[-2] == 'e':
        new_text.write(item.rstrip() + '\n')
        cnt += 1
    else:
        new_text.write(item.rstrip() + '厂' + '\n')


print(cnt)

