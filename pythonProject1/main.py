#files(soubory), mode v domacim ukolu tabulka rozepsana


file = open("first_file.txt", "w")
file.write("test text")
file.close()

#pri cteni musi soubor existovat
file = open("first_file.txt")
data = file.read()
file.close()
print(data)

file = open("first_file.txt","a")
file.writelines("\ndruhy radek")
file.writelines("\ndruhy radek")
file.close()

file = open("first_file.txt")
data = file.read()
data2 = file.readlines()
file.close()
print(data)
print(data2)
# rozsyreni .me moze byt jaka chceme (.me to je priklad)
file = open("first_file.me", "w")
file.write("test text")
file.close()

#pri cteni musi soubor existovat
file = open("first_file.me")
data = file.read()
file.close()

print(data)

file = open("first_file.me","a")
file.writelines("\ndruhy radek")
file.writelines("\ndruhy radek")
file.close()

file = open("first_file.me")
data = file.read()
data2 = file.readlines()
file.close()
print(data)
print(data2)


print ("hello")