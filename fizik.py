import time

true = ["B", "betul", "Betul", "Ya", "ya"]
false = ["S", "salah", "Salah", "Tidak", "tidak"]
answerq1 = ["Nukleus yang berat", "nukleus yang berat", "berat", "Berat"]
answerq3 = ["haba", "Haba"]
answerq4 = ["satu", "Satu", "1"]
answerq7 = ["banyak neutron yang dihasilkan dan tenaga yang banyak dibebaskan"]
answerq11 = ["percantuman nukleus", "Percantuman nukleus"]
answerq13 = ["kehilangan jisim", "Kehilangan jisim"]
answerq14 = ["lebih besar", ">"]
answerq15 = ["tenaga"]
answerq17 = ["menjana tenaga eletrik melalui proses pembelahan nukleus"]
answerq18 = ["mendidihkan air untuk menjadi stim pada tekanan yang tinggi"]
answerq19 = ["1,2,4", "1,2 dan 4"]
answerq20 = ["2,3,4", "2,3 dan 4"]
answerq21 = ["1,2,3", "1,2 dan 3"]
correct = 0

print(" _____ ___ ________ _  _______ ____  ____ ____  _  _   ")
print("|  ___|_ _|__  /_ _| |/ /_   _| ___|| __ ) ___|| || |  ")
print("| |_   | |  / / | || ' /  | | |___ \|  _ \___ \| || |_ ")
print("|  _|  | | / /_ | || . \  | |  ___) | |_) |__) |__   _|")
print("|_|   |___/____|___|_|\_\ |_| |____/|____/____(_) |_|  ")
print("Coded by Syafiqlim")
name = input("\nApakah nama anda?\n>>>")

print("\nOK, " + name + ", mari mulakan kuiz! Jawapan hendaklah dalam ejaan yang betul.")
time.sleep(1)

print("\n1.Nukleus yang ringan ataupun berat yang terlibat dalam pembelahan nukleus?")
choice = input("=> ")
if choice in answerq1:
    correct += 1
else:
    correct += 0

print("\n2.Adakah nukleus berat dipecahkan kepada dua nukleus yang lebih ringan?")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n3. Apakah bentuk tenaga nuklear yang dibebaskan?")
choice = input(": ")
if choice in answerq3:
    correct += 1
else:
    correct += 0

print("\n4. Berapakah neutron yang menghentam Uranium-235 supaya menjadi tidak stabil dan berlakunya pembelahan nukleus?")
choice = input("= ")
if choice in answerq4:
    correct += 1
else:
    correct += 0

print("\n5. Adakah hanya satu neutron yang dihasilkan selepas proses pembelahan nukleus Uranium-235?")
choice = input(">: ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n6. Adakah tindak balas berantai tidak mendorong untuk tindak balas seterusnya untuk berlaku?")
choice = input(":- ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n7. Apakah yang menyebabkan tindak balas berantai berlaku?")
choice = input("=> ")
if choice in answerq7:
    correct += 1
else:
    correct += 0

print("\n8. Adakah tindak balas berantai hanya berlaku jika jisim sampel uraninium melebihi jisim genting?")
choice = input("> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n9. Adakah pembelahan atom uranium membebaskan tenaga yang sangat banyak?")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n10. Adakah tindak balas yang terkawal digunakan dalam letupan bom atom?")
choice = input(">> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n11. Pelakuran nuklear ialah percantuman nukleus ataupun pemecahan nukleus?")
choice = input("= ")
if choice in answerq11:
    correct += 1
else:
    correct += 0

print("\n12. Adakah pelakuran nukleus membebaskan tenaga yang besar?")
choice = input(">> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n13. Daripada manakah punca tenaga yang dibebaskan ini datang?")
choice = input("==> ")
if choice in answerq13:
    correct += 1
else:
    correct += 0

print("\n14. Jumlah jisim sebelum tindak lebih besar/lebih kecil berbanding jumlah jisim hasil tindak balas.")
choice = input("= ")
if choice in answerq14:
    correct += 1
else:
    correct += 0

print("\n15. Kehilangan jisim dalam tindak balas nuklear menyebabkan ia bertukar menjadi?")
choice = input(">> ")
if choice in answerq15:
    correct += 1
else:
    correct += 0

print("\n16. Adakah persamaan yang digunakan untuk mengira tenaga yang dibebaskan dalam tindak balas nuklear ialah KE=1/2mv^2?")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n17. Apakah fungsi reaktor nuklear")
choice = input("= ")
if choice in answerq17:
    correct += 1
else:
    correct += 0

print("\n18. Selepas proses pembelahan nukleus di dalam reaktor nuklear, tenaga haba yang dibebaskan berfungsi sebagai apa?")
choice = input("=> ")
if choice in answerq18:
    correct += 1
else:
    correct += 0

print("\n19. Yang manakah kebaikan penggunaan tenaga nuklear?")
time.sleep(1)
print("\n1. Kuantiti bahan api nuklear yang kecil dapat mengeluarkan kuantiti tenaga yang besar.")
time.sleep(1)
print("2. Tiada kesan rumah hijau jika menggunakan tenaga nuklear.")
time.sleep(1)
print("3. Kos yang mudah untuk memibna stesen kuasa nuklear.")
time.sleep(1)
print("4. Sumber semula jadi bahan api nukelar masih wujud dalam kuantiti yang besar.")
choice = input(">>")
if choice in answerq19:
    correct += 1
else:
    correct += 0

print("\n20. Yang manakah keburukan penggunaan tenaga nuklear?")
time.sleep(1)
print("\n1. Kuantiti penghasilan tenaga yang kecil.")
time.sleep(1)
print("2. Kos membina dan menyiapkan stesen kuasa nuklear adalah sangat tinggi.")
time.sleep(1)
print("3. Pekerja di stesen nuklear didedahkan kepada sinaran radioaktif.")
time.sleep(1)
print("4. Pemantauan yang berterusan dan rapi perlu sentiasa dilaksanakan.")
choice = input(">> ")
if choice in answerq20:
    correct += 1
else:
    correct += 0

print("\n21. Yang manakah kesan negatif bahan radioaktif?")
time.sleep(1)
print("\n1. Sinaran radioaktif boleh menyebabkan kerosakan sel-sel hidup dan menjadi sel kanser.")
time.sleep(1)
print("2. Menyebabkan kesan segera seperti letih, loya juga kesan tertunda seperti kerosakan organ dan kanser")
time.sleep(1)
print("3. Menyebabkan kesan genetik seperti kecacatan bayi dan kromosom tidak normal")
time.sleep(1)
print("4. Menyebabkan seseorang berasa terlebih bersemangat.")
choice = input(">> ")
if choice in answerq21:
    correct += 1
else:
    correct += 0

print("\nKUIZ TAMAT! TERIMA KASIH KERANA MENJAWAB KUIZ INI. " + name + ", Anda dapat", correct, "daripada 21.")
