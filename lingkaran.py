class lingkaran(object):
   def __init__(self, phi, r):
      self.phi= phi
      self.jarijari= r
   def hitungluaslingkaran(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   # membuat objek pertama
   lingkaran1 = lingkaran(3.14, 20)

   # menggunakan objek pertama
   print('Objek lingkaran1')
   print('phi\t: ', lingkaran1.phi)
   print('jarijari\t: ', lingkaran1.jarijari)
   print('luas\t= ', lingkaran1.hitungluaslingkaran())
   

   # membuat objek kedua
   lingkaran2 = lingkaran(3.14, 8)

   # menggunakan objek kedua
   print("Objek lingkaran2")
   print("phi\t: ", lingkaran2.phi)
   print("jarijari\t: ", lingkaran2.jarijari)
   print("luas\t= ", lingkaran2.hitungluaslingkaran())
   

if __name__ == "__main__":
   main()
