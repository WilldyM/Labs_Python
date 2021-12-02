addresses = [
    'www.youtube',
    'wresting',
    'github.com',
    'vk.com',
    'www.silencesfrom'
    ]
print(addresses)

addresses2 = [s for s in addresses if s[0:3] == 'www']
addresses2 = addresses2 + ['www.'+s for s in addresses if s[0:3] != 'www']
addresses2 = ['http://'+s for s in addresses2]
addresses3 = [s for s in addresses2 if s[len(s)-4:len(s)] == '.com']
addresses3 = addresses3 + [s+'.com' for s in addresses2 if s[len(s)-4:len(s)] != '.com']
print('Отформатированные строки:')
print(addresses3)

