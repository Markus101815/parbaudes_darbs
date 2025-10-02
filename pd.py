vards = "Markus"
vecums1 = 15
print(f"Mani sauc {vards} un man ir {vecums1} gadi.")

skaitlis1 = int(input("Ievadiet, lūdzu, jebkuru veselu skaitli! "))
skaitlis2 = int(input("Ievadiet, lūdzu, vēl vienu veselu skaitli! "))
print(f"Šo skaitļu summa ir {skaitlis1 + skaitlis2}.")

skaitlis3 = int(input("Ievadiet, lūdzu, jebkuru veselu skaitli! "))
if skaitlis3 % 2 == 0:
    print("Skaitlis ir pāra.")
else:
    print("Skaitlis ir nepāra.")

skaitlis4 = int(input("Ievadiet, lūdzu, jebkuru veselu skaitli! "))
if skaitlis4 > 0:
    print("Skaitlis ir pozitīvs.")
elif skaitlis4 < 0:
    print("Skaitlis ir negatīvs.")
else:
    print("Skaitlis ir nulle.")

vecums2 = int(input("Ievadiet, lūdzu, savu vecumu! "))
if vecums2 >= 18:
    print("Jūs esat pilngadīgs.")
else:
    print("Jūs esat nepilngadīgs.")

skaitlis5 = int(input("Ievadiet, lūdzu, jebkuru veselu skaitli! "))
if skaitlis5 >= 10 and skaitlis5 <= 20:
    print("Šis skaitlis atrodas starp 10 un 20.")
else:
    print("Šis skaitlis neatrodas starp 10 un 20.")

i = 1
for i in range(10):
    i = i + 1
    print(i)