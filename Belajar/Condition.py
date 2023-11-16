# if elif else
nilai = int(input("berapa nilai anda ? "))

if(nilai >= 90):
    score = "A"
elif(nilai >= 80):
    score = "B"
elif(nilai >= 70):
    score = "C"
else:
    score = "D"

print(f"anda mendapatkan nilai {score}")

# match
match(score):
    case "A":
         print("nilai anda sangat baik")
    case "B":
        print("nilai anda cukup baik")
    case "C":
        print("nilai anda baik")
    case "D":
        print("nilai anda kurang baik")
    case _:
        print("maaf anda belum mendapatkan nilai")

# ternary operator
ucapan = "selamat anda lulus" if nilai > 70 else "maaf anda belum lulus"