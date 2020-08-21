#****************************************************************************************************************************************************
#
#   Definición de clases y funciones, las funciones se dividen en funciones de ficheros y de procesado de texto, la
#   definición de la clase contiene un dato de nombre y un vector de preguntas. Se trabaja con la codificación UTF-8.
#
#****************************************************************************************************************************************************

class Cuestionario:

    titulo = ''
    autor = ''
    fecha = ''
    secciones = []
    preguntas = []
    separacion = [False, False]
    linea_alumno = False
    linea_grupo = False
    instrucciones = False
    texto_instrucciones = ''

    def modificarTitulo(self, titulo_leido):
        self.titulo = titulo_leido
    
    def modificarAutor(self, autor_leido):
        self.autor = autor_leido

    def modificarFecha(self, fecha_leida):
        self.fecha = fecha_leida

    def modificarSecciones(self, seccion_leida):
        self.secciones.append(seccion_leida)

    def modificarPreguntas(self, vector_preguntas):
        self.preguntas.append(vector_preguntas)

    def modificarSeparacion(self, opcion_leida):
        self.separacion = opcion_leida

    def modificarLineaAlumno(self, opcion_leida):
        self.linea_alumno = opcion_leida

    def modificarLineaGrupo(self, opcion_leida):
        self.linea_grupo = opcion_leida

    def modificarInstrucciones(self, opcion_leida):
        self.instrucciones = opcion_leida

    def modificarTextoInstrucciones(self, texto_leido):
        self.texto_instrucciones = texto_leido

#    Funciones de ficheros
def crear_fichero(nombre_fichero):
    fichero = open(nombre_fichero, 'w')
    fichero.close()

def escribir_linea(nombre_fichero, dato):
    fichero = open(nombre_fichero, 'a')
    fichero.write(dato + '\n')
    fichero.close()

def leer_linea(nombre_fichero):
    fichero = open(nombre_fichero, 'r')
    linea = fichero.readline()
    fichero.close()
    return linea

def leer_fichero(nombre_fichero):
    vector = []
    fichero = open(nombre_fichero, 'r')
    lectura = fichero.readline()
    vector.append(lectura)
    while lectura != '':
        lectura = fichero.readline()        
        vector.append(lectura)    
    fichero.close()
    return vector

#    Funciones de revision y captura
def revisar_numero(dato, mensaje_error):
    diccionario_numeros = {
        'cero':'0',
        'uno':'1',
        'una':'1',
        'dos':'2',
        'tres':'3',
        'cuatro':'4',
        'cinco':'5',
        'seis':'6',
        'siete':'7',
        'ocho':'8',
        'nueve':'9',
        'diez':'10',
        'once':'11',
        'doce':'12',
        'trece':'13',
        'catorce':'14',
        'quince':'15',
        'dieciséis':'16',
        'dieciseis':'16',
        'diecisiete':'17',
        'dieciocho':'18',
        'diecinueve':'19',
        'veinte':'20',
        'veintiuno':'21',
        'veintidós':'22',
        'veintidos':'22',
        'veintitrés':'23',
        'veintitres':'23',
        'veinticuatro':'24',
        'veinticinco':'25',
        'veintiséis':'26',
        'veintiseis':'26',
        'veintisiete':'27',
        'veintiocho':'28',
        'veintinueve':'29',
        'treinta':'30'
    }
    dato = dato.strip()
    dato = dato.lower()
    claves = diccionario_numeros.keys()
    if dato.isalpha() == True:
        for elemento in claves:
            if elemento == dato:
                dato = diccionario_numeros[dato]
    if dato.isdigit() != True:
        print(mensaje_error)
    return dato

def procesar_pregunta(dato):    
    dato = dato.strip()
    x = True
    y = True
    z = False
    if (dato[len(dato) - 2:len(dato)] == '-?' or dato[len(dato) - 2:len(dato)] == '-¿'):
        x = False
        dato = dato[0:len(dato) - 2]
        dato = dato.strip()
        if dato[len(dato) - 1] == '!':
            if dato[0] == '¡':
                z = True
            if ('¡' in dato) != True:
                z = True
    if dato[0] == '+' and dato[1].lower() == 'm':
        y = False
        dato = dato[2:len(dato)]
        dato = dato.strip()
        contador = 0
        for indice in range(len(dato)):
            if dato[indice].isalpha() == True:
                contador = indice                
                break
        letra = dato[contador]
        if x == True:
            if '¡' in dato[0:contador]:
                z = True
        dato = dato[contador + 1:len(dato)]
        dato = letra.upper() + dato
    if (x == False) and (z == True):
        if y == False:
            if dato[0] != '¡':
                dato = '¡' + dato
        else:
            if dato[0] != '¡':
                dato = dato.capitalize()
                dato = '¡' + dato
            else:
                dato = dato[1:len(dato)]
                dato = dato.capitalize()
                dato = '¡' + dato
    if (x == False) and (z == False):
        if y == True:
            dato = dato.capitalize()
        if dato[len(dato) - 1] != '.':
            dato = dato + '.'
    if (x == True) and (y == False):
        if dato[len(dato) - 1] == '¿':
            dato = dato[0:len(dato) - 1] + '?'
        elif dato[len(dato) - 1] != '?':
            dato = dato + '?'
        dato = '¿' + dato
    if (x == True) and (y == True):
        if dato[len(dato) - 1] == '¿':
            dato = dato[0:len(dato) - 1] + '?'
        elif dato[len(dato) - 1] != '?':
            dato = dato + '?'
        dato = '¿' + dato.capitalize()
    return dato

