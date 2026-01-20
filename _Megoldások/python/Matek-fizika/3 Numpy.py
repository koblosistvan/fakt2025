
import numpy as np

# -----------------------------------------------------------------------------
# Vektorszorzás (skaláris szorzat)
# Két 3D vektor beolvasása (pl. '1 2 3'), numpy tömbbé alakítás és skaláris szorzat.
# -----------------------------------------------------------------------------
a_list = list(map(float, input("Add meg az első 3D vektort (pl. '1 2 3'): ").strip().split()))
b_list = list(map(float, input("Add meg a második 3D vektort (pl. '4 5 6'): ").strip().split()))
a = np.array(a_list, dtype=float)
b = np.array(b_list, dtype=float)
if a.shape != (3,) or b.shape != (3,):
    raise ValueError("Mindkét vektornak 3 eleműnek kell lennie.")
dot = np.dot(a, b)  # skaláris szorzat
print(f'{a} · {b} = {dot}')


# -----------------------------------------------------------------------------
# Zajszűrés: 100 elemű szinusz + normál zaj, majd átlag számítása
# Létrehoz egy 100 elemű szinuszfüggvényt (alapértelmezés), zajt ad hozzá, visszaadja az átlagát.
# -----------------------------------------------------------------------------
n = 100           # mintavételek száma
freq = 1.0        # a szinusz frekvenciája
noise_mu = 0.0    # a normális eloszlású zaj átlaga
noise_sigma = 0.2 # a normális eloszlású zaj szórása
seed = 42         # a véletlenszám generátor kiinduló értéke, hogy azonos "véletlen" zajt generáljunk

rng = np.random.default_rng(seed)           # _R_andom _N_umber _G_enerator létrehozása
t = np.linspace(0, 1, n, endpoint=False)    # mintavételi időpontok generálása egy tömbbe
clean = np.sin(2 * np.pi * freq * t)        # tiszta jel kiszámítása
noise = rng.normal(loc=noise_mu, scale=noise_sigma, size=n)     # zaj kiszámítása
signal = clean + noise                      # zajos jel kiszámítása
mean_val = signal.mean()                    # zajos jel átlaga
print(f'{t=}\n{clean=}\n{noise=}\n{signal=}')
print(f'{mean_val=}')


# -----------------------------------------------------------------------------
# Mátrix determináns (2x2)
# Egy 2x2-es mátrix elemeinek beolvasása és determináns számítása NumPy-val.
# -----------------------------------------------------------------------------
r1 = list(map(float, input("Add meg az első sort (pl. '1 2'): ").strip().split()))
r2 = list(map(float, input("Add meg a második sort (pl. '3 4'): ").strip().split()))
M = np.array([r1, r2], dtype=float)
if M.shape != (2, 2):
    raise ValueError("A mátrixnak 2x2-esnek kell lennie.")
d = np.linalg.det(M)
print(f'Mátrix determinálna: {d}')


# -----------------------------------------------------------------------------
# Normálás (10 véletlen szám összege = 1)
# -----------------------------------------------------------------------------
seed = 42         # a véletlenszám generátor kiinduló értéke, hogy azonos "véletlen" adatsort generáljunk

rng = np.random.default_rng(seed)
vals = rng.random(10)
s = vals.sum()
# védelem s=0 esetre (gyakorlatilag nem fordul elő uniform randomnál):
normed = np.zeros_like(vals) if s == 0 else vals / s
print(f'{vals=}\n{normed=}')


# -----------------------------------------------------------------------------
# Polinom értékei: P(x) = 2x^3 - 5x + 3, x ∈ [-5, 5], 50 pont
# -----------------------------------------------------------------------------
n = 50      # mintavételi pontok száma
x_min=-5.0  # intervallum kezdete
x_max=5.0   # intervallum vége

x = np.linspace(x_min, x_max, n)
# P(x) = 2x^3 - 5x + 3
p = 2 * x**3 - 5 * x + 3


# -----------------------------------------------------------------------------
# 6) Frekvencia-idő: 50 Hz-es szinusz 0..1 s között 1000 pont
# -----------------------------------------------------------------------------
def sine_50hz(n=1000, f=50.0, t_start=0.0, t_end=1.0):
    t = np.linspace(t_start, t_end, n, endpoint=False)
    y = np.sin(2 * np.pi * f * t)
    return t, y


# -----------------------------------------------------------------------------
# 7) Radioaktív bomlás: N(t)=N0 * exp(-λ t) 100 elemű időtömbre
# -----------------------------------------------------------------------------
def radioactive_decay(N0, lam, n=100, t_start=0.0, t_end=10.0):
    t = np.linspace(t_start, t_end, n)
    N = N0 * np.exp(-lam * t)
    return t, N


