T=input('Jelek: ')
a="><-"
b=0
p=0
for i in range(len(T)):
 if T[i] in a:
     if T[i]=='>':
      b+=1
     elif T[i]=='<':
      p+=b
print(p)