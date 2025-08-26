a = float(input("Masukan nombor pertama:"))
b = float(input("Masukan nombor kedua:"))
op = input("Masukkan operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print( a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Error: Nombor Tidak bisa di bahagi 0")
    else:
        print("hasil =", a / b)
else:
    print("Operator Tidak di kenal")
