# 18 prímszám
'''
szam = int(input('Add meg a számot: '))
if szam < 2:
    print(f'{szam} nem prím.')
elif szam == 2:
    print(f'{szam} prím.')
else:
    for i in range(2, int(szam**0.5)):
        if szam % i == 0:
            print(f'{szam} nem prím.')
            break
    else:
        print(f'{szam} prím.')
'''

# 30 Newton módszer
szam = float(input('Add meg a számot: '))
becsles_felso = szam
becsles_also = 0
pontossag = 10
while (becsles_felso - becsles_also) > 1 / 10**pontossag:
    becsles_kozep = (becsles_also + becsles_felso) / 2
    if becsles_kozep**2 == szam:
        break
    elif becsles_kozep**2 < szam:
        becsles_also = becsles_kozep
    else:
        becsles_felso = becsles_kozep

print(f'{szam} négyzetgyöke {becsles_kozep}.')