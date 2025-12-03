helyezes = int(input('Hányadik helyezést értél el? '))

if helyezes == 1:
    print('Gratulálunk! Arany érmet szereztél!')
elif helyezes == 2:
    print('Gratulálunk! Ezüst érmet szereztél!')
elif helyezes ==3:
    print('Gratulálunk! Bronz érmet szereztél!')
elif helyezes <10:
    print('Gratulálunk! Benne vagy a Top 10-ben!')
elif helyezes < 1:
    print('Na ne szórakozz velem')
else:
    print('Na majd legközelebb')