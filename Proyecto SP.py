#Proyecto Situación Problema
from io import open #Abrir archivos
import random #Librería para usar númeross aleatorios
import sys #Salir del programa
from tkinter import* #Abrir imágenes

def reg_alumno(registro_alumno):
    print('\nNo te preocupes, aquí puedes registrar rápidamente.\n')
    
    registro_alumno=[]
    nombre=input('Escribe tu primer nombre: ')
    seg_nombre=input('Escribe tu segundo nombre (en caso de tener): ')
    apellido=input('Escribe tu apellido paterno: ')
    seg_apellido=input('Escribe tu apelllido materno: ')
    fecha_nacimiento=input('Escribe tu fecha de nacimiento en el siguiente formato (dia/mes/año), \n  Ejemplo-25/09/2007:  ')
    correo=input('Escribe tu correo electrónico: ')
    
    registro_alumno.append(nombre)
    registro_alumno.append(seg_nombre)
    registro_alumno.append(apellido)
    registro_alumno.append(seg_apellido)
    registro_alumno.append(fecha_nacimiento)
    registro_alumno.append(correo)
    return registro_alumno
        
def verif_registro(alumnos, variables_registro, registro_alumno):
    print('\nPor favor, verifica tus datos. \n¿Son correctos?')
    
    print('Nombre completo:', end=' ')
    for i in range(len(registro_alumno)-2):
        print(registro_alumno[i], end= ' ')

    print('\nFecha de nacimiento:', registro_alumno[-2])
    print('Correo electrónico:',registro_alumno[-1])
    print('\nSi son correctos, por favor, selecciona el número 1 para Sí, de lo contrario, coloca 2.')
    sn= """
1. Sí
2. No
    """
    print(sn)
    sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
    while sino!='1' and sino!='2':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
        sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
    sino=int(sino)
    
    if sino==1:
        alumnos.append(registro_alumno)
        print('\nFelicidades '+ registro_alumno[0] + ', te has registrado exitosamente. \nEs un gusto tenerte aquí, dispuesto(a) a aprender.')
    else:
        print('¿Qué dato deseas modificar?')
        correccion_registro= """
        1. Nombre
        2. Segundo Nombre
        3. Apellido paterno
        4. Apellido materno
        5. Correo electrónico
        """
        print(correccion_registro)
        corregir=input('Escribe el número de la opción que deseas llevar a cabo: ')
        while corregir!='1' and corregir!='2' and corregir!='3' and corregir!='4' and corregir!='5':
            print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
            corregir=input('Escribe el número de la opción que deseas llevar a cabo: ')
        corregir=int(corregir)

        dato_corregido=input('Escribe el dato corregido: ')
        print(f'Tu {variables_registro[corregir-1].lower()} ha sido modificado de {registro_alumno[corregir-1]} a {dato_corregido}')
        registro_alumno[corregir-1]=dato_corregido
        print('\n¿Deseas realizar otro cambio?')
        print(sn)
        sino=input('Escribe el número de la opción que deseas llevar a cabo: ')

        while sino!='1' and sino!='2':
            print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
            sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
        
        sino=int(sino)
        while sino==1:
            print(correccion_registro)
            corregir=input('Escribe el número de la opción que deseas llevar a cabo: ')
            while corregir!='1' and corregir!='2' and corregir!='3' and corregir!='4':
                print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
                corregir=input('Escribe el número de la opción que deseas llevar a cabo: ')
            corregir=int(corregir)

            dato_corregido=input('Escribe el dato corregido: ')
            print(f'Tu {variables_registro[corregir-1].lower()} ha sido modificado de {registro_alumno[corregir-1]} a {dato_corregido}')
            registro_alumno[corregir-1]=dato_corregido
            print('¿Deseas realizar otro cambio?')
            print(sn)
            sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
            while sino!='1' and sino!='2':
                print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
                sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
            sino=int(sino)
    
        print('\nTu información ha quedado de la siguiente manera:')
        print('Nombre completo: ', end=' ')
        for i in range(len(registro_alumno)-2):
            print(registro_alumno[i], end= ' ')
    
        print('\nFecha de nacimiento: ', registro_alumno[-2])
        print('\nCorreo electrónico: ', registro_alumno[-1])
        
        alumnos.append(registro_alumno)
        print('\nFelicidades '+ registro_alumno[0] + ', te has registrado exitosamente. \nEs un gusto tenerte aquí, dispuesto(a) a aprender.')
        
    print('\n¿Deseas registrar a alguien más?')
    print(sn)
    sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
    while sino!='1' and sino!='2':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
        sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
    
    sino=int(sino)
    while sino==1:
        registro_alumno=reg_alumno(registro_alumno)
        registro_completado=verif_registro(alumnos, variables_registro, registro_alumno)
        registro_arc(registro_completado,alumnos)
        print('¿Deseas registrar a alguien más?')
        print(sn)
        sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
        while sino!='1' and sino!='2':
            print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
            sino=input('Escribe el número de la opción que deseas llevar a cabo: ')
        sino=int(sino)
    cont_mod=0
    cont_ejer=0
    menu(cont_mod,cont_ejer)
    return alumnos