def capturar_pregunta(mensaje, mensaje_error):
    aux_a = cad2 + cads + "\u001b[33m    Esta pregunta es:                                                     \u001b[32m|\u001b[37m\n"
    aux_b = cad2 + cads + "       1) Respuesta Libre.                                                \u001b[32m|\u001b[37m\n"
    aux_c = cad2 + cads + "       2) Opción Múltiple.                                                \u001b[32m|\u001b[37m\n"
    aux_d = cad2 + cads + "       3) Verdadero/Falso.                                                \u001b[32m|\u001b[37m\n"
    aux_e = cad2 + cads + "       4) Relacionar columnas.                                            \u001b[32m|\u001b[37m\n"
    aux_f = cad2 + cads + "       5) Sopa de letras.                                                 \u001b[32m|\u001b[37m\n"
    aux_g = cad2 + cads + "                         \u001b[32m>>\u001b[37m  "
    pregunta = input(mensaje)
    pregunta = procesar_pregunta(pregunta)
    opcion = input(aux_a + aux_b + aux_c + aux_d + aux_e + aux_f + aux_g)
    opcion = revisar_numero(opcion, mensaje_error)
    verificar_opcion = True
    if opcion.isdigit() != True:
        verificar_opcion = False
    if opcion.isdigit() == True:
        if not int(opcion) in range(1, 6):
            verificar_opcion = False
    while verificar_opcion != True:
        opcion = input(aux_a + aux_b + aux_c + aux_d + aux_e + aux_f + aux_g)
        opcion = revisar_numero(opcion, mensaje_error)
        verificar_opcion = True
        if opcion.isdigit() != True:
            verificar_opcion = False
        if opcion.isdigit() == True:
            if not int(opcion) in range(1, 6):
                verificar_opcion = False
    if opcion == '1':
        mensaje_uno = cad2 + cads + "    \u001b[36mIntroduce el número de renglones en blanco: \u001b[37m"
        pregunta_atributo = input(mensaje_uno)
        pregunta_atributo = revisar_numero(pregunta_atributo, mensaje_error)
        while pregunta_atributo.isdigit() != True:
            pregunta_atributo = input(mensaje_uno)
            pregunta_atributo = revisar_numero(pregunta_atributo, mensaje_error)
        if pregunta_atributo == '0':
            pregunta_atributo = '1'
    elif opcion == '2':
        mensaje_dos = cad2 + cads + "    \u001b[36mIntroduce el número de incisos: \u001b[37m"
        numero_incisos = input(mensaje_dos)
        numero_incisos = revisar_numero(numero_incisos, mensaje_error)
        while numero_incisos.isdigit() != True:
            numero_incisos = input(mensaje_dos)
            numero_incisos = revisar_numero(numero_incisos, mensaje_error)
        while numero_incisos == '0':
            print(mensaje_error)
            numero_incisos = input(mensaje_dos)
            numero_incisos = revisar_numero(numero_incisos, mensaje_error)
        numero_incisos = int(numero_incisos)
        pregunta_atributo = []
        for i in range(numero_incisos):
            inciso = input(cad2 + cads + "       Introduce el inciso " + alfabeto[i] + "): ")
            inciso = inciso.strip() 
            letra = inciso[0]
            inciso = inciso[1:len(inciso)]
            inciso = letra.upper() + inciso
            pregunta_atributo.append(inciso)
    elif opcion == '3':
        mensaje_tres = cad2 + cads + "    \u001b[36mPregunta con respuesta Verdadero o Falso.                             \u001b[32m|\u001b[37m"
        print(mensaje_tres)
        pregunta_atributo = 'VF'
    elif opcion == '4':
        mensaje_cuatro_uno = cad2 + cads + "    \u001b[36mIngresa el número de renglones en la primer columna: \u001b[37m"
        mensaje_cuatro_dos = cad2 + cads + "    \u001b[36mIngresa el número de renglones en la segunda columna: \u001b[37m"
        columna_uno = []
        columna_dos = []
        numero_columna_uno = input(mensaje_cuatro_uno)
        numero_columna_uno = revisar_numero(numero_columna_uno, mensaje_error)
        while numero_columna_uno.isdigit() != True:
            numero_columna_uno = input(mensaje_cuatro_uno)
            numero_columna_uno = revisar_numero(numero_columna_uno, mensaje_error)
        while numero_columna_uno == '0':
            print(mensaje_error)
            numero_columna_uno = input(mensaje_cuatro_uno)
            numero_columna_uno = revisar_numero(numero_columna_uno, mensaje_error)
        numero_columna_dos = input(mensaje_cuatro_dos)
        numero_columna_dos = revisar_numero(numero_columna_dos, mensaje_error)
        while numero_columna_dos.isdigit() != True:
            numero_columna_dos = input(mensaje_cuatro_dos)
            numero_columna_dos = revisar_numero(numero_columna_dos, mensaje_error)
        while numero_columna_dos == '0':
            print(mensaje_error)
            numero_columna_dos = input(mensaje_cuatro_dos)
            numero_columna_dos = revisar_numero(numero_columna_dos, mensaje_error)
        print(cad2 + cads + "    \u001b[36mIngresa la primer columna:                                            \u001b[32m|\u001b[37m")
        for i in range(int(numero_columna_uno)):
            x = input(cad2 + cads + "    \u001b[36m   " + str(i + 1) + "): \u001b[37m")
            x = x.strip()
            x = x.capitalize()
            columna_uno.append(str(i + 1) + ") " + x)
        print(cad2 + cads + "    \u001b[36mIngresa la segunda columna:                                           \u001b[32m|\u001b[37m")
        for j in range(int(numero_columna_dos)):
            y = input(cad2 + cads + "    \u001b[36m   " + alfabeto[j] + "): \u001b[37m")
            y = y.strip()
            y = y.capitalize()
            columna_dos.append(alfabeto[j] + ") " + y)
        pregunta_atributo = [columna_uno, columna_dos]
    elif opcion == '5':
        mensaje_cinco_uno = cad2 + cads + "    \u001b[36mIngresa el número de renglones de la sopa de letras: \u001b[37m"
        mensaje_cinco_dos = cad2 + cads + "    \u001b[36mIngresa el número de columnas de la sopa de letras: \u001b[37m"
        matriz = []
        numero_renglones = input(mensaje_cinco_uno)
        numero_renglones = revisar_numero(numero_renglones, mensaje_error)        
        while numero_renglones.isdigit() != True:
            numero_renglones = input(mensaje_cinco_uno)
            numero_renglones = revisar_numero(numero_renglones, mensaje_error)
        while numero_renglones == '0':
            print(mensaje_error)
            numero_renglones = input(mensaje_cinco_uno)
            numero_renglones = revisar_numero(numero_renglones, mensaje_error)            
        numero_columnas = input(mensaje_cinco_dos)
        numero_columnas = revisar_numero(numero_columnas, mensaje_error)        
        while numero_columnas.isdigit() != True:
            numero_columnas = input(mensaje_cinco_dos)
            numero_columnas = revisar_numero(numero_columnas, mensaje_error)
        while numero_columnas == '0':
            print(mensaje_error)
            numero_columnas = input(mensaje_cinco_dos)
            numero_columnas = revisar_numero(numero_columnas, mensaje_error)
        for i in range(int(numero_renglones)):
            print(cad2 + cads + "    \u001b[33m  Ingresa el renglón " + str(i + 1) + " de la sopa de letras: \u001b[37m")
            x = []
            for j in range(int(numero_columnas)):
                verificar_digito = True
                y = input(cad2 + cads + "    \u001b[36m    Ingresa la letra " + str(j + 1) + ": \u001b[37m")
                if len(y) != 1:
                    verificar_digito = False
                    print(cad2 + cads + "    \u001b[31m    Debes ingresar una letra.                                         \u001b[32m|\u001b[37m")
                elif y.isalpha() != True:
                    verificar_digito = False
                    print(cad2 + cads + "    \u001b[31m    Debes ingresar una letra.                                         \u001b[32m|\u001b[37m")
                while verificar_digito != True:
                    verificar_digito = True
                    y = input(cad2 + cads + "    \u001b[36m    Ingresa la letra " + str(j + 1) + ": \u001b[37m")
                    if len(y) != 1:
                        verificar_digito = False
                        print(cad2 + cads + "    \u001b[31m    Debes ingresar una letra.                                         \u001b[32m|\u001b[37m")
                    elif y.isalpha() != True:
                        verificar_digito = False
                        print(cad2 + cads + "    \u001b[31m    Debes ingresar una letra.                                         \u001b[32m|\u001b[37m")
                x.append(y)
            matriz.append(x)
        pregunta_atributo = matriz
    return [pregunta, opcion, pregunta_atributo]

def capturar_preguntas(secciones, mensaje_error):
    for elemento in secciones:
        preguntas_seccion = []
        print(cad2 + cads + "\u001b[35mSección " + elemento + "\u001b[37m")
        mensaje_seccion = cad2 + cads + "  Introduce el número de preguntas de la sección " + elemento + ": "
        numero_preguntas = input(mensaje_seccion)
        numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)        
        while numero_preguntas.isdigit() != True:
            numero_preguntas = input(mensaje_seccion)
            numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)
        while numero_preguntas == '0':
            print(mensaje_error)
            numero_preguntas = input(mensaje_seccion)
            numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)
        print(cad2 + cads + "  \u001b[36mIntroduce las preguntas.                                                \u001b[32m|\u001b[37m")
        for i in range(int(numero_preguntas)):
            mensaje = cad2 + cads + "    \u001b[33m" + elemento + " pregunta " + str(i + 1) + ": \u001b[37m"
            pregunta = capturar_pregunta(mensaje, mensaje_error)
            preguntas_seccion.append(pregunta)
        cuestionario.modificarPreguntas(preguntas_seccion)

def verificar_fecha(dato, mensaje_error):
    valor = True
    x = dato.strip()
    x = x.replace('.',' ')
    x = x.replace(',',' ')
    x = x.replace(';',' ')
    x = x.replace(':',' ')
    x = x.replace('-',' ')
    x = x.replace('_',' ')
    x = x.replace('/',' ')
    x = x.replace('\\',' ')
    x = x.replace('=',' ')
    x = x.replace('%',' ')
    x = x.replace('&',' ')
    x = x.replace('#',' ')
    x = x.replace('?',' ')
    x = x.replace('¿',' ')
    x = x.replace('!',' ')
    x = x.replace('¡',' ')
    x = x.replace('|',' ')
    x = x.replace('¬',' ')
    if (len(x) > 10 or len(x) < 8):
        valor = False
    elif ((x.isalnum() == True) or (x.isalpha() == True)):
        valor = False
    else:
        y = x.split(' ')
        for i in range(len(y)):
            y[i] = int(y[i])
        if y[0] > 31 or y[0] < 1:
            valor = False
        elif y[1] > 12 or y[1] < 1:
            valor = False
        elif y[2] > 2030 or y[2] < 1900:
            valor = False
    if valor == False:
        mensaje = "\u001b[37m    Vuelve a intentar (dia-mes-año).                                      \u001b[32m|\u001b[37m"
        print(cad2 + cads + mensaje_error + cad2 + cads + mensaje)
    return valor

def procesar_fecha(dato):
    diccionario_mes = {
        '1':'Enero',
        '2':'Febrero',
        '3':'Marzo',
        '4':'Abril',
        '5':'Mayo',
        '6':'Junio',
        '7':'Julio',
        '8':'Agosto',
        '9':'Septiembre',
        '10':'Octubre',
        '11':'Noviembre',
        '12':'Diciembre'
    }
    x = dato.strip()
    x = x.replace('.', ' ')
    x = x.replace(',', ' ')
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('-', ' ')
    x = x.replace('_', ' ')
    x = x.replace('/', ' ')
    x = x.replace('\\', ' ')
    x = x.replace('=', ' ')
    x = x.replace('%', ' ')
    x = x.replace('&', ' ')
    x = x.replace('#', ' ')
    x = x.replace('?', ' ')
    x = x.replace('¿', ' ')
    x = x.replace('!', ' ')
    x = x.replace('¡', ' ')
    x = x.replace('|', ' ')
    x = x.replace('¬', ' ')
    y = x.split(' ')
    dia = y[0]
    if dia [0] == '0':
        dia = dia.replace('0', ' ')
        dia = dia.strip()
    mes = y[1]
    if mes[0] == '0':
        mes = mes.replace('0', ' ')
        mes = mes.strip()
    anio = y[2]
    mes = diccionario_mes[mes]
    f = dia + ' de ' + mes + ' de ' + anio
    return f

#    Funciones de escritura en pantalla
def reinicio(dato):
    crear_fichero('programa.txt')
    escribir_linea('programa.txt', 'generador.py')
    crear_fichero('sistema.txt')
    escribir_linea('sistema.txt', dato)
    os.system('python3 reinicio.py')

def limpiar_pantalla(dato):
    if dato == 'W':
        os.system('CLS')
    elif dato == 'L':
        os.system('clear')

