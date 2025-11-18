a,bal,jobb,p=input(),[],[],0
for i in range(len(a)):
 if a[i]=='<':
  jobb.append(i)
 elif a[i]=='>':
  bal.append(i)
for i in range(len(bal)):
 for h in range(len(jobb)):
  if bal[i]<jobb[h]:p+=1
for i in range(len(jobb)):
 for h in range(len(bal)):
  if jobb[i]>bal[h]:p+=1
print(int(p/2))