stream = open("versiontool.py")
read_file = stream.read()
exec(read_file)

stream = open("getroot.py")
read_file = stream.read()
exec(read_file)

stream = open("getostype.py")
read_file = stream.read()
exec(read_file)


print("\n")
print("\n")

document = open("legal.txt","r")
legal = document.read()
document.close()

print(legal)


stream = open("Windowmain.py")
read_file = stream.read()
exec(read_file)



