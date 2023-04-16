# Importē bibliotēkas
import sys

# Ielasīt lietotāja ievadi
def ielasit_ievadi():
    # Izvēles ielasīšana
    izvele = input().strip()
    if izvele == 'I':
        # Ja lietotājs izvēlas ievadīt pašam
        paraugs = input().strip()
        teksts = input().strip()
    elif izvele == 'F':
        # Ja lietotājs izvēlas ielasīt failu
        with open('./tests/06') as f:
            paraugs = f.readline().strip()
            teksts = f.readline().strip()
    return paraugs, teksts

# Izdrukāt rezultātus
def izdrukat_rezultatus(rezultati):
    print(' '.join(map(str, rezultati)))

# Aprēķināt vērtības
def hasot(virkne, pirmais, otro):
    h = 0
    for burts in reversed(virkne):
        h = (h * otro + ord(burts)) % pirmais
    return h

# Aprēķina vērtības pirms datu meklēšanas
def sagatavot_hasus(teksts, paraugs, pirmais, otro):
    garums_teksts, garums_paraugs = len(teksts), len(paraugs)
    hasi = [None] * (garums_teksts - garums_paraugs + 1)
    sakums = teksts[garums_teksts - garums_paraugs:]
    hasi[garums_teksts - garums_paraugs] = hasot(sakums, pirmais, otro)
    y = 1
    for i in range(1, garums_paraugs + 1):
        y = (y * otro) % pirmais
    for i in range(garums_teksts - garums_paraugs - 1, -1, -1):
        hasi[i] = (otro * hasi[i + 1] + ord(teksts[i]) - y * ord(teksts[i + garums_paraugs])) % pirmais
    return hasi

# Atgriezt meklēšanas rezultātus
def atrast_sakritibas(paraugs, teksts):
    pirmais = 10**9 + 7
    otro = 263
    parauga_has = hasot(paraugs, pirmais, otro)
    hasi = sagatavot_hasus(teksts, paraugs, pirmais, otro)
    sakritibas = [i for i in range(len(teksts) - len(paraugs) + 1) if parauga_has == hasi[i] and teksts[i:i+len(paraugs)] == paraugs]
    return sakritibas

if __name__ == '__main__':
    paraugs, teksts = ielas
