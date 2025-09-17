helyezes =int(input('Hányadik lettél? '))

if helyezes == 1:
    print('aranyérem')
elif helyezes == 2:
    print('ezüstérem')
elif helyezes == 3:
    print('bronzérem')
elif helyezes < 1:
    print('ne szórakozz') 
else:
    print('nem kapsz érmet')