# -----------------------------------------------------------------------------
# 8) Mérési hiba: std és var egy adott tömbre
# -----------------------------------------------------------------------------
def stats_of_measurements_from_input():
    """
    Beolvas egy mérési tömböt (pl. '1.2 1.3 1.25 1.27') és kiszámolja std és var értékeket.
    """
    arr = np.array(list(map(float, input("Add meg a mérési értékeket (szóközzel elválasztva): ").strip().split())))
    std_val = np.std(arr)
    var_val = np.var(arr)
    return arr, std_val, var_val


# -----------------------------------------------------------------------------
# 9) Egyenletrendszer megoldása: ax+by=e, cx+dy=f
# -----------------------------------------------------------------------------
def solve_linear_system_from_input():
    """
    Bemenet: a, b, c, d, e, f (szóközzel elválasztva).
    Megoldás: np.linalg.solve a 2x2 rendszerre.
    """
    a, b, c, d, e, f = map(float, input("Add meg a,b,c,d,e,f értékeket (pl. '1 2 3 4 5 6'): ").strip().split())
    A = np.array([[a, b], [c, d]], dtype=float)
    rhs = np.array([e, f], dtype=float)
    # Ellenőrzés: szinguláris-e a mátrix?
    if np.isclose(np.linalg.det(A), 0.0):
        raise ValueError("A rendszer szinguláris (determináns = 0), nincs egyértelmű megoldás.")
    x = np.linalg.solve(A, rhs)
    return A, rhs, x


# -----------------------------------------------------------------------------
# 10) Ideális gáz: P = n R T / V, T 273..373 K között 20 pont
# -----------------------------------------------------------------------------
def ideal_gas_pressure(n=1.0, V=0.024, T_min=273.0, T_max=373.0, nT=20, R=8.314462618):
    """
    n: anyagmennyiség (mol)
    V: térfogat (m^3) - például 0.024 m^3 ~ 24 liter
    R: egyetemes gázállandó (J/(mol*K))
    """
    T = np.linspace(T_min, T_max, nT)
    P = n * R * T / V
    return T, P


# -----------------------------------------------------------------------------
# DEMÓ FUTTATÁS (kommenteld ki/át, ha csak a függvények kellenek)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # 1) Vektorszorzás - interaktív:
    # a, b, dot = scalar_product_from_input()
    # print("a =", a, " b =", b, " skaláris szorzat =", dot)

    # 2) Zajos szinusz és átlag:
    t, clean, noise, sig, mean_val = noisy_sine_mean(n=100, freq=5.0, noise_mu=0.0, noise_sigma=0.3, seed=42)
    print("[2] Zajos szinusz átlag:", mean_val)

    # 3) 2x2 determináns - interaktív:
    # M, d = det_2x2_from_input()
    # print("[3] Mátrix:\n", M, "\nDetermináns:", d)

    # 4) Normálás (10 random):
    vals, normed, s = normalize_random_10(seed=123)
    print("[4] 10 véletlen:", np.round(vals, 6))
    print("[4] Normalizált:", np.round(normed, 6), " Összeg:", float(s))

    # 5) Polinom értékek:
    x, p = poly_values(n_points=50, x_min=-5.0, x_max=5.0)
    print("[5] P(x) első 5 érték:", np.round(p[:5], 6))

    # 6) 50 Hz szinusz:
    t50, y50 = sine_50hz(n=1000, f=50.0, t_start=0.0, t_end=1.0)
    print("[6] 50Hz szinusz minták száma:", y50.size)

    # 7) Radioaktív bomlás:
    tdec, N = radioactive_decay(N0=1000.0, lam=0.2, n=100, t_start=0.0, t_end=10.0)
    print("[7] N(t) első 5 érték:", np.round(N[:5], 6))

    # 8) Mérési hiba - interaktív:
    # arr, std_val, var_val = stats_of_measurements_from_input()
    # print("[8] Tömb:", arr, " STD:", std_val, " VAR:", var_val)

    # 9) Egyenletrendszer - interaktív:
    # A, rhs, sol = solve_linear_system_from_input()
    # print("[9] A=\n", A, "\nRHS=", rhs, "\nMegoldás x,y =", sol)

    # 10) Ideális gáz (P = nRT/V):
    T, P = ideal_gas_pressure(n=1.0, V=0.024, T_min=273.0, T_max=373.0, nT=20)
    print("[10] T első 5:", np.round(T[:5], 3), "  P első 5:", np.round(P[:5], 3))
