def network(L, first = None, second = None):
    connection = []
    for item in L:
        connection.append({item.split('-')[0], item.split('-')[1]})
    print(connection)
    l = [item for item in connection if item.issuperset({first})]
    print(l)
    if {first, second} in connection:
        return True
    else:
        pass
            



















test_L = ['a1-a2', 'a2-a3', 'a2-a8', 'a3-a4', 'a3-a5', 'a5-a8',
          'a8-a7', 'a6-a7']

network(test_L,'a1','a6')