def presentar_preguntas():
    print(cad2 + cad2 + cad1 + cad2 + cads + "\u001b[34mLos datos del documento son son:                                          \u001b[32m|\u001b[37m")
    print(cad2 + cads + "  Nombre del cuestionario: \u001b[33m" + cuestionario.titulo + "\u001b[37m")
    print(cad2 + cads + "  Nombre del autor:        \u001b[33m" + cuestionario.autor + "\u001b[37m")
    print(cad2 + cads + "  Fecha:                   \u001b[33m" + cuestionario.fecha + "\u001b[37m")
    if cuestionario.linea_alumno == True:
        print(cad2 + cads + "\u001b[36m  Nombre:                                                                 \u001b[32m|\u001b[37m")
    if cuestionario.linea_grupo == True:
        print(cad2 + cads + "\u001b[36m  Grupo:                                                                  \u001b[32m|\u001b[37m")
    if cuestionario.instrucciones == True:
        print(cad2 + cads + "\u001b[36m  Instrucciones: \u001b[37m" + cuestionario.texto_instrucciones)
    if cuestionario.separacion == [True, True]:
        print(cad2 + cads + "\u001b[36m  Cada sección junto con la portada van en hojas separadas.               \u001b[32m|\u001b[37m")
    elif cuestionario.separacion == [True, False]:
        print(cad2 + cads + "\u001b[36m  Cada sección sin tomar en cuenta la portada van en hojas separadas.     \u001b[32m|\u001b[37m")
    elif cuestionario.separacion == [False, False]:
        print(cad2 + cads + "\u001b[36m  Ni la portada ni las secciones están separadas.                         \u001b[32m|\u001b[37m")
    elif cuestionario.separacion == [False, True]:
        print(cad2 + cads + "\u001b[36m  La portada va en una hoja separada, pero las secciones no.              \u001b[32m|\u001b[37m")
    print(cad2 + cad2 + cads + "\u001b[34mLas preguntas introducidas son:                                           \u001b[32m|\u001b[37m")
    for i in range(len(cuestionario.secciones)):
        print(cad2 + cad2 + cads + "  \u001b[35m" + cuestionario.secciones[i] + "\u001b[37m")
        for j in range(len(cuestionario.preguntas[i])):
            print(cad2 + cads + "    \u001b[32m" + str(j + 1) + " .-" + cuestionario.preguntas[i][j][0] + "\u001b[37m")
            if cuestionario.preguntas[i][j][1] == '1':
                print(cad2 + cads + "    \u001b[36m  Pregunta con \u001b[33m" + str(cuestionario.preguntas[i][j][2]) + " espacios \u001b[36men blanco para la respuesta.\u001b[37m")
            elif cuestionario.preguntas[i][j][1] == '2':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con los siguietes incisos:                 \u001b[32m|\u001b[37m")
                for k in range(len(cuestionario.preguntas[i][j][2])):
                    if len(cuestionario.preguntas[i][j][2]) <= len(alfabeto):
                        print(cad2 + cads + "       \u001b[33m  " + alfabeto[k] + ") " + cuestionario.preguntas[i][j][2][k] + "\u001b[37m")
                    else:
                        print(cad2 + cads + "       \u001b[33m  " + str(k + 1) + cuestionario.preguntas[i][j][2][k] + "\u001b[37m")
            elif cuestionario.preguntas[i][j][1] == '3':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde seleccionando \u001b[33mVerdadero \u001b[36mo \u001b[33mFalso\u001b[36m.           \u001b[32m|\u001b[37m")
            elif cuestionario.preguntas[i][j][1] == '4':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde relacionando columnas.                     \u001b[32m|\u001b[37m")
                maximo_uno = len(cuestionario.preguntas[i][j][2][0][0])
                maximo_dos = len(cuestionario.preguntas[i][j][2][1][0])
                for t in range(len(cuestionario.preguntas[i][j][2][0])):
                    if len(cuestionario.preguntas[i][j][2][0][t]) > maximo_uno:
                        maximo_uno = len(cuestionario.preguntas[i][j][2][0][t])
                for r in range(len(cuestionario.preguntas[i][j][2][1])):
                    if len(cuestionario.preguntas[i][j][2][1][r]) > maximo_dos:
                        maximo_dos = len(cuestionario.preguntas[i][j][2][1][r])
                for k in range(len(cuestionario.preguntas[i][j][2][0])):
                    if ((cuestionario.preguntas[i][j][2][0][k] == '') or (cuestionario.preguntas[i][j][2][0][k] == ' ')):
                        print(cad2 + cads + "    \u001b[33m      " + "{0}".format(" " * maximo_uno) + "    " + cuestionario.preguntas[i][j][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[i][j][2][1][k]))) + "\u001b[37m")
                    elif ((cuestionario.preguntas[i][j][2][1][k] == '') or (cuestionario.preguntas[i][j][2][1][k] == ' ')):
                        print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[i][j][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[i][j][2][0][k]))) + "    " + "{0}".format(" " * maximo_dos) + "\u001b[37m")
                    else:
                        print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[i][j][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[i][j][2][0][k]))) + "    " + cuestionario.preguntas[i][j][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[i][j][2][1][k]))) + "\u001b[37m")
            elif cuestionario.preguntas[i][j][1] == '5':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con una sopa de letras.                    \u001b[32m|\u001b[37m")
                for r in range(len(cuestionario.preguntas[i][j][2])):
                    renglon_sopa = cad2 + cads + "          " + "\u001b[33m"
                    for t in range(len(cuestionario.preguntas[i][j][2][r])):
                        renglon_sopa = renglon_sopa + cuestionario.preguntas[i][j][2][r][t] + " "
                    renglon_sopa = renglon_sopa + "\u001b[37m"
                    print(renglon_sopa)

#    Funciones de escritura de encabezado
def introducir_nombre(opcion):
    nombre_cuestionario = input(cad2 + cads + "Introduce el nombre del cuestionario: ")
    if opcion != 's':    
        nombre_cuestionario = nombre_cuestionario.lower()
        nombre_cuestionario = nombre_cuestionario.title()
    cuestionario.modificarTitulo(nombre_cuestionario)

def introducir_autor(opcion):
    nombre_autor = input(cad2 + cads + "Introduce el nombre del autor: ")
    if opcion != 's':
        nombre_autor = nombre_autor.lower()
        nombre_autor = nombre_autor.title()
    cuestionario.modificarAutor(nombre_autor)

def introducir_fecha():
    try:
        dato_fecha = input(cad2 + cads + "Introduce la fecha en el formato dd-mm-aaaa: ")
        comprobacion = verificar_fecha(dato_fecha, error_formato)
        while comprobacion != True:
            dato_fecha = input(cad2 + cads + "Introduce la fecha en el formato dd-mm-aaaa: ")
            comprobacion = verificar_fecha(dato_fecha, error_formato)
        dato_fecha = procesar_fecha(dato_fecha)
        cuestionario.modificarFecha(dato_fecha)
    except:
        m_uno = cad2 + cads + error_formato + cad2 + cads
        m_dos = m_uno + "Se ha introducido la fecha 1 de Enero de 2020, esta fecha se puede        \u001b[32m|\u001b[37m\n"
        m_tres = m_dos + cad2 + cads
        m_cuatro = m_tres + "modificar más adelante en las correcciones.                               \u001b[32m|\u001b[37m"
        print(m_cuatro)
        dato_fecha = '1-1-2020'
        dato_fecha = procesar_fecha(dato_fecha)
        cuestionario.modificarFecha(dato_fecha)

def correccion(opcion, mensaje_error):
    dato_correccion = [0, 0]
    print(cad2 + cad2 + cad1 + cad2 + cad2 + cads + "    \u001b[36mPara corregir un dato del Encabezado presiona    1)                   \u001b[32m|\u001b[37m")    
    print(cad2 + cads + "    \u001b[36mCorección en la sección Preguntas                2)                   \u001b[32m|\u001b[37m")
    print(cad2 + cads + "    \u001b[37mPara salir de la correción presiona otro número                       \u001b[32m|\u001b[37m")
    correccion_uno = input(cad2 + cads + indicador)
    correccion_uno = revisar_numero(correccion_uno, mensaje_error)
    while correccion_uno.isdigit() != True:
        correccion_uno = input(cad2 + cads + indicador)
        correccion_uno = revisar_numero(correccion_uno, mensaje_error)
    dato_correccion[0] = int(correccion_uno)
    if dato_correccion[0] == 1:
        print(cad2 + cads + "    \u001b[36mSelecciona la corrección:                                             \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Cambiar Nombre del Cuestionario           1)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Cambiar Nombre del Autor                  2)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Cambiar Fecha                             3)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Añadir/Quitar Línea de Nombre             4)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Añadir/Quitar Línea de Grupo              5)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Añadir/Quitar/Cambiar Instrucciones       6)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Modificar la separación entre secciones   7)                        \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[37m  Presiona otra número para salir.                                    \u001b[32m|\u001b[37m")        
        opcion_dos = input(cad2 + cads + indicador)
        opcion_dos = revisar_numero(opcion_dos, mensaje_error)
        while opcion_dos.isdigit() != True:
            opcion_dos = input(cad2 + cads + indicador)
            opcion_dos = revisar_numero(opcion_dos, mensaje_error)
        dato_correccion[1] = int(opcion_dos)
    elif dato_correccion[0] == 2:
        print(cad2 + cads + "    \u001b[36mSelecciona la corrección:                                             \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Eliminar Sección                           1)                       \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Añadir Sección                             2)                       \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Cambiar título de una Sección              3)                       \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Cambiar una pregunta de una Sección        4)                       \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[33m  Añadir/Quitar una pregunta de una Sección  5)                       \u001b[32m|\u001b[37m")
        print(cad2 + cads + "    \u001b[37m  Presiona otra número para salir.                                    \u001b[32m|\u001b[37m")
        opcion_dos = input(cad2 + cads + indicador)
        opcion_dos = revisar_numero(opcion_dos, mensaje_error)
        while opcion_dos.isdigit() != True:
            opcion_dos = input(cad2 + cads + indicador)
            opcion_dos = revisar_numero(opcion_dos, mensaje_error)
        dato_correccion[1] = int(opcion_dos)
    if dato_correccion[0] == 1:
        if dato_correccion[1] == 1:
            introducir_nombre(opcion)
        elif dato_correccion[1] == 2:
            introducir_autor(opcion)
        elif dato_correccion[1] == 3:
            introducir_fecha()
        elif dato_correccion[1] == 4:
            if cuestionario.linea_alumno == True:
                print(cad2 + cads + "    \u001b[36m¿Quitar la línea de Nombre? Presiona \'s\' para confirmar               \u001b[32m|\u001b[37m")
                correccion = input(cad2 + cads + indicador)
                correccion = correccion.lower()
                correccion = correccion.strip()
                if correccion == 's':
                    print(cad2 + cads + "    \u001b[33mSe ha quitado la línea de Nombre.                                     \u001b[32m|\u001b[37m")
                    cuestionario.modificarLineaAlumno(False)
            elif cuestionario.linea_alumno == False:
                print(cad2 + cads + "    \u001b[36m¿Añadir la línea de Nombre? Presiona \'s\' para confirmar               \u001b[32m|\u001b[37m")
                correccion = input(cad2 + cads + indicador)
                correccion = correccion.lower()
                correccion = correccion.strip()
                if correccion == 's':
                    print(cad2 + cads + "    \u001b[33mSe ha añadido la línea de Nombre.                                     \u001b[32m|\u001b[37m")
                    cuestionario.modificarLineaAlumno(True)
        elif dato_correccion[1] == 5:
            if cuestionario.linea_grupo == True:
                print(cad2 + cads + "    \u001b[36m¿Quitar la línea de Grupo? Presiona \'s\' para confirmar                \u001b[32m|\u001b[37m")
                correccion = input(cad2 + cads + indicador)
                correccion = correccion.lower()
                correccion = correccion.strip()
                if correccion == 's':
                    print(cad2 + cads + "    \u001b[33mSe ha quitado la línea de Grupo.                                      \u001b[32m|\u001b[37m")
                    cuestionario.modificarLineaGrupo(False)
            elif cuestionario.linea_grupo == False:
                print(cad2 + cads + "    \u001b[36m¿Añadir la línea de Grupo? Presiona \'s\' para confirmar                \u001b[32m|\u001b[37m")
                correccion = input(cad2 + cads + indicador)
                correccion = correccion.lower()
                correccion = correccion.strip()
                if correccion == 's':
                    print(cad2 + cads + "    \u001b[33mSe ha añadido la línea de Grupo.                                      \u001b[32m|\u001b[37m")
                    cuestionario.modificarLineaGrupo(True)
        elif dato_correccion[1] == 6:
            if cuestionario.instrucciones == True:
                print(cad2 + cads + "    \u001b[33mQuitar Instrucciones    1)                                            \u001b[32m|\u001b[37m")
                print(cad2 + cads + "    \u001b[33mCambiar Instrucciones   2)                                            \u001b[32m|\u001b[37m")        
                correccion = input(cad2 + cads + indicador)
                correccion = revisar_numero(correccion, mensaje_error)
                while correccion.isdigit() != True:
                    print(mensaje_error)
                    print(cad2 + cads + "    \u001b[33mQuitar Instrucciones    1)                                            \u001b[32m|\u001b[37m")
                    print(cad2 + cads + "    \u001b[33mCambiar Instrucciones   2)                                            \u001b[32m|\u001b[37m")        
                    correccion = input(cad2 + cads + indicador)
                    correccion = revisar_numero(correccion, mensaje_error)
                correccion = int(correccion)
                if correccion == 1:
                    cuestionario.modificarInstrucciones(False)
                    cuestionario.modificarTextoInstrucciones('')
                    print(cad2 + cads + "    \u001b[33mSe han quitado las Instrucciones.                                     \u001b[32m|\u001b[37m")
                elif correccion == 2:
                    instrucciones = input(cad2 + cads + "Introduce las instrucciones (trata de no comerter faltas ortográficas): ")
                    cuestionario.modificarTextoInstrucciones(instrucciones)
                    print(cad2 + cads + "    \u001b[33mSe han cambiado las Instrucciones.                                    \u001b[32m|\u001b[37m")                    
            elif cuestionario.instrucciones == False:
                print(cad2 + cads + "    \u001b[33mIntroduce las Instrucciones:                                          \u001b[32m|\u001b[37m")    
                cuestionario.modificarInstrucciones(True)
                instrucciones = input(cad2 + cads + "Introduce las instrucciones (trata de no comerter faltas ortográficas): ")
                cuestionario.modificarTextoInstrucciones(instrucciones)
        elif dato_correccion[1] == 7:
            respuesta_separacion = [cuestionario.separacion[0], cuestionario.separacion[1]]
            respuesta_separacion_cero = cuestionario.separacion[0]
            respuesta_separacion_uno = cuestionario.separacion[1]
            if cuestionario.separacion[0] == True:
                if cuestionario.separacion[1] == True:
                    print(cad2 + cads + "    \u001b[36m¿Quitar separación entre secciones? Presiona \'s\' para confirmar       \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_cero = False
                    print(cad2 + cads + "    \u001b[36m¿Quitar separación de la portada? Presiona \'s\' para confirmar         \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_uno = False
                    respuesta_separacion[0] = respuesta_separacion_cero
                    respuesta_separacion[1] = respuesta_separacion_uno                
                if cuestionario.separacion[1] == False:
                    print(cad2 + cads + "    \u001b[36m¿Quitar separación entre secciones? Presiona \'s\' para confirmar       \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_cero = False
                    print(cad2 + cads + "    \u001b[36m¿Añadir separación de la portada? Presiona \'s\' para confirmar         \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_uno = True
                    respuesta_separacion[0] = respuesta_separacion_cero
                    respuesta_separacion[1] = respuesta_separacion_uno                        
            elif cuestionario.separacion[0] == False:            
                if cuestionario.separacion[1] == True:                    
                    print(cad2 + cads + "    \u001b[36m¿Añadir separación entre secciones? Presiona \'s\' para confirmar       \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_cero = True
                    print(cad2 + cads + "    \u001b[36m¿Quitar separación de la portada? Presiona \'s\' para confirmar         \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_uno = False
                    respuesta_separacion[0] = respuesta_separacion_cero
                    respuesta_separacion[1] = respuesta_separacion_uno
                elif cuestionario.separacion[1] == False:
                    print(cad2 + cads + "    \u001b[36m¿Añadir separación entre secciones? Presiona \'s\' para confirmar       \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_cero = True
                    print(cad2 + cads + "    \u001b[36m¿Añadir separación de la portada? Presiona \'s\' para confirmar         \u001b[32m|\u001b[37m")
                    respuesta = input(cad2 + cads + indicador)
                    respuesta = respuesta.strip()
                    respuesta = respuesta.lower()
                    if respuesta == 's':
                        respuesta_separacion_uno = True
                    respuesta_separacion[0] = respuesta_separacion_cero
                    respuesta_separacion[1] = respuesta_separacion_uno
            cuestionario.modificarSeparacion(respuesta_separacion)
    elif dato_correccion[0] == 2:
        if dato_correccion[1] == 1:
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la sección:                                   \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.secciones[i])
            correccion_dos = input(cad2 + cads + indicador)
            correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            while correccion_dos.isdigit() != True:
                correccion_dos = input(cad2 + cads + indicador)
                correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            dato_correccion[1] = int(correccion_dos)
            rectificar = input(cad2 + cads + "    \u001b[36mPresiona \'s\' para confirmar la eliminación de la sección " + cuestionario.secciones[dato_correccion[1] - 1] + ": ")
            print(cad2 + cads + "    \u001b[33mSe ha eliminado la sección " + cuestionario.secciones[dato_correccion[1] - 1])
            rectificar = rectificar.strip()
            rectificar = rectificar.lower()
            if rectificar == 's':
                cuestionario.secciones.remove(cuestionario.secciones[dato_correccion[1] - 1])
                cuestionario.preguntas.remove(cuestionario.preguntas[dato_correccion[1] - 1])
        elif dato_correccion[1] == 2:
            print(cad2 + cads + "    \u001b[36mLas secciones son:                                                    \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.secciones[i])        
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la nueva sección:                             \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") ")
            print(cad2 + cads + "      \u001b[33m" + str(len(cuestionario.secciones) + 1) + ") última posición")
            nuevo_numero = input(cad2 + cads + indicador)
            nuevo_numero = revisar_numero(nuevo_numero, mensaje_error)
            while nuevo_numero.isdigit() != True:
                nuevo_numero = input(cad2 + cads + indicador)
                nuevo_numero = revisar_numero(nuevo_numero, mensaje_error)
            nuevo_numero = int(nuevo_numero) - 1            
            preguntas_nueva_seccion = []
            print(cad2 + cads + "\u001b[35mIntroduce el nombre de la nueva sección:                                  \u001b[32m|\u001b[37m")
            nuevo_titulo = input(cad2 + cads + indicador)
            mensaje_seccion = cad2 + cads + "  Introduce el número de preguntas de la sección " + nuevo_titulo + ": "
            numero_preguntas = input(mensaje_seccion)
            numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)        
            while numero_preguntas.isdigit() != True:
                numero_preguntas = input(mensaje_seccion)
                numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)
            while numero_preguntas == '0':
                print(mensaje_error)
                numero_preguntas = input(mensaje_seccion)
                numero_preguntas = revisar_numero(numero_preguntas, mensaje_error)
            print(cad2 + cads + "  \u001b[36mIntroduce las preguntas.                                                \u001b[32m|\u001b[37m")
            for i in range(int(numero_preguntas)):
                mensaje = cad2 + cads + "    \u001b[33m" + nuevo_titulo + " pregunta " + str(i + 1) + ": \u001b[37m"
                pregunta = capturar_pregunta(mensaje, mensaje_error)
                preguntas_nueva_seccion.append(pregunta)
            if nuevo_numero == (len(cuestionario.secciones) + 1):
                cuestionario.modificarPreguntas(nuevo_titulo)
                cuestionario.modificarPreguntas(preguntas_seccion)
            elif nuevo_numero <= len(cuestionario.secciones):
                cuestionario.secciones.insert(nuevo_numero, nuevo_titulo)
                cuestionario.preguntas.insert(nuevo_numero, preguntas_nueva_seccion)
        elif dato_correccion[1] == 3:
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la sección:                                   \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.secciones[i])
            correccion_dos = input(cad2 + cads + indicador)
            correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            while correccion_dos.isdigit() != True:
                correccion_dos = input(cad2 + cads + indicador)
                correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            dato_correccion[1] = int(correccion_dos)
            print(cad2 + cads + "    \u001b[36mEscribe el nuevo nombre de la Sección correspondiente a " + cuestionario.secciones[dato_correccion[1] - 1])
            nuevo_nombre_seccion = input(cad2 + cads + indicador)
            print(cad2 + cads + "    \u001b[36mSe ha cambiado el nombre: " + cuestionario.secciones[dato_correccion[1] - 1] + " por el nombre: " + nuevo_nombre_seccion)
            cuestionario.secciones[dato_correccion[1] - 1] = nuevo_nombre_seccion
        elif dato_correccion[1] == 4:
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la sección:                                   \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.secciones[i])
            correccion_dos = input(cad2 + cads + indicador)
            correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            while correccion_dos.isdigit() != True:
                correccion_dos = input(cad2 + cads + indicador)
                correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            dato_correccion.append(int(correccion_dos))
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la pregunta a cambiar:                        \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.preguntas[dato_correccion[2] - 1])):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.preguntas[dato_correccion[2] - 1][i][0])
            correccion_tres = input(cad2 + cads + indicador)
            correccion_tres = revisar_numero(correccion_tres, mensaje_error)                    
            while correccion_tres.isdigit() != True:
                correccion_tres = input(cad2 + cads + indicador)
                correccion_tres = revisar_numero(correccion_tres, mensaje_error)
            correccion_tres = int(correccion_tres)
            correccion_tres = correccion_tres - 1
            print(cad2 + cad2 + cads + "\u001b[32mLa pregunta a cambiar es: \u001b[37m" + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][0])
            if cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '1':
                print(cad2 + cads + "    \u001b[36m  Pregunta con \u001b[33m" + str(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2]) + " espacios \u001b[36men blanco para la respuesta.\u001b[37m")
            elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '2':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con los siguietes incisos:                 \u001b[32m|\u001b[37m")
                for k in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2])):
                    if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2]) <= len(alfabeto):
                        print(cad2 + cads + "       \u001b[33m  " + alfabeto[k] + ") " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][k] + "\u001b[37m")
                    else:
                        print(cad2 + cads + "       \u001b[33m  " + str(k + 1) + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][k] + "\u001b[37m")
            elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '3':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde seleccionando \u001b[33mVerdadero \u001b[36mo \u001b[33mFalso\u001b[36m.           \u001b[32m|\u001b[37m")
            elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '4':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde relacionando columnas.                     \u001b[32m|\u001b[37m")
                maximo_uno = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][0])
                maximo_dos = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][0])
                for t in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0])):
                    if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][t]) > maximo_uno:
                        maximo_uno = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][t])
                for r in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1])):
                    if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][r]) > maximo_dos:
                        maximo_dos = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][r])
                for k in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0])):
                    if ((cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] == '') or (cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] == ' ')):
                        print(cad2 + cads + "    \u001b[33m      " + "{0}".format(" " * maximo_uno) + "    " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k]))) + "\u001b[37m")
                    elif ((cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] == '') or (cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] == ' ')):
                        print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k]))) + "    " + "{0}".format(" " * maximo_dos) + "\u001b[37m")
                    else:
                        print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k]))) + "    " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k]))) + "\u001b[37m")
            elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '5':
                print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con una sopa de letras.                    \u001b[32m|\u001b[37m")
                for r in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2])):
                    renglon_sopa = cad2 + cads + "          " + "\u001b[33m"
                    for t in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][r])):
                        renglon_sopa = renglon_sopa + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][r][t] + " "
                    renglon_sopa = renglon_sopa + "\u001b[37m"
                    print(renglon_sopa)            
            print(cad2 + cads + "    \u001b[36mPara cambiar la pregunta presiona                 1)                  \u001b[32m|\u001b[37m")
            print(cad2 + cads + "    \u001b[36mPara cambiar la pregunta y su respuesta presiona  2)                  \u001b[32m|\u001b[37m")
            cambio_pregunta = input(cad2 + cads + indicador)
            cambio_pregunta = revisar_numero(cambio_pregunta, mensaje_error)
            while cambio_pregunta.isdigit() != True:
                cambio_pregunta = input(cad2 + cads + indicador)
                cambio_pregunta = revisar_numero(cambio_pregunta, mensaje_error)
            if cambio_pregunta == '1':
                print(cad2 + cads + "    \u001b[36mIntroduce la nueva pregunta                                           \u001b[32m|\u001b[37m")
                cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][0] = input(cad2 + cads + indicador)                
            elif cambio_pregunta == '2':
                print(cad2 + cads + "    \u001b[36mIntroduce la nueva pregunta y su respuesta                            \u001b[32m|\u001b[37m")
                cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres] = capturar_pregunta(cad2 + cads + "Introduce la nueva pregunta: ",mensaje_error)
        elif dato_correccion[1] == 5:
            print(cad2 + cads + "    \u001b[36mSelecciona el número de la sección:                                   \u001b[32m|\u001b[37m")
            for i in range(len(cuestionario.secciones)):
                print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.secciones[i])
            correccion_dos = input(cad2 + cads + indicador)
            correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            while correccion_dos.isdigit() != True:
                correccion_dos = input(cad2 + cads + indicador)
                correccion_dos = revisar_numero(correccion_dos, mensaje_error)
            dato_correccion.append(int(correccion_dos))            
            print(cad2 + cads + "    \u001b[36mPara añadir pregunta presiona    1)                                   \u001b[32m|\u001b[37m")
            print(cad2 + cads + "    \u001b[36mPara eliminar pregunta presiona  2)                                   \u001b[32m|\u001b[37m")
            respuesta = input(cad2 + cads + indicador)
            respuesta = revisar_numero(respuesta, mensaje_error)
            while respuesta.isdigit() != True:
                respuesta = input(cad2 + cads + indicador)
                respuesta = revisar_numero(respuesta, mensaje_error)
            if respuesta == '1':
                print(cad2 + cads + "    \u001b[36mLas preguntas de la Sección son:                                      \u001b[32m|\u001b[37m")
                for i in range(len(cuestionario.preguntas[dato_correccion[2] - 1])):
                    print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.preguntas[dato_correccion[2] - 1][i][0])
                print(cad2 + cads + "    \u001b[36mSelecciona el número de la nueva pregunta:                            \u001b[32m|\u001b[37m")
                for i in range(len(cuestionario.preguntas[dato_correccion[2] - 1])):
                    print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") ")
                print(cad2 + cads + "      \u001b[33m" + str(len(cuestionario.preguntas[dato_correccion[2] - 1]) + 1) + ") última posición")
                nuevo_numero = input(cad2 + cads + indicador)
                nuevo_numero = revisar_numero(nuevo_numero, mensaje_error)
                while nuevo_numero.isdigit() != True:
                    nuevo_numero = input(cad2 + cads + indicador)
                    nuevo_numero = revisar_numero(nuevo_numero, mensaje_error)
                nuevo_numero = int(nuevo_numero) - 1
                nueva_pregunta = capturar_pregunta(cad2 + cads + "Introduce la nueva pregunta: ", mensaje_error)
                if nuevo_numero == (len(cuestionario.preguntas[dato_correccion[2] - 1]) + 1):
                    cuestionario.preguntas[dato_correccion[2] - 1].append(nueva_pregunta)
                elif nuevo_numero <= len(cuestionario.preguntas[dato_correccion[2] - 1]):
                    cuestionario.preguntas[dato_correccion[2] - 1].insert(nuevo_numero, nueva_pregunta)
            elif respuesta == '2':
                print(cad2 + cads + "    \u001b[36mSelecciona el número de la pregunta a eliminar:                       \u001b[32m|\u001b[37m")
                for i in range(len(cuestionario.preguntas[dato_correccion[2] - 1])):
                    print(cad2 + cads + "      \u001b[33m" + str(i + 1) + ") " + cuestionario.preguntas[dato_correccion[2] - 1][i][0])
                correccion_tres = input(cad2 + cads + indicador)
                correccion_tres = revisar_numero(correccion_tres, mensaje_error)                    
                while correccion_tres.isdigit() != True:
                    correccion_tres = input(cad2 + cads + indicador)
                    correccion_tres = revisar_numero(correccion_tres, mensaje_error)
                correccion_tres = int(correccion_tres)
                correccion_tres = correccion_tres - 1
                print(cad2 + cad2 + cads + "\u001b[32mLa pregunta a elimar es: \u001b[37m" + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][0])
                if cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '1':
                    print(cad2 + cads + "    \u001b[36m  Pregunta con \u001b[33m" + str(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2]) + " espacios \u001b[36men blanco para la respuesta.\u001b[37m")
                elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '2':
                    print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con los siguietes incisos:                 \u001b[32m|\u001b[37m")
                    for k in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2])):
                        if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2]) <= len(alfabeto):
                            print(cad2 + cads + "       \u001b[33m  " + alfabeto[k] + ") " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][k] + "\u001b[37m")
                        else:
                            print(cad2 + cads + "       \u001b[33m  " + str(k + 1) + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][k] + "\u001b[37m")
                elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '3':
                    print(cad2 + cads + "    \u001b[36m  Pregunta que se responde seleccionando \u001b[33mVerdadero \u001b[36mo \u001b[33mFalso\u001b[36m.           \u001b[32m|\u001b[37m")
                elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '4':
                    print(cad2 + cads + "    \u001b[36m  Pregunta que se responde relacionando columnas.                     \u001b[32m|\u001b[37m")
                    maximo_uno = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][0])
                    maximo_dos = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][0])
                    for t in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0])):
                        if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][t]) > maximo_uno:
                            maximo_uno = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][t])
                    for r in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1])):
                        if len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][r]) > maximo_dos:
                            maximo_dos = len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][r])
                    for k in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0])):
                        if ((cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] == '') or (cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] == ' ')):
                            print(cad2 + cads + "    \u001b[33m      " + "{0}".format(" " * maximo_uno) + "    " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k]))) + "\u001b[37m")
                        elif ((cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] == '') or (cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] == ' ')):
                            print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k]))) + "    " + "{0}".format(" " * maximo_dos) + "\u001b[37m")
                        else:
                            print(cad2 + cads + "    \u001b[33m      " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k] + "{0}".format(" " * (maximo_uno - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][0][k]))) + "    " + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k] + "{0}".format(" " * (maximo_dos - len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][1][k]))) + "\u001b[37m")
                elif cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][1] == '5':
                    print(cad2 + cads + "    \u001b[36m  Pregunta que se responde con una sopa de letras.                    \u001b[32m|\u001b[37m")
                    for r in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2])):
                        renglon_sopa = cad2 + cads + "          " + "\u001b[33m"
                        for t in range(len(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][r])):
                            renglon_sopa = renglon_sopa + cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres][2][r][t] + " "
                        renglon_sopa = renglon_sopa + "\u001b[37m"
                        print(renglon_sopa)           
                confirmacion = input(cad2 + cads + "        Presiona \'s\' para confirmar : ")
                confirmacion = confirmacion.strip()
                confirmacion = confirmacion.lower()
                if confirmacion == 's':
                    cuestionario.preguntas[dato_correccion[2] - 1].remove(cuestionario.preguntas[dato_correccion[2] - 1][correccion_tres])

