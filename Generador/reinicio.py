import os
fichero = open('programa.txt','r')
linea = fichero.readline()
fichero.close()
linea = linea.strip('\n')
fichero_sis = open('sistema.txt','r')
sistema = fichero_sis.readline()
fichero_sis.close()
sistema = sistema.strip('\n')
if sistema == 'W':
    os.system('ERASE programa.txt')
    os.system('ERASE sistema.txt')
elif sistema == 'L':
    os.system('rm programa.txt')
    os.system('rm sistema.txt')
os.system('python3 ' + linea)
