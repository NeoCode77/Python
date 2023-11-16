# # idential error 
# if x == 20:
# print("hello world")

# # syntax error
# i = 0
# while i < 10
#     print(i)
#     i+=1

# # NameError
# print(i)

# # TypeError
# x = "2"
# z = x + 2

# # ZeroDevisionError
# x = 6/0
# print(x)

try:
    i = None
    print(i)
except Exception:
    print("kode anda salah")
else:
    print("kode anda berhasil")
finally:
    print("kode selesai")

if i is None:
    raise Exception("i adalah kosong")
else:
    print("i tidak kosong")