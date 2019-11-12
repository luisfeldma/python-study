from time import sleep
while True:
    n1 = int(input("Quer ver a tabuada de qual número? "))
    sleep(0.5)
    if n1 < 0:
        break
    print("--" * 20)
    for c in range(1, 11):
        print(f"""{n1} x {c} = {n1*c}""")
    print("--" * 20)
print("FIM")