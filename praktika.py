
"""
# task 1

i = int(input("eded daxil edin"))
j = 1
while j < i:
  j += 1
  hasil = j * i
  print(hasil)
else:
  print("dayan")
  """
"""
# task 3

i = 0
while (i < 10) :
    if not i %2 :
        i = i + 1 # örneğin bu satır olmaz ise döngü bitmez. (sonsuzdöngü/hatalı kod önleme).
        continue
    print("tek ededler",i)
    i = i + 1
    """
# task 2 
	
vurulan = 1

while vurulan <= 10:
	vuran = 1
	while vuran <= 10:
		hasil = vurulan * vuran
		print(vurulan, "x", vuran, "=", hasil, end="\t")
		vuran += 1
	print()
	vurulan += 1