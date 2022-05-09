#-------change this----------------
version = ("1.2 Beta")
#----------------------------------

raw = open("Root file directory.fdir","r")
root = raw.read()
path = (root + "\Software data\ ")

softwareV = open(path + "version.info","w")
softwareV.write(version)
softwareV.close()
