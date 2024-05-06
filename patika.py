import math

def mesafe_hesapla(nokta1, nokta2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Argümanlar:
    nokta1: (x1, y1) şeklinde bir demet olan ilk nokta.
    nokta2: (x2, y2) şeklinde bir demet olan ikinci nokta.

  Dönüş Değeri:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = nokta1
  x2, y2 = nokta2
  kare_fark_toplami = (x2 - x1) ** 2 + (y2 - y1) ** 2
  mesafe = math.sqrt(kare_fark_toplami)
  return mesafe

def ana_fonksiyon():
  """
  Ana fonksiyon. Noktaları tanımlar, mesafeleri hesaplar ve minimum mesafeyi bulur.
  """
  noktalar = [
    (1, 2),
    (4, 5),
    (7, 8),
    (3, 1),
  ]

  mesafeler = []
  for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
      mesafe = mesafe_hesapla(noktalar[i], noktalar[j])
      mesafeler.append(mesafe)

  minimum_mesafe = min(mesafeler)

  print("Minimum mesafe:", minimum_mesafe)

if __name__ == "__main__":
  ana_fonksiyon()
