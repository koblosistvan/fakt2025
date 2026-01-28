import math
tömeg=float(input("Add meg a tömeget: "))
hajlásszög= float(input("Add meg a hajlásszöget fokban: "))
hajlásszög=math.radians(hajlásszög)
lejtőirány=tömeg*9.81*math.sin(hajlásszög)
print(f'A lejtőirány az {lejtőirány:.2f} N')