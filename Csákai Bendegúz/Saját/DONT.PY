import random
list = ['Yes', 'No', 'Maybe']
'''T = False
ans_list = []
while T != True:
    ans_list.append(Answ)'''
yes=0
no=0
maybe=0
ans_list = []
meg = []
for i in range(100):
    Answ = random.choice(list)
    ans_list.append(Answ)
print(ans_list)
for i in ans_list:
    if i == list[0]:
        yes += 1
    elif i == list[1]:
        no += 1
    else:
        maybe += 1
meg.append(yes)
meg.append(no)
meg.append(maybe)
er = ''
if max(meg) == yes:
    er = 'Yes'
elif max(meg) == no:
    er = 'No'
else:
    er = 'Maybe'
print(f'A döntés {max(meg)} db eredménnyel lett {er} [{yes,no,maybe}]')