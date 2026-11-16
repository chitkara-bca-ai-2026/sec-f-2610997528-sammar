tui=int(input("Enter tuition fee:-"))
lab=int(input("Enter lab fee:-"))
lib=int(input("Enter library fee:-"))
exam=int(input("Enter exam fee:-"))
dis=int(input("Enter discount amount:-"))

total=(tui+lab+lib+exam)
after=(total-dis)
anual=after*2
mnth=anual/12

print(f"Tuition Fee: {tui:.1f}")
print(f"Lab Fee: {lab:.1f}")
print(f"Library Fee: {lib:.1f}")
print(f"Exam Fee: {exam:.1f}")
print(f"Total Fee: {total:.1f}")
print(f"Discount: {dis:.1f}")
print(f"Fee after discount: {after:.1f}")
print(f"Anual Fee: {anual:.1f}")
print(f"Monthly Installment: {mnth:.2f}")