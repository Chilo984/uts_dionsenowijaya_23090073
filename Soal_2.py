def kabisat(tahun):
    if tahun % 400 == 0:
        return True
    if tahun % 4 == 0:
        return True
    else:
        return False
    
tahun = int(input('masukan tahun :'))
print("")

if kabisat(tahun):
    print(tahun,"meerupakan tahun kabisat")
else:
    print(tahun,"bukan tahun kabisat")