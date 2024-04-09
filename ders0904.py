# f = open("text0904.txt")

# f = open("text0904.txt", "r")
# print(f.read())

# f = open("C:/Users/user/Desktop/python/text0904.txt","r")
# print(f.read())

# f = open("text0904.txt", "r")
# print(f.read(10))

# f = open("text0904.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f = open("text0904.txt", "r")
# for x in f:
#   print(x)

# f = open("text0904.txt", "a")
# f.write("\nNow the file has more content!")
# f.close()

# f = open("text0904.txt", "r")
# print(f.read())

# f = open("text0904.txt", "w")
# f.write("\nWoops! I have deleted the content!")
# f.close()

# f = open("text0904.txt", "r")
# print(f.read())

## oluşturma
# f = open("text0904.txt", "w") sil
# print(f.write("\nHello World!"))
# f = open("text0904.txt", "a") append
# print(f.write("\nHello World!"))

# f = open("text0904.txt", "x") # yeni oluşturma varsa error
# print(f.write("\nHello World!"))

# with open("text0904.txt", "a") as f:
#     f.write("\nHello World!")
# f.write("\nHello World!2")

# import os
# os.remove("demofile.txt")

# import os
# if os.path.exists("demofile1.txt"):
#   os.remove("demofile1.txt")
# else:
#   print("The file does not exist")

# import os
# os.rmdir("myfolder")

f = open("text0904.txt", "x") # yeni oluşturma varsa error
print(f.write("\nHello World!"))