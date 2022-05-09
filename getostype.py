import platform
raw = open("Root file directory.fdir","r")
root = raw.read()
path = (root + "\OS Data")
versionpath = (root + "\Software data\ ")
raw.close()
print("\n")
print("working directory: ", root)

version = open(versionpath + "version.info","r")
version = version.read()

print("\n")
print("\n")
print("Protonmail unofficial client ",version," runing on:")

OST = platform.system()
OSTF = open(path + "\OStype.info","w")
OSTF.write(OST)
OSTF.close()
print(OST)

OSV = platform.release()
OSVF = open(path + "\OSversion.info","w")
OSVF.write(OSV)
OSVF.close()
print(OSV)

OSP = platform.platform()
OSPF = open(path + "\OSplatform.info","w")
OSPF.write(OSP)
OSPF.close()
print(OSP)