#    Funciones para guardar cuestionarios                    
def guardar_cuestionario(nombre_json):
    datos = {
        'titulo':cuestionario.titulo,
        'autor':cuestionario.autor,
        'fecha':cuestionario.fecha,
        'secciones':cuestionario.secciones,
        'preguntas':cuestionario.preguntas,
        'separacion':cuestionario.separacion,
        'linea_alumno':cuestionario.linea_alumno,
        'linea_grupo':cuestionario.linea_grupo,
        'instrucciones':cuestionario.instrucciones,
        'texto_instrucciones':cuestionario.texto_instrucciones
    }
    with open(nombre_json, 'w') as archivo:
        json.dump(datos, archivo)

def abrir_cuestionario(nombre_json):
    with open(nombre_json, 'r') as archivo:
        datos = json.load(archivo)
    return datos

#    Funciones de codificación
def procesar_vector(vector):
    salida = []
    for elemento in vector:
        if elemento != '':
            salida.append(elemento.strip('\n'))
    return salida

def codificar_incisos(elemento):
    codigo = ["        	\\begin{itemize}"]
    if len(elemento) > len(alfabeto):
        for i in range(len(elemento)):
            x = "        		\item[" + str(i) + ")]" + elemento[i]
            codigo.append(x)
        codigo.append("        	\end{itemize}")
    else:
        for i in range(len(elemento)):
            x = "        		\item[" + alfabeto[i] + ")]" + elemento[i]
            codigo.append(x)
        codigo.append("        	\end{itemize}")
    return codigo

