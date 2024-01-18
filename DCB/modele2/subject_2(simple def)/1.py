def banana (a):
    if a%2==0:
        return "чётное"
    elif a%2!=0:
        return "нечётное"
print(banana(int(input("Введите число"))))