import math

kis_r = int(input('Kis r: '))
nagy_r = int(input('Nagy r: '))
koz_tav = int(input('koz_tav: '))
egy = (koz_tav**2 - (nagy_r-kis_r)**2)**0.5
print(f'Iv egyenes = {egy:.2f} cm')
alfa = math.degrees(math.asin((nagy_r-kis_r)/koz_tav))
gam = 180-(2*alfa)
bet = 180+(2*alfa)
pi = math.pi
kicsi = (gam/360)*(2*pi)*kis_r
nagy = (bet/360)*(2*pi)*nagy_r
print(f'Adatok: \n{alfa:.2f}\n{gam:.2f}\n{bet:.2f}')
print(f'Kicsi iv = {kicsi:.2f} cm')
print(f'Nagy iv = {nagy:.2f} cm')
print(f'Összeg: {kicsi + nagy + (2*egy):.2f} cm')