def codificar_preguntas(vector,seccion):
    codigo = ["    \section{" + seccion + "}"]
    codigo.append("    \\begin{itemize}")
    for i in range(len(vector)):
        if vector[i][1] == '1':
            x = "        \item[" + str(i + 1) + "] " + vector[i][0]
            y = "        	\\newline"
            codigo.append(x)
            iteracion = int(vector[i][2])
            for j in range(iteracion):
                codigo.append(y)
        elif vector[i][1] == '2':
            x = "        \item[" + str(i + 1) + "] " + vector[i][0]
            codigo.append(x)
            y = codificar_incisos(vector[i][2])
            for elemento in y:
                codigo.append(elemento)
        elif vector[i][1] == '3':
            x = "        \item[" + str(i + 1) + "] " + vector[i][0]
            codigo.append(x)
            y = "        	\\newline"
            z = "        	\\newline \centerline{Veradero\hspace{5cm}Falso\hspace{3cm}}"
            codigo.append(y)
            codigo.append(z)
            codigo.append(y)
        elif vector[i][1] == '4':
            max_uno = len(vector[i][2][0][0])
            max_dos = len(vector[i][2][1][0])
            for r in range(len(vector[i][2][0])):
                if len(vector[i][2][0][r]) > max_uno:
                    max_uno = len(vector[i][2][0][r])
            for t in range(len(vector[i][2][1])):
                if len(vector[i][2][1][t]) > max_dos:
                    max_dos = len(vector[i][2][1][t])            
            x = "        \item[" + str(i + 1) + "] " + vector[i][0]
            codigo.append(x)
            codigo.append("            \\begin{center}")
            codigo.append("                \\begin{tabular}{c c c c} \\\\")
            if len(vector[i][2][0]) > len(vector[i][2][1]):
                for j in range(len(vector[i][2][0]) - len(vector[i][2][1])):
                    vector[i][2][1].append("{0}".format(" " * max_dos))
            elif len(vector[i][2][1]) > len(vector[i][2][0]):
                for j in range(len(vector[i][2][1]) - len(vector[i][2][0])):
                    vector[i][2][0].append("{0}".format(" " * max_uno))
            for k in range(len(vector[i][2][0])):
                codigo.append("                    \\\\" + vector[i][2][0][k] + " & \hspace{2cm} & " + vector[i][2][1][k] + " & \hspace{2cm} \\\\")
            codigo.append("                \end{tabular}")
            codigo.append("            \end{center}") 
        elif vector[i][1] == '5':
            x = "        \item[" + str(i + 1) + "] " + vector[i][0]
            codigo.append(x)
            codigo.append("        \\begin{center}")
            formato = "c|"
            tabla = "|"
            for a in range(len(vector[i][2][0])):
                tabla = tabla + formato
            linea = "            \\begin{tabular}{" + tabla + "}\hline"
            codigo.append(linea)
            for j in range(len(vector[i][2])):
                linea_tabla = ''
                for k in range(len(vector[i][2][j])):
                    linea_tabla = linea_tabla + vector[i][2][j][k] + " & "
                linea_tabla.strip()
                linea_tabla = linea_tabla[0:len(linea_tabla) - 2]
                linea_tabla = "                " + linea_tabla + "\\\\ \hline"
                codigo.append(linea_tabla)
            codigo.append("            \end{tabular}")
            codigo.append("        \end{center}")
    codigo.append("    \end{itemize}")
    return codigo


