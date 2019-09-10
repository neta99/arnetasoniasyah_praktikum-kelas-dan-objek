class lingkaran(object):
   def __init__(self, phi, r):
      self.phi= phi
      self.jarijari= r
   def hitungkelilinglingkaran(self):
      return 2 * self.phi * self.jarijari 

def main():
   # membuat objek pertama
   keliling1 = lingkaran(3.14, 10)

   # menggunakan objek pertama
   print('Objek keliling1')
   print('phi\t: ', keliling1.phi)
   print('jarijari\t: ', keliling1.jarijari)
   print('keliling\t= ', keliling1.hitungkelilinglingkaran())
   

   # membuat objek kedua
   keliling2 = lingkaran(3.14, 5)

   # menggunakan objek kedua
   print("Objek keliling2")
   print("phi\t: ", keliling2.phi)
   print("jarijari\t: ", keliling2.jarijari)
   print("keliling\t= ", keliling2.hitungkelilinglingkaran())
   

if __name__ == "__main__":
   main()
