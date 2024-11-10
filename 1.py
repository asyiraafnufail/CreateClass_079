class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling (self,panjang,lebar):
        if self.panjang >= 0 or self.lebar >= 0 :
            2* (self.panjang + self.lebar)
        else :
            return

    def luas (self,panjang,lebar):    
        return (self.panjang * self.lebar)
    
    def __str__ (self):
        return f"persegi panjang, panjang {self.panjang}cm , dan lebar {self.lebar} cm"

def main():
    try:
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        
        # if panjang <= 0 or lebar <= 0:
        #     print("Nilai harus diatas 0")
        #     return

        pp = PersegiPanjang(panjang, lebar)
        print(pp)
        print("Kelilingnya: ", pp.keliling(panjang,lebar), "cm")
        print("Luasnya: ", pp.luas(panjang,lebar), "cm2")
    
    except ValueError:
        print("Nilai harus sesuai")

main()