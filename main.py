20-misol
def ism_tekshir(ism):
    if ism and ism[0].isupper():
        return "To‘g‘ri yozilgan"
    else:
        return "Ism noto‘g‘ri yozilgan"

user_ism = input("Ismingizni kiriting: ")
natija = ism_tekshir(user_ism)
print(natija)


#21-misol
def baho_tekshir(baho):
    if 90 <= baho <= 100:
        return "A"
    elif 70 <= baho <= 89:
        return "B"
    elif 50 <= baho <= 69:
        return "C"
    else:
        return "Yiqildi"


user_baho = int(input("Bahoni kiriting: "))
natija = baho_tekshir(user_baho)
print(natija)
