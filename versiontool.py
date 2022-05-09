raw = open("Root file directory.fdir","r")
root = raw.read()
path = (root + "\Software data\ ")

version = ("1.0")

softwareV = open(path + "version.info","w")
softwareV.write(version)
softwareV.close()
