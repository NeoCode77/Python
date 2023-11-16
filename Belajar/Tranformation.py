text1 = "hello world"
text2 = "HELLO WORLD"

# tranformasi dari huruf kecil sampai besar
print(text1.upper())

# tranformasi dari huruf besar ke kecil
print(text2.lower())

text3 = "     hello     "

# menghilangkan whitespace di kanan dan kiri 
print(text3.strip())

# menghilangkan whitespace di kanan
print(text3.rstrip())

# menghilangkan whitespace di kiri
print(text3.lstrip())

# menentukan awalan text
print(text1.startswith("hello"))
print(text1.startswith("bye"))

# menentukan akhiran text
print(text1.endswith("world"))

# menggambungkan array menjadi string
arr1 = ["aku","makan","nasi"]
pemisah = " "
print(pemisah.join(arr1))

# memisahkan string mejadi array
text4 = "aku minum air"
print(text4.split(pemisah))

# mengganti kata dalam string
print(text4.replace("minum","makan"))

x = "dicoding"
x[0] = "f"
print(x)