#****************************************************************************************************************************************************
#
#   Ejecución del programa, se pide información, se leen preguntas, se escriben ficheros y se juntan en un archivo .tex
#
#****************************************************************************************************************************************************

#    Importar módulos.
import os
import json
import platform as pl


#    Detectar sistema operativo y directorio de ejecución.
if hasattr(pl, 'system'):
    sistema_clave = '%s: %s' % ('system', getattr(pl, 'platform')())
sistema = sistema_clave[8].upper()

ruta_uno = os.getcwd()
ruta_dos = ''
if sistema == 'W':
    ruta_dos = ruta_uno + '\Cuestionarios'
elif sistema == 'L':
    ruta_dos = ruta_uno + '/Cuestionarios'


#    Limpiar pantalla y presentación del programa.

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
cad0 = "\u001b[32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\u001b[37m"
cad1 = "\u001b[32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\u001b[37m\n"
cad2 = "\u001b[32m|                                                                                |\u001b[37m\n"  
cad3 = "\u001b[32m|\u001b[36m********************************************************************************\u001b[32m|\u001b[37m\n"  
cad4 = "\u001b[32m|\u001b[36m************************                               *************************\u001b[32m|\u001b[37m\n"
cad5 = "\u001b[32m|                                                                                |\u001b[37m"
cadp = "\u001b[32m|\u001b[36m************************  \u001b[37mGENERADOR DE CUESTIONARIOS.  \u001b[36m*************************\u001b[32m|\u001b[37m\n" 
cads = "\u001b[32m|\u001b[37m      "

indicador = "                         \u001b[32m>>\u001b[37m  "
error_formato = "    \u001b[31mFormato no válido.\u001b[37m                                                    \u001b[32m|\u001b[37m\n"
error_opcion = "    \u001b[31mOpción no válida.\u001b[37m                                                     \u001b[32m|\u001b[37m"

limpiar_pantalla(sistema)
print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)

if sistema == 'W':
    os.chdir('C:\\')
elif sistema == 'L':
    os.chdir('/')

print(cad2 + cad2 + cads + "Introduce el directorio de trabajo o presiona D si quieres usar el        \u001b[32m|\u001b[37m")
print(cad2 + cads + "directorio de trabajo predeterminado:                                     \u001b[32m|\u001b[37m")
print(cad2 + cads + "\u001b[32m" + ruta_dos + "\u001b[37m")
directorio_trabajo_respuesta = input(cad2 + cads + indicador)
xyz = directorio_trabajo_respuesta.strip()
xyz = xyz.lower()
if xyz == 'd':
    directorio_trabajo = ruta_uno
elif xyz != 'd':
    directorio_trabajo = directorio_trabajo_respuesta

