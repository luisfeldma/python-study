a = int(input("Primeiro lado: "))
b = int(input("Segundo lado: "))
c = int(input("Terceiro lado: "))

if a + b > c and b + c > a and a + c > b :
    print("É possível formar um triângulo!")
    if a == b and a == c :
        print("Esse triângulo é equilátero.")
    elif a == b and a != c or a == c and a != b or b == c and b != a :
        print("Esse triângulo é isóceles.")
    elif a != b != c :  
        print("Esse triângulo é escaleno.")      
else:
    print("Não é possível formar um triângulo!")


