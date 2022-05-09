import os 
cwd = os.getcwd() 
root = open("Root file directory.fdir","w")
root.write(cwd)
root.close()
