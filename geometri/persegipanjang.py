class PersegiPanjang():
    def __init__(self, p, l):
        #fungsi yg dipanggil pertama kali
        self.p = p
        self.l = l

    def info(self):
        return f'ini adalah objek dari persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l

