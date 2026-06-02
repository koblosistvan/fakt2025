# 1.fájl 
forras = open("_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-1.txt", mode="r",encoding="utf-8")
adat = forras.readline().strip()







# 2.fájl 
forras = open("_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-2.txt", mode="r",encoding="utf-8")
adat = forras.readline().strip()
adat.split(" ")


# 3.fájl 
forras = open("_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-3.txt", mode="r",encoding="utf-8")
adat =[]
for sor in forras:
    adat.append(sor.strip())

# 4.fájl 
forras = open("_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-3.txt", mode="r",encoding="utf-8")
forras.readline()
adat =[]
for sor in forras:
    adat.append(sor.strip())



#feladat

gyongy = []

for i in range(len(adat)):
    if adat[i] not in gyongy:
        gyongy.append(adat[i])


print(f'{len(gyongy)}db gyöngy van')



egymasutan = "nincs"

for i in range(len(adat)-1):
    if adat[i] == adat[i+1]:
        egymasutan = "van"

print(f'{egymasutan} 2 gyöngy')


M_db = int(input("Milyen hosszú láncot keresel? "))
counter = 1
elf = "Nem fordul elő"

for i in range(len(adat)-1):
    if adat[i] == adat[i+1]:
        counter += 1
    if M_db == counter:
        elf = "Előfordul"


print(f'{elf} hogy {M_db}szor egymás után jön ugyanolyan szín') 



max_counter = 0
max_color = ''
current_counter = 1
first_counter = 0

for i in range(len(adat)-1):
    if adat[i] == adat[i+1]:
        current_counter += 1
    else:
        current_counter = 1
        first_counter = current_counter
    if current_counter > max_counter:
        max_counter = current_counter
        max_color = adat[i]
if adat[-1] == adat[0]:
    if first_counter + current_counter > max_counter:
        max_counter = first_counter + current_counter
        max_color = adat[0]


print(max_counter)
print(max_color)
