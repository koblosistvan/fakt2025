N = int(input())
szavak = input().split()

teljes = " ".join(szavak)
maganhangzok = "aeiou"
eredmeny = ""

for i in range(len(teljes)-2):
    if teljes[i] in maganhangzok and teljes[i+1] not in maganhangzok and teljes[i+1] != " " and teljes[i+2] not in maganhangzok and teljes[i+2] != " ":
        continue 
    eredmeny += teljes[i]

eredmeny += teljes[-2:]

print(eredmeny[::-1])
