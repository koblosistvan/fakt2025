ora = int(input('Hány óra van? '))
perc = int(input('És perc?' ))

if ora > 12:
    ora = ora-12
elif ora < 12:
    ora = ora 
else:
    print('helytelen időpont')
if ora*5 > perc:
    szög = (ora * 5-perc) * 6
else:
    szög = (perc- ora * 5) *6

print(f'A két mutató {szög} fokos szöget zár be')