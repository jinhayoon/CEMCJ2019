#2019 J1
three_pointers_a = int(input(""))
two_pointers_a = int(input(""))
one_pointers_a = int(input(""))

three_pointers_b = int(input(""))
two_pointers_b = int(input(""))
one_pointers_b = int(input(""))

apples = three_pointers_a * 3 + two_pointers_a * 2 + one_pointers_a * 1
bananas = three_pointers_b * 3 + two_pointers_b * 2 + one_pointers_b * 1

if apples > bananas:
	print("A")
elif bananas > apples:
	print ("B")
else:
	print ("T")