while os.path.isdir(directorio_trabajo) != True:
    mensaje_directorio = cad2 + cads + error_formato + cad2 + cads + "El directorio no existe                                                   \u001b[32m|\u001b[37m\n"
    print(mensaje_directorio + cad2 + cads + "Introduce el directorio de trabajo o presiona D si quieres usar el        \u001b[32m|\u001b[37m")
    print(cad2 + cads + "directorio de trabajo predeterminado:                                     \u001b[32m|\u001b[37m")
    print(cad2 + cads + "\u001b[32m" + ruta_dos + "\u001b[37m")
    directorio_trabajo_respuesta = input(cad2 + cads + indicador)
    xyz = directorio_trabajo_respuesta.strip()
    xyz = xyz.lower()
    if xyz == 'd':
        directorio_trabajo = ruta_uno
    elif xyz != 'd':
        directorio_trabajo = directorio_trabajo_respuesta

os.chdir(ruta_uno)

respaldo = False
if sistema == 'W':
    if os.path.isfile(ruta_uno + '\\respaldo.json') == True:
        respaldo = True
elif sistema == 'L':
    if os.path.isfile(ruta_uno + '/respaldo.json') == True:
        respaldo = True

if respaldo == True:
    print(cad2 + cad2 + cads + "Se ha detectado un cuestionario no guardado, presiona \'s\' si quieres      \u001b[32m|\u001b[37m" )
    print(cad2 + cads +  "restaurar el cuestionario.                                                \u001b[32m|\u001b[37m")
    respaldo_respuesta = input(cad2 + cads + indicador)
    respaldo_respuesta = respaldo_respuesta.strip()
    respaldo_respuesta = respaldo_respuesta.lower()
    if respaldo_respuesta == 's':
        eleccion_inicio = '5'
    else:
        if sistema == 'W':
            os.system('ERASE respaldo.json')
        elif sistema == 'L':
            os.system('rm respaldo.json')

        limpiar_pantalla(sistema)
        print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)
        print(cad2 + cad2 + cads + "\u001b[32mSelecciona una opción.                                                    \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Escribir un cuestionario   1)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Editar un cuestionario     2)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Manual                     3)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Información del programa   4)                                           \u001b[32m|\u001b[37m")
        eleccion_inicio = input(cad2 + cads + indicador)
        eleccion_inicio = revisar_numero(eleccion_inicio, cad2 + cads + error_opcion)
        while eleccion_inicio not in {'1', '2', '3', '4'}:
            print(cad2 + cad2 + cads + "\u001b[32mSelecciona una opción.                                                    \u001b[32m|\u001b[37m")
            print(cad2 + cads + "  Escribir un cuestionario   1)                                           \u001b[32m|\u001b[37m")
            print(cad2 + cads + "  Editar un cuestionario     2)                                           \u001b[32m|\u001b[37m")
            print(cad2 + cads + "  Manual                     3)                                           \u001b[32m|\u001b[37m")
            print(cad2 + cads + "  Información del programa   4)                                           \u001b[32m|\u001b[37m")
            eleccion_inicio = input(cad2 + cads + indicador)
            eleccion_inicio = revisar_numero(eleccion_inicio, cad2 + cads + error_opcion)

else:
    limpiar_pantalla(sistema)
    print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)
    print(cad2 + cad2 + cads + "\u001b[32mSelecciona una opción.                                                    \u001b[32m|\u001b[37m")
    print(cad2 + cads + "  Escribir un cuestionario   1)                                           \u001b[32m|\u001b[37m")
    print(cad2 + cads + "  Editar un cuestionario     2)                                           \u001b[32m|\u001b[37m")
    print(cad2 + cads + "  Manual                     3)                                           \u001b[32m|\u001b[37m")
    print(cad2 + cads + "  Información del programa   4)                                           \u001b[32m|\u001b[37m")
    eleccion_inicio = input(cad2 + cads + indicador)
    eleccion_inicio = revisar_numero(eleccion_inicio, cad2 + cads + error_opcion)
    while eleccion_inicio not in {'1', '2', '3', '4'}:
        print(cad2 + cad2 + cads + "\u001b[32mSelecciona una opción.                                                    \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Escribir un cuestionario   1)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Editar un cuestionario     2)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Manual                     3)                                           \u001b[32m|\u001b[37m")
        print(cad2 + cads + "  Información del programa   4)                                           \u001b[32m|\u001b[37m")
        eleccion_inicio = input(cad2 + cads + indicador)
        eleccion_inicio = revisar_numero(eleccion_inicio, cad2 + cads + error_opcion)

if eleccion_inicio == '1':
    limpiar_pantalla(sistema)
    print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)
    cuestionario = Cuestionario()
    correccion_eleccion = 'n'

    introducir_nombre(correccion_eleccion)

    introducir_autor(correccion_eleccion)

    introducir_fecha()

    respuesta_alumno = input(cad2 + cads + "Presiona \'s\' para añadir la línea del nombre: ")
    respuesta_alumno = respuesta_alumno.strip()
    respuesta_alumno = respuesta_alumno.lower()
    if respuesta_alumno == 's':
        cuestionario.modificarLineaAlumno(True)
        print(cad2 + cads + "\u001b[36m    Se introdujo la linea Nombre:                                         \u001b[32m|\u001b[37m")

    respuesta_grupo = input(cad2 + cads + "Presiona \'s\' para añadir la línea del grupo: ")
    respuesta_grupo = respuesta_grupo.strip()
    respuesta_grupo = respuesta_grupo.lower()
    if respuesta_grupo == 's':
        cuestionario.modificarLineaGrupo(True)
        print(cad2 + cads + "\u001b[36m    Se introdujo la linea Grupo:                                          \u001b[32m|\u001b[37m")

    respuesta_instrucciones = input(cad2 + cads + "Presiona \'s\' si quieres añadir instrucciones: ")
    respuesta_instrucciones = respuesta_instrucciones.strip()
    respuesta_instrucciones = respuesta_instrucciones.lower()
    if respuesta_instrucciones == 's':
        cuestionario.modificarInstrucciones(True)
        mensaje_instrucciones = "\u001b[36mIntroduce las instrucciones (trata de no comerter faltas ortográficas):   \u001b[32m|\u001b[37m\n"
        instrucciones = input(cad2 + cads + mensaje_instrucciones + cad2 + "\u001b[32m|      >>  \u001b[37m")
        cuestionario.modificarTextoInstrucciones(instrucciones)

    numero_secciones = input(cad2 + cads + "Introduce el número de secciones: ")
    numero_secciones = revisar_numero(numero_secciones, cad2 + cads + error_opcion)
    while numero_secciones.isdigit() != True:
        numero_secciones = input(cad2 + cads + "Introduce el número de secciones: ")
        numero_secciones = revisar_numero(numero_secciones, cad2 + cads + error_opcion)
    numero_secciones = int(numero_secciones)

    respuesta_secciones = input(cad2 + cads + "Si quieres que cada sección vaya en una página presiona \'s\': ")
    respuesta_secciones = respuesta_secciones.strip()
    respuesta_secciones = respuesta_secciones.lower()
    if respuesta_secciones == 's':
        cuestionario.modificarSeparacion([True, False])
        print(cad2 + cads + "\u001b[36m    Las secciones van en hojas separadas.                                 \u001b[32m|\u001b[37m")
        respuesta_portada = input(cad2 + cads + "Presiona \'s\' si quieres dejar la portada en una hoja individual: ")
        respuesta_portada = respuesta_portada.strip()
        respuesta_portada = respuesta_portada.lower()
        if respuesta_portada == 's':
            cuestionario.modificarSeparacion([True, True])
            print(cad2 + cads + "\u001b[36m    La portada va en una hoja separada.                                   \u001b[32m|\u001b[37m")
        else:
            print(cad2 + cads + "\u001b[36m    La portada no va en una hoja separada.                                \u001b[32m|\u001b[37m")
    else:
        print(cad2 + cads + "\u001b[36m    Las secciones no van en hojas separadas.                              \u001b[32m|\u001b[37m")

    print(cad2 + cad1 + cad2 + cads + "  \u001b[33mIntroduce las secciones.                                                \u001b[32m|\u001b[37m")
    for i in range(numero_secciones):
        cadena = input(cad2 + cads + "    \u001b[32mSección " + str(i + 1) + ":\u001b[37m ")
        cadena = cadena.strip()
        cadena = cadena.title()
        cuestionario.modificarSecciones(cadena)
    print(cad2 + cad1 + cad5)

    capturar_preguntas(cuestionario.secciones, cad2 + cads + error_opcion)
    guardar_cuestionario(cuestionario.titulo + '.json')
    guardar_cuestionario('respaldo.json')
    
