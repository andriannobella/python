from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga


'''
Encapsulation
'''
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

print('\n')

s1 = Segitiga(4, 2)
print(s1.info())
print(s1.hitung_luas())

'''
inheritance
'''
print('\nMencoba membuat objek dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())


'''
Polymorphism
'''
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