def registro_arc(registro_completado,alumnos):
    base_alumnos=open('base_alumnos.txt','w')
    
    for i in range(len(alumnos)):
        for j in range(len(alumnos[0])):
            base_alumnos.write(alumnos[i][j])
    base_alumnos.close()
    
        
def menu(cont_mod,cont_ejer):
    menu= """
Ahora que ya has realizado el proceso de registro, puedes comenzar tus ejercicios.
A continuación, se muestran las opciones disponibles.
    1. Estudiar temas específicos
    2. Realizar prueba tipo PISA
    3. Salir
    """
    print(menu)
    opc=input('Escribe el número de la opción que desees realizar: ')
    while opc!='1' and opc!='2' and opc!='3':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
        opc=input('Escribe el número de la opción que deseas llevar a cabo: ')
    opc=int(opc)
    if opc==1:
        menu_contenido1(opc,cont_mod,cont_ejer)
    elif opc==2:
        menu_contenido2(cont_mod,cont_ejer)
    else:
         porc=cont_mod/6
         porc=str(porc)
         cont_mod=str(cont_mod)
         cont_ejer=str(cont_ejer)
         print('Aprobaste ' + cont_mod + ' módulo(s), lo cual corresponde a un ' + porc + '% de los temas a practicar.')
         print('Completaste ' + cont_ejer + ' ejercicios correctos.')
         sys.exit('Fue un gusto trabajar contigo, hasta luego! :)')
        
        