elif eleccion_inicio == '2':
    limpiar_pantalla(sistema)
    print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)
    if sistema == 'W':
        os.chdir('C:\\')
    elif sistema == 'L':
        os.chdir('/')
    print(cad2 + cad2 + cads + "Introduce el directorio en donde está guardado el archivo:                \u001b[32m|\u001b[37m")
    directorio_archivo = input(cad2 + cads + indicador)
    while os.path.isdir(directorio_archivo) != True:
        print(cad2 + cads + error_formato + cad2 + cad2 + cads + "Introduce el directorio en donde está guardado el archivo:                \u001b[32m|\u001b[37m")
        directorio_archivo = input(cad2 + cads + indicador)
    print(cad2 + cad2 + cads + "Introduce el nombre del archivo (.json):                                  \u001b[32m|\u001b[37m")
    nombre_archivo = input(cad2 + cads + indicador)
    while os.path.isfile(directorio_archivo + '/' + nombre_archivo) != True:
        print(cad2 + cads + error_opcion + "\n" + cad2 + cad2 + cads + "Introduce el nombre del archivo (.json):                                  \u001b[32m|\u001b[37m")
        nombre_archivo = input(cad2 + cads + indicador)
    os.chdir(directorio_trabajo)
    cuestionario_json = abrir_cuestionario(directorio_archivo + '/' + nombre_archivo)    
    cuestionario = Cuestionario()
    cuestionario.modificarTitulo(cuestionario_json['titulo'])
    cuestionario.modificarAutor(cuestionario_json['autor'])
    cuestionario.modificarFecha(cuestionario_json['fecha'])
    for elemento in cuestionario_json['secciones']:        
        cuestionario.modificarSecciones(elemento)
    for elemento in cuestionario_json['preguntas']:        
        cuestionario.modificarPreguntas(elemento)
    cuestionario.modificarSeparacion(cuestionario_json['separacion'])
    cuestionario.modificarLineaAlumno(cuestionario_json['linea_alumno'])
    cuestionario.modificarLineaGrupo(cuestionario_json['linea_grupo'])
    cuestionario.modificarInstrucciones(cuestionario_json['instrucciones'])
    cuestionario.modificarTextoInstrucciones(cuestionario_json['texto_instrucciones'])
    print(cad2 + cad2 + cads + "\u001b[32mEditar Cuestionario.                                                      |\u001b[37m")
    guardar_cuestionario(cuestionario.titulo + '.json')
    guardar_cuestionario('respaldo.json')

elif eleccion_inicio == '3':
    if sistema == 'W':
        os.system(ruta_uno + "\Manual\presentacion.html")
        print(cad2 + cad2 + cad1)
        os.system('PAUSE')
        reinicio(sistema)
    elif sistema == 'L':
        os.system("gnome-www-browser " + ruta_uno + "\Manual\presentacion.html")
        print(cad2 + cads + "Si no inicia el manual, abre el archivo \"presentacion.html\" en la ruta:   \u001b[32m|\u001b[37m")
        print(cad2 + cads + ruta_uno + "/Manual")
        print(cad2 + cad2 + cad1)
        os.system('sleep 10')
        reinicio(sistema)

elif eleccion_inicio == '4':
    limpiar_pantalla(sistema)
    print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)    
    print(cad2  + cads + "\u001b[32mVersión:         \u001b[37m 0                                                       \u001b[32m|\u001b[37m")
    print(cad2  + cads + "\u001b[32mLicencia de uso: \u001b[37m Apache 2.0                                              \u001b[32m|\u001b[37m")
    print(cad2  + cads + "\u001b[32mDesarrollador:   \u001b[37m Omar Daniel Esquivel Sánchez                            \u001b[32m|\u001b[37m")
    print(cad2  + cads + "\u001b[32mContacto:        \u001b[37m omar48arch@gmail.com                                    \u001b[32m|\u001b[37m")
    print(cad2 + cad1)
    no_variable = input("Presione una tecla para continuar . . . ")
    reinicio(sistema)

elif eleccion_inicio == '5':
    limpiar_pantalla(sistema)
    print(cad1 + cad3 + cad4 + cadp + cad4 + cad3 + cad0)
    cuestionario_json = abrir_cuestionario('respaldo.json')    
    cuestionario = Cuestionario()
    cuestionario.modificarTitulo(cuestionario_json['titulo'])
    cuestionario.modificarAutor(cuestionario_json['autor'])
    cuestionario.modificarFecha(cuestionario_json['fecha'])
    for elemento in cuestionario_json['secciones']:        
        cuestionario.modificarSecciones(elemento)
    for elemento in cuestionario_json['preguntas']:        
        cuestionario.modificarPreguntas(elemento)
    cuestionario.modificarSeparacion(cuestionario_json['separacion'])
    cuestionario.modificarLineaAlumno(cuestionario_json['linea_alumno'])
    cuestionario.modificarLineaGrupo(cuestionario_json['linea_grupo'])
    cuestionario.modificarInstrucciones(cuestionario_json['instrucciones'])
    cuestionario.modificarTextoInstrucciones(cuestionario_json['texto_instrucciones'])
    print(cad2 + cad2 + cads + "\u001b[32mEditar Cuestionario.                                                      |\u001b[37m")
    guardar_cuestionario(cuestionario.titulo + '.json')
    guardar_cuestionario('respaldo.json')

presentar_preguntas()

correccion_eleccion = input(cad2 + cad2 + cads + "Presiona \'s\' si quieres hacer una correción: ")
correccion_eleccion = correccion_eleccion.strip()
correccion_eleccion = correccion_eleccion.lower()

while correccion_eleccion == 's':
    correccion(correccion_eleccion, cad2 + cads + error_opcion)
    presentar_preguntas()
    correccion_eleccion = input(cad2 + cad2 + cads + "Presiona \'s\' si quieres hacer una correción: ")
    correccion_eleccion = correccion_eleccion.strip()
    correccion_eleccion = correccion_eleccion.lower()
    guardar_cuestionario(cuestionario.titulo + '.json')
    guardar_cuestionario('respaldo.json')


#    Aqui va la codificación y compilación.
codigo_principal = []

for i in range(len(cuestionario.preguntas)):
    preguntas_latex = codificar_preguntas(cuestionario.preguntas[i], cuestionario.secciones[i])
    if cuestionario.separacion == [True, True]:
        preguntas_latex.insert(0, '    \\newpage')
    elif cuestionario.separacion == [True, False]:
        if i != 0:
            preguntas_latex.insert(0, '    \\newpage')
    elif cuestionario.separacion == [False, True]:
        if i == 0:
            preguntas_latex.insert(0, '    \\newpage')

    for subelemento in preguntas_latex:
        codigo_principal.append(subelemento)

codigo_principal.append("\end{document}")

argumento_fichero = ''
if sistema == 'W':
    argumento_fichero = 'ficherostexto\preambulo.txt'
elif sistema == 'L':
    argumento_fichero = './ficherostexto/preambulo.txt'


preambulo = leer_fichero(argumento_fichero) 
codigo_latex = procesar_vector(preambulo)

codigo_latex.append("%   Inicio del documento.")
codigo_latex.append("\\begin{document}")
codigo_latex.append("        %   Datos del encabezado.")
codigo_latex.append("        \\title{" + cuestionario.titulo +"}")
codigo_latex.append("        \\author{" + cuestionario.autor + "}")
codigo_latex.append("        \date{" + cuestionario.fecha + "}")
codigo_latex.append("        \maketitle")

if cuestionario.linea_alumno == True:
    codigo_latex.append("        \paragraph{Nombre: }")

if cuestionario.linea_grupo == True:
    codigo_latex.append("        \paragraph{Grupo: }")

if cuestionario.instrucciones == True:
    codigo_latex.append("        \paragraph{Instrucciones: }" + cuestionario.texto_instrucciones)

for elemento in codigo_principal:
    codigo_latex.append(elemento)

crear_fichero('auxiliar.txt')
for elemento in codigo_latex:
    escribir_linea('auxiliar.txt', elemento)


#   Creación de la carpeta, archivo.txt configurar los archivos y compilar. -------------------------------------------------------------------------
if directorio_trabajo == ruta_uno:
    directorio_trabajo = ruta_dos

if sistema == 'W':
    os.system('iconv -f windows-1252 -t utf-8 auxiliar.txt > "' + cuestionario.titulo + '.tex"')
    os.system('MKDIR "' + cuestionario.titulo + '"')
    os.system('MOVE "' + cuestionario.titulo + '.tex" "' + cuestionario.titulo + '"')
    os.system('pdflatex -output-directory="' + cuestionario.titulo + '" "' + cuestionario.titulo + '.tex"')
    os.system('ERASE auxiliar.txt')
    os.system('MOVE "' + cuestionario.titulo + '.json" "' + cuestionario.titulo + '"')
    os.system('MOVE "' + cuestionario.titulo + '" "' + directorio_trabajo + '"')
elif sistema == 'L':
    os.system('iconv -f ISO-8859-1 -t UTF-8 auxiliar.txt > "' + cuestionario.titulo + '.tex"')
    os.system('mkdir "' + cuestionario.titulo + '"')
    os.system('mv "' + cuestionario.titulo + '.tex" "' + cuestionario.titulo + '"')
    os.system('pdflatex -output-directory="' + cuestionario.titulo + '" "' + cuestionario.titulo + '.tex"')
    os.system('rm auxiliar.txt')
    os.system('mv "' + cuestionario.titulo + '.json" "' + cuestionario.titulo + '"')
    os.system('mv "' + cuestionario.titulo + '" "' + directorio_trabajo + '"')


#    Finalizar el programa.
archivos_directorio = os.listdir(ruta_uno)
archivos_borrar = []

for elemento in archivos_directorio:
    if elemento[len(elemento) - 5:len(elemento)] == '.json':
        archivos_borrar.append(elemento)

if sistema == 'W':
    for elemento in archivos_borrar:
        os.system('ERASE ' + elemento)
elif sistema == 'L':
    for elemento in archivos_borrar:
        os.system('rm ' + elemento)

cadena_salida = "\u001b[32m|\u001b[37m   Se ha generado el archivo " + '\u001b[34m' + cuestionario.titulo + ".pdf \u001b[37men la carpeta: " + '\u001b[34m ' + cuestionario.titulo
print(cad2 + cad2 + cadena_salida)

opcion_reinicio = input(cad2 + cad2 + cads + "Presiona \'s\' si quieres reiniciar el programa: ")
opcion_reinicio = opcion_reinicio.strip()
opcion_reinicio = opcion_reinicio.lower()
if opcion_reinicio == 's':
    reinicio(sistema)
else:
    print(cad2 + cad2 + cads + "\u001b[32mFIN DEL PROGRAMA.                                                         \u001b[32m|\u001b[37m\n" + cad2 + cad2 + cad1)