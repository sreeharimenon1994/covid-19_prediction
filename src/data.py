from ast import literal_eval

city = literal_eval(open('data/density.json','r').read())
density = literal_eval(open('data/density.json','r').read())

both = []
missing = []
for x in city:
    flag = False
    for y in density:
        if x[0].lower() == y[0].lower():
            both.append(x[0])
            flag = True
            break
    if flag == False:
        missing.append(x)

print(len(both), 'both')
print(len(missing), 'missing')
missing