def menu_contenido1(opc,cont_mod,cont_ejer):
    menu_temas= """
Estudiar y repasar temas con tiempo antes de un examen ayuda a obtener mejores resultados.
A continuación, se muestran los temas disponibles.
    1. Operaciones básicas
    2. Álgebra
    3. Geometría
    4. Funciones y gráficas
    5. Estadística
    6. Combinatoria y probabilidad
    7. Regresar
"""
    print(menu_temas)
    opc_temas=input('Escribe el número de la opción que desees realizar: ')
    while opc_temas!='1' and opc_temas!='2' and opc_temas!='3' and opc_temas!='4' and opc_temas!='5' and opc_temas!='6' and opc_temas!='7':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar.')
        print(menu_temas)
        opc_temas=input('Escribe el número de la opción que deseas llevar a cabo: ')
    
    opc_temas=int(opc_temas)
    while opc_temas!=7:
        print('\nPara lograr un mejor resultado, procura hacer todos tus procedimientos a mano, con el fin de irte preparando para la prueba.')
        estatus_resp=['RESPUESTA CORRECTA\n', 'RESPUESTA INCORRECTA\n']
        if opc_temas==1:
            print('\nHas decidido practicar OPERACIONES BÁSICAS. \nA continuación, se presentan ejercicios con sumas, restas, multiplicaciones y divisiones.')
            #En estos ejercicios, consideraré que en el peor de los casos, el usuario teclea un número incorrecto, pero NO otro tipo de dato
            cont_opbasicas=16
            print('\nSUMAS')
            #SUMA 1
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                suma_1=int(input(f'{num_1} + {num_2}= '))
                if suma_1==(num_1+num_2):
                    print(estatus_resp[0]) 
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #SUMA 2
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                suma_2=int(input(f'{num_1} + {num_2}= '))
                if suma_2==(num_1+num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #SUMA 3
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                suma_3=int(input(f'{num_1} + {num_2}= '))
                if suma_3==(num_1+num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #SUMA 4
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                suma_4=int(input(f'{num_1} + {num_2}= '))
                if suma_4==(num_1+num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            print('\nRESTAS')
            #RESTA 1
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                resta_1=int(input(f'{num_1} - {num_2}= '))
                if resta_1==(num_1-num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #RESTA 2
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                resta_2=int(input(f'{num_1} - {num_2}= '))
                if resta_2==(num_1-num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #RESTA 3
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                resta_3=int(input(f'{num_1} - {num_2}= '))
                if resta_3==(num_1-num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #RESTA 4
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                resta_4=int(input(f'{num_1} - {num_2}= '))
                if resta_4==(num_1-num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            
            print('\nMULTIPLICACIONES')
            #MULTIPLICACIÓN 1
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                multi_1=int(input(f'{num_1} * {num_2}= '))
                if multi_1==(num_1*num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #MULTIPLICACIÓN 2
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                multi_2=int(input(f'{num_1} * {num_2}= '))
                if multi_2==(num_1*num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #MULTIPLICACIÓN 3
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                multi_3=int(input(f'{num_1} * {num_2}= '))
                if multi_3==(num_1*num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #MULTIPLICACIÓN 4
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                multi_4=int(input(f'{num_1} * {num_2}= '))
                if multi_4==(num_1*num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            print('\nDIVISIONES')
            print('Para estos ejercicios, coloca SOLAMENTE el COCIENTE, es decir, las veces que el divisor cabe en el dividendo.')
            #DIVISIÓN 1
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                div_1=int(input(f'{num_1} ÷ {num_2}= '))
                if div_1==(num_1//num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #DIVISIÓN 2
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                div_2=int(input(f'{num_1} ÷ {num_2}= '))
                if div_2==(num_1//num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #DIVISIÓN 3
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                div_3=int(input(f'{num_1} ÷ {num_2}= '))
                if div_3==(num_1//num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            #DIVISIÓN 4
            cont=0
            while cont<3:
                num_1=random.randint(1,1000)
                num_2=random.randint(1,1000)
                div_4=int(input(f'{num_1} ÷ {num_2}= '))
                if div_4==(num_1//num_2):
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_opbasicas-=1
            
            cal_1=float((cont_opbasicas/16)*100)
            print(f'\nHas tenido {cont_opbasicas} respuesta(s) correcta(s), lo cual equivale a un {cal_1}% del total de ejercicios de esta sección.')
            if cal_1>80.00:
                print('FELICIDADES!, haz aprobado el Módulo 1.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 1. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
            
            menu_finmod(cont_mod,cont_ejer)
        
        elif opc_temas==2:
            print('Has decidido practicar ÁLGEBRA.' +
            '\nA continuación, se presentan ejercicios con ecuaciones lineales y cuadráticas, así como multiplicación de polinomios.')
            print('\nECUACIONES LINEALES')
            print('INSTRUCCIÓN: Despeja para cada variable.')
            cont_algebra=12
            #ECUACIÓN LINEAL 1
            cont=0
            while cont<3:
                lineal_1=input('3c + 3= 15 \n¿Cuánto vale c? ')
                if int(lineal_1)==4:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #ECUACIÓN LINEAL 2
            cont=0
            while cont<3:
                lineal_2=input('2x + 9= 27 \n¿Cuánto vale x? ')
                if int(lineal_2)==9:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #ECUACIÓN LINEAL 3
            cont=0
            while cont<3:
                lineal_3=input('5u + 125= 200 \n¿Cuánto vale u? ')
                if int(lineal_3)==15:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #ECUACIÓN LINEAL 4
            cont=0
            while cont<3:
                lineal_4=input('14y + 6= 90 \n¿Cuánto vale y? ')
                if int(lineal_4)==6:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            print('\nMULTIPLICACIÓN DE POLINOMIOS')
            print('INSTRUCCIÓN: Simplifica cada expresión.')
            print('CONSIDERACIONES AL ESCRIBIR TU RESPUESTA:' +
                  '\n1.- Utiliza el signo ^ para representar exponentes.' +
                  '\n2.- Escribe el resultado TODO JUNTO.' +
                  '\n3.- TODAS las variables se colocan en minúsculas.' +
                  '\n4.- Recuerda trabajar con la variable de cada ejercicio.' +
                  '\nEjemplo: 20b^4+29b^7' +
                  '\nEs muy IMPORTANTE escribir el resultado en el formato solicitado, de lo contrario se marcará comoo INCORRECTA.')
            
            #MULTI POLI 1
            cont=0
            while cont<3:
                multi_poli_1=input('5w(7w^4 + 3w^2) \n¿Cuál es el resultado de esta multiplicación? ')
                if multi_poli_1=='35w^5+15w^3':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #MULTI POLI 2
            cont=0
            while cont<3:
                multi_poli_2=input('6q(8q^9 + q^3) \n¿Cuál es el resultado de esta multiplicación? ')
                if multi_poli_2=='48q^10+6q^4':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #MULTI POLI 3
            cont=0
            while cont<3:
                multi_poli_3=input('3d(14d^2 + 3d) \n¿Cuál es el resultado de esta multiplicación? ')
                if multi_poli_3=='42d^3+9d^2':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #MULTI POLI 4
            cont=0
            while cont<3:
                multi_poli_4=input('23a(2a + 10a^7) \n¿Cuál es el resultado de esta multiplicación? ')
                if multi_poli_4=='46a^2+230a^8':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            
            print('\nECUACIONES CUADRÁTICAS')
            print('INSTRUCCIÓN: Encuentra los posibles valores para la incógnita.')
            print('CONSIDERACIONES AL ESCRIBIR TU RESPUESTA:' +
                  '\n1.- Escribe ambos valores, separados por una coma.' +
                  '\n2.- No utilices ningún espacio.' +
                  '\n3.- No te preocupes por el orden de los valores, cualquiera de los dos será correcto.' +
                  '\n4.- En caso de solo tener una solución, escribe el valor solo. Ejemplo: 9'+
                  '\nEjemplo para posibles valores de x: 5,1' +
                  '\nEs muy IMPORTANTE escribir el resultado en el formato solicitado, de lo contrario se marcará comoo INCORRECTA.')
            
            #CUADRÁTICAS 1
            cont=0
            while cont<3:
                cuad_1=input('x^2-5x+6=0 \n¿Cuáles son los posibles valores para x en esta ecuación? ')
                if cuad_1=='2,3' or cuad_1=='3,2':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #CUADRÁTICAS 2
            cont=0
            while cont<3:
                cuad_2=input('y^2-2y+1=0 \n¿Cuáles son los posibles valores para y en esta ecuación? ')
                if cuad_2=='1':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #CUADRÁTICAS 3
            cont=0
            while cont<3:
                cuad_3=input('x^2+(7-x)^2=25 \n¿Cuáles son los posibles valores para y en esta ecuación? ')
                if cuad_3=='4,3' or cuad_3=='3,4':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            #CUADRÁTICAS 4
            cont=0
            while cont<3:
                cuad_4=input('x^2-5x-84=0 \n¿Cuáles son los posibles valores para y en esta ecuación? ')
                if cuad_4=='12,-7' or cuad_4=='-7,12':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_algebra-=1
            
            cal_2=float((cont_algebra/12)*100)
            print(f'\nHas tenido {cont_algebra} respuestas correctas, lo cual equivale a un {cal_2}%.')
            if cal_2>80.00:
                print('FELICIDADES!, haz aprobado el Módulo 2.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 2. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
            
            menu_finmod(cont_mod,cont_ejer)
               
        elif opc_temas==3:
            print('Has decidido practicar GEOMETRÍA.' +
            '\nA continuación, se presentan ejercicios que involucran figuras y ángulos.')
            cont_geo=4
            
            #GEOMETRÍA 1
            cont=0
            while cont<3:
                geo_1=input("""
Nicolás quiere pavimentar el patio rectangular de su nueva casa. El patio mide 5,25 metros de largo y 3,00 metros de ancho.
Nicolás necesita 81 ladrillos por metro cuadrado.
Calcula cuántos ladrillos necesita Nicolás para pavimentar todo el patio.
Recuerda que no se pueden tener partes de un ladrillo. Pregúntate: ¿Hacia dónde tengo que redondear?
Respuesta: """)
                if geo_1=='1276':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_geo-=1
            
            #GEOMETRÍA 2
            cont=0
            print("""Para la solución de este ejercicio, se muestra una imagen externa. 
IMPORTANTE: Cuando estés seguro de tu respuesta, por favor, cierra la imagen y regresa al programa. 
Este te solicitará ingresar tu respuesta, pero ya no podrás visualizar el problema, así que NO OLVIDES tus respuestas.
RECOMENDACIÓN: Expande la imagen para verla completa""")
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                geop2=PhotoImage(file='geo2.png')
                fondo=Label(root,image=geop2).place(x=100,y=30,width='1200',height='900')
                root.mainloop()
                geo_2=input("""Ingresa el inciso de la figura que cumpla con las condiciones del problema.
PD: No te preocupes por mayúsculas o minúsculas, de cualquier forma la respuesta se te marcará como correcta, siempre y cuando la letra lo sea.
Respuesta: """)
                geo_2=geo_2.upper()
                if geo_2=='D':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_geo-=1
            
            #GEOMETRÍA 3
            cont=0
            while cont<3:
                geo_3=input("""
La estación espacial Mir permaneció en órbita 15 años y durante este tiempo dio aproximadamente 86.5 vueltas alrededor de la Tierra.
La permanencia más larga de un astronauta en la Mir fue de 680 días.
La Mir daba vueltas alrededor de la Tierra a una altura aproximada de 400 kilómetros. El diámetro de la Tierra mide aproximadamente 12,700 km y su circunferencia es de alrededor de 40,000 km (π × 12,700).
Calcula aproximadamente la distancia total recorrida por la Mir durante sus 86,500 vueltas mientras estuvo en órbita. Redondea el resultado a las decenas de millón.
Valores formato con y sin coma son aceptados, ejemplo: 5837 o 5,837.
Respuesta: """)
                
                if geo_3=='3680' or geo_3=='3,680':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_geo-=1
                
            #GEOMETRÍA 4
            cont=0
            print("""Para la solución de este ejercicio, se muestra una imagen externa. 
IMPORTANTE: Cuando estés seguro de tu respuesta, por favor, cierra la imagen y regresa al programa. 
Este te solicitará ingresar tu respuesta, pero ya no podrás visualizar el problema, así que NO OLVIDES tus respuestas.
RECOMENDACIÓN: Expande la imagen para verla completa.
Deberáss ingresar la medida del ángulo en grados""")
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                geop4=PhotoImage(file='geo4.png')
                fondo=Label(root,image=geop4).place(x=0,y=0,width='1450',height='1350')
                root.mainloop()
                geo_4=input('Medida del ángulo en grados: ')
                if geo_4=='120':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_geo-=1
            
            cal_3=float((cont_geo/4)*100)
            print(f'\nHas tenido {cont_geo} respuestas correctas, lo cual equivale a un {cal_3}%.')
            if cal_3>70.00:
                print('FELICIDADES!, haz aprobado el Módulo 3.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 3. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
            
            menu_finmod(cont_mod,cont_ejer)
               
        elif opc_temas==4:
            print("""Has decidido practicar FUNCIONES Y GRÁFICAS.
A continuación, se presentan ejercicios que te permitirán interpretar datos o gráficas para sacar conclusiones.""")
            cont_funciones=4
            print("""Para la solución de algunos de estos ejercicios, se muestra una imagen externa. 
IMPORTANTE: Cuando estés seguro de tu respuesta, por favor, cierra la imagen y regresa al programa. 
Este te solicitará ingresar tu respuesta, pero ya no podrás visualizar el problema, así que NO OLVIDES tus respuestas.
RECOMENDACIÓN: Expande la imagen para verla completa""")
            
            #FUNCIONES 1 
            cont=0
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                fun1=PhotoImage(file='func1.png')
                fondo=Label(root,image=fun1).place(x=0,y=0,width='1450',height='1125')
                root.mainloop()
                fun_1=input("""
Desde 1980 la estatura media de las chicas de 20 años ha aumentado 2.3 cm, hasta alcanzar los 170.6 cm.
¿Cuál era la estatura media de las chicas de 20 años en 1980 en centímetros?: """)
                if fun_1=='168,3' or fun_1=='168.3':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_funciones-=1
            
            #FUNCIONES 2 
            cont=0
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                fun2=PhotoImage(file='func2.png')
                fondo=Label(root,image=fun2).place(x=1,y=3,width='1500',height='1260')
                root.mainloop() 
                fun_2=float(input("""¿Cuál es la distancia aproximada desde la línea de salida hasta el comienzo del tramo
recto más largo que hay en la pista?. Ingresa un número decimal aproximado.
Resspuesta: """))
            
                if fun_2>1.2 and fun_2<1.6:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_funciones-=1
            
            #FUNCIONES 3 
            cont=0
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                fun3=PhotoImage(file='func3.png')
                fondo=Label(root,image=fun3).place(x=100,y=30,width='1300',height='1050')
                root.mainloop()

                fun_3=input('¿Cuál fue la velocidad máxima del coche durante el paseo en km/h? \nRespuesta: ')
                if fun_3=='60':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_funciones-=1
                
            #FUNCIONES 4 
            cont=0
            while cont<3:
                print("""Por razones de salud la gente debería limitar sus esfuerzos; por ejemplo al hacer deporte, para no superar una determinada frecuencia cardíaca.
Durante años la relación entre la máxima frecuencia cardíaca recomendada para una persona y su edad se describía mediante la fórmula siguiente:
Máxima frecuencia cardiaca recomendada = 220 – edad
Investigaciones recientes han demostrado que esta fórmula debería modificarse ligeramente. La nueva fórmula es la siguiente:
Máxima frecuencia cardiaca recomendada = 208 – (0,7 x edad)  """)
                fun_4=input("""\nUn artículo de periódico afirma:
“El resultado de usar la nueva fórmula en lugar de la antigua es que el máximo número recomendado de latidos cardíacos por minuto disminuye ligeramente para los
jóvenes y aumenta ligeramente para los mayores”.
¿A partir de qué edad aumenta la máxima frecuencia cardiaca recomendada como resultado de introducir la nueva fórmula?: """)
                if fun_4=='40' or fun_4=='41':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_funciones-=1
            
            cal_4=float((cont_funciones/4)*100)
            print(f'\nHas tenido {cont_funciones} respuestas correctas, lo cual equivale a un {cal_4}%.')
            if cal_4>70.00:
                print('FELICIDADES!, haz aprobado el Módulo 4.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 4. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
            
            menu_finmod(cont_mod,cont_ejer)
     
        elif opc_temas==5:
            print('Has decidido practicar ESTADÍSTICA.' +
            '\nA continuación, se presentan ejercicios relacionados con medias, rangos, así como deducciones a partir de la información provista.')
            cont_est=3
            
            #ESTADISTICA 1
            cont=0
            while cont<3:
                print("""
En el colegio de Irene, su profesora de ciencias les hace exámenes que se puntúan de 0 a 100.
Irene tiene una media de 60 puntos de sus primeros cuatro exámenes de ciencias. En el quinto examen sacó 80 puntos. """)
                est_1=input('¿Cuál es la media de las notas de Irene en ciencias después de los cinco exámenes?: ')
                if int(est_1)==64:
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_est-=1
            
            #ESTADISTICA 2
            cont=0
            while cont<3:
                print("""Un día, en clase de matemáticas, se mide la estatura de todos los alumnos.
La estatura media de los chicos es de 160 cm y la estatura media de las chicas es de 150 cm.
Elena ha sido la más alta (mide 180 cm). Pedro ha sido el más bajo (mide 130 cm).
Dos estudiantes faltaron a clase ese día, pero fueron a clase al día siguiente.
Se midieron sus estaturas y se volvieron a calcular las medias. Sorprendentemente, la
estatura media de las chicas y la estatura media de los chicos no cambió.""")
                est_2=input('Uno de los estudiantes es un chico y el otro es una chica. ¿Puede deducirse esta afirmación? Escribe S para sí y N para no: ')
                est_2=est_2.upper()
                if est_2=='N':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_est-=1
                
            #ESTADISTICA 3
            cont=0
            print("""
Para la solución de este ejercicio, se muestra una imagen externa. 
IMPORTANTE: Cuando estés seguro de tu respuesta, por favor, cierra la imagen y regresa al programa. 
Este te solicitará ingresar tu respuesta, pero ya no podrás visualizar el problema, así que NO OLVIDES tus respuestas.
RECOMENDACIÓN: Expande la imagen para verla completa""")
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                est3=PhotoImage(file='estad3.png')
                fondo=Label(root,image=est3).place(x=10,y=10,width='1500',height='1250')
                root.mainloop()
                est_3=input('¿Cuál fue el valor total (en millones de zeds) de las exportaciones de Zedlandia en 1998?: ')
                if est_3=='27,1' or est_3=='27.1':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_est-=1
                
            cal_5=float((cont_est/3)*100)
            print(f'\nHas tenido {cont_est} respuestas correctas, lo cual equivale a un {cal_5}%.')
            if cal_5>60.00:
                print('FELICIDADES!, haz aprobado el Módulo 5.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 5. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
           
            menu_finmod(cont_mod,cont_ejer)
                
        elif opc_temas==6:
            print("""
Has decidido practicar COMBINATORIA Y PROBABILIDAD.
A continuación, se presentan ejercicios con combinatoria y probabilidad.""")
            cont_combi=4
            #COMBI 1
            cont=0
            print("""
Para la solución de TODOS estos ejercicios, se muestra una imagen externa. 
IMPORTANTE: Cuando estés seguro de tu respuesta, por favor, cierra la imagen y regresa al programa. 
Este te solicitará ingresar tu respuesta, pero ya no podrás visualizar el problema, así que NO OLVIDES tus respuestas.
RECOMENDACIÓN: Expande la imagen para verla completa""")
            while cont<3:
                root = Tk() 
                root.geometry('700x500')
                comb1=PhotoImage(file='combi1.png')
                fondo=Label(root,image=comb1).place(x=1,y=0,width='1525',height='1500')
                root.mainloop()
                combi_1=input(("""
¿Cuál es la probabilidad de que Roberto extraiga un caramelo rojo?
Ingresa el porcentaje en número (sin el signo), ejemplo: 35
Respuesta: """))
                if combi_1=='20':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
                if cont==3:
                    cont_combi-=1
                
            #COMBI 2
            cont=0
            while cont<3:
                root = Tk()
                root.geometry('700x500')
                comb2=PhotoImage(file='combi2.png')
                fondo=Label(root,image=comb2).place(x=5,y=5,width='1500',height='940')
                root.mainloop()
                combi_2=input(("""¿Qué coche cumple las condiciones de Cris? 
PD: No te preocupes por mayúsculas o minúsculas, de cualquier forma la respuesta se te marcará como correcta, siempre y cuando el nombre del modelo lo sea.
Ejemplo: Dezal, dezal o DEZAL.
Respuesta: """))
                combi_2=combi_2.upper()
                if combi_2=='BOLTE':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_combi-=1
            
            #COMBI 3
            cont=0
            while cont<3:
                print('¿Cuántos CDs vendió el grupo Los Metalgaites en abril?')
                root = Tk() 
                root.geometry('700x500')
                comb3=PhotoImage(file='combi3.png')
                fondo=Label(root,image=comb3).place(x=0,y=0,width='1300',height='1100')
                root.mainloop()
                combi_3=input(("""
Ingresa un número entero paso la respuesta, en caso de ser de 4 dígitos, puedes usar comas, pero no es necesario. Ejemplo: 3942 o 3,942.
Respuesta: """))
                if combi_3=='500':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_combi-=1
                
            #COMBI 4
            cont=0
            while cont<3:
                print("""
En una pizzería se puede elegir una pizza básica con dos ingredientes: queso y tomate. También puedes diseñar tu propia pizza con ingredientes adicionales.
Se pueden seleccionar entre cuatro ingredientes adicionales diferentes: aceitunas, jamón, champiñones y salami.
Jaime quiere encargar una pizza con dos ingredientes adicionales diferentes. """)
                combi_4=input("""¿Cuántas combinaciones diferentes podría seleccionar Jaime?  """)
                if combi_4=='6':
                    print(estatus_resp[0])
                    cont_ejer+=1
                    break
                else:
                    print(estatus_resp[1])
                    cont+=1
            if cont==3:
                cont_combi-=1
            
            cal_6=float((cont_combi/4)*100)
            print(f'\nHas tenido {cont_combi} respuestas correctas, lo cual equivale a un {cal_6}%.')
            if cal_6>70.00:
                print('FELICIDADES!, haz aprobado el Módulo 6.')
                cont_mod+=1
            else:
                print('Lamentablemente no haz aprobado el Módulo 6. \nTe sugerimos volverlo a tomar para mejorar tu desempeño en esta sección.')
                
            menu_finmod(cont_mod,cont_ejer)
    menu(cont_mod,cont_ejer)

def menu_contenido2(cont_mod,cont_ejer):
    
    print('Prueba Tipo Pisa')
    print('Te recomendamos solucionar los siguientes problemas en una hoja aparte, trata de realizar los procedimientos.\n')
    
    file=open('pruebapisa.txt')
    lineas=file.readlines()
    for linea in lineas:
        print(linea)
    
    menu(cont_mod,cont_ejer)
    
def resultados(cont_mod,cont_ejer): #LLAMARLA BIEN EN CODIGOO
    print(f'Has aprobado {cont_mod} módulo(s), lo cual corresponde a un {(cont_mod/6)*100}% de los temas a practicar')
    print(f'Has realizado {cont_ejer} ejercicios correctos')
    
    porc=(cont_mod/6)*100
    cont_mod=str(cont_mod)
    cont_porcentaje=str(porc)
    cont_ejer=str(cont_ejer)
    
    result_alumno=open('result_alumno.txt','w')
    result_alumno.write(cont_mod)
    result_alumno.write(cont_porcentaje)
    result_alumno.write(cont_ejer)
    result_alumno.close()
    
    menu_finmod(cont_mod,cont_ejer)
    
def menu_finmod(cont_mod,cont_ejer):
    menu_temafinalizado=("""\n¿Qué deseas hacer a continuación?
1. Seguir practicando
2. Realizar prueba tipo PISA
3. Consultar módulos aprobados, ejercicios correctos y porcentajes
4. Regresar
""")
    print(menu_temafinalizado)
    opc_continuacion=input('Escribe el número de la opción que desees realizar: ')
    while opc_continuacion!='1' and opc_continuacion!='2' and opc_continuacion!='3' and opc_continuacion!='4':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar.')
        print(menu_temafinalizado)
        opc_continuacion=input('Escribe el número de la opción que deseas llevar a cabo: ')
    opc_continuacion=int(opc_continuacion)

    if opc_continuacion==1:
        menu_contenido1(opc_continuacion,cont_mod,cont_ejer)
    elif opc_continuacion==2:
        menu_contenido2(cont_mod,cont_ejer)
    elif opc_continuacion==3:
        resultados(cont_mod,cont_ejer)
    else:
        menu(cont_mod,cont_ejer)
  
def main():
    inicio = """
Hola!,
Este es un programa que tiene como objetivo apoyar a los estudiantes de 15 años a mejorar sus habilidades y conocimientos en el área de
matemáticas, los cuales evalúa la prueba PISA de la OCDE.
De acuerdo con el artículo “Resultados PISA 2018: Latinoamérica por debajo del promedio”: en México casi un millón y medio de jóvenes
participaron en la prueba, y los resultados muestran que "los estudiantes tienen dificultades  en aspectos básicos de lectura" y que
"solo el 1% de los estudiantes mexicanos obtuvo un desempeño sobresaliente en lectura, matemáticas y ciencia".

¿Estás listo para incrementar ese 1%?

Antes de comenzar a practicar, es importante que te encuentres registrado(a), ¿ya lo estás?
    1. Sí
    2. No
    """ 
    print(inicio)
    opc=input('Escribe el número de la opción que corresponda a tu respuesta: ')
    while opc!='1' and opc!='2':
        print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda escribir 1 para Sí y 2 para No.')
        opc=input('Escribe el número de la opción que deseas llevar a cabo: ')
    opc=int(opc)
    
    alumnos=[]
    alumno_registrado=[]
    variables_registro=['Nombre', 'Segundo nombre', 'Apellido paterno', 'Apellido materno', 'Correo electrónico']
    
    
    if opc==2:
        registro_alumno=reg_alumno(alumno_registrado)
        registro_completado=verif_registro(alumnos, variables_registro, registro_alumno)
        registro_arc(registro_completado,alumnos)
    else:
        print('HOLA')
        nombre=input('Escribe tu primer nombre: ')
        apellido=input('Escribe tu apellido paterno: ')
        correo=input('Escribe tu correo electrónico: ')
        
        renglones=len(alumnos)
        columnas=len(alumnos[0])
        if renglones==0:
            print('No te encuentras registrado.')
        else:
            columnas=len(alumnos[0])
            for ren in range(renglones):
                for col in range(columnas):
                    if correo in alumnos[ren][col]==True:
                        print('fBienvenido(a) {nombre} {apellido}, es un gusto tenerte de nuevo por aquí.')
                        menu(cont_mod,cont_ejer)
                        
                    else:
                        print('Lo siento, tu registro no ha sido encontrado.')
                        revision_reg="""A continuación, te mostramos las opciones disponibles.
1. Volver a escribir tus datos por si hubo un error
2. Registrarte"""
                        print(revision_reg)
                        opc_reg=input('Escribe el número de la opción que deseas llevar a cabo: ')
                        while opc_reg!='1' and opc_reg!='2':
                            print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda solamente escribir 1 o 2.')
                            opc_reg=input('Escribe el número de la opción que deseas llevar a cabo: ')
                        opc_reg=int(opc_reg)
                        
                        while opc_reg==1:
                            print(revision_reg)
                            opc_reg=input('Escribe el número de la opción que deseas llevar a cabo: ')
                            while opc_reg!='1' and opc_reg!='2':
                                print('El caracter seleccionado es incorrecto, por favor, vuelve a intentar. \nRecuerda solamente escribir 1 o 2.')
                                opc_reg=input('Escribe el número de la opción que deseas llevar a cabo: ')
                            opc_reg=int(opc_reg)
                            
        registro_alumno=reg_alumno(alumno_registrado)
        registro_completado=verif_registro(alumnos, variables_registro, registro_alumno)
        registro_arc(registro_completado,alumnos)
        
        cont_mod=0
        cont_ejer=0
        menu(cont_mod,cont_ejer)

    
main()
