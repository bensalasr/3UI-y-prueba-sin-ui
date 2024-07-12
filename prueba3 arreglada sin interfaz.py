import csv
import easygui

def verificar_rut(rut):
    rut = rut.replace('.', '').replace('-', '')
    numero = rut[:-1]
    digito_verificador = rut[-1].upper()

    if len(numero) < 7 or len(numero) > 8:
        return False

    reverso = numero[::-1]
    total = 0
    factor = 2

    for char in reverso:
        total += int(char) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_calculado = 11 - (total % 11)
    if digito_calculado == 11:
        digito_calculado = '0'
    elif digito_calculado == 10:
        digito_calculado = 'K'
    else:
        digito_calculado = str(digito_calculado)

    return digito_calculado == digito_verificador

def exportar_a_csv(estudiantes_aprobados, estudiantes_reprobados):
    archivo_aprobados = 'aprobados.csv'
    archivo_reprobados = 'reprobados.csv'

    with open(archivo_aprobados, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "rut", "nota 1", "nota 2", "nota 3", "nota 4", "promedio"])
        for estudiante in estudiantes_aprobados:
            escritor.writerow(estudiante)

    with open(archivo_reprobados, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "rut", "nota 1", "nota 2", "nota 3", "nota 4", "promedio"])
        for estudiante in estudiantes_reprobados:
            escritor.writerow(estudiante)

def buscar_estudiante(rut, lista_datos):
    for estudiante in lista_datos:
        if estudiante[1] == rut:
            return estudiante
    return None

def agregar_estudiante(lista_datos):
    while True:
        easygui.msgbox("ingrese los datos del estudiante", "Agregar estudiante")
        nombre = easygui.enterbox("nombre:")
        rut = easygui.enterbox("rut (formato 12345678-9):")

        if not verificar_rut(rut):
            easygui.msgbox("rut invalido. intente nuevamente.", "Error")
            continue

        try:
            nota1 = float(easygui.enterbox("nota 1:"))
            nota2 = float(easygui.enterbox("nota 2:"))
            nota3 = float(easygui.enterbox("nota 3:"))
            nota4 = float(easygui.enterbox("nota 4:"))
        except ValueError:
            easygui.msgbox("error: por favor, ingrese notas validas.", "Error")
            continue

        promedio = (nota1 + nota2 + nota3 + nota4) / 4
        estado = "aprobado" if promedio >= 4 else "reprobado"

        datos_estudiante = [nombre, rut, nota1, nota2, nota3, nota4, promedio]
        lista_datos.append(datos_estudiante)

        easygui.msgbox(f"el estudiante {nombre} ({rut}) esta {estado} con un promedio de {promedio:.2f}.", "Resultado")

        if easygui.ccbox("estudiante ingresado correctamente. ¿Desea agregar otro?", choices=("Sí", "No")):
            continue
        else:
            break

def ver_todos_estudiantes(lista_datos):
    if not lista_datos:
        easygui.msgbox("no hay estudiantes registrados.", "Información")
    else:
        mensaje = "\n".join([
            f"nombre: {estudiante[0]}, rut: {estudiante[1]}, nota 1: {estudiante[2]}, nota 2: {estudiante[3]}, nota 3: {estudiante[4]}, nota 4: {estudiante[5]}, promedio: {estudiante[6]:.2f}"
            for estudiante in lista_datos
        ])
        easygui.msgbox(mensaje, "Todos los estudiantes")

def menu():
    lista_datos = []
    
    while True:
        opciones = [
            "agregar estudiante",
            "ver todos los estudiantes",
            "buscar estudiante por rut",
            "exportar a csv",
            "salir"
        ]
        opcion = easygui.buttonbox("menu:", choices=opciones)

        if opcion == "agregar estudiante":
            agregar_estudiante(lista_datos)
        elif opcion == "ver todos los estudiantes":
            ver_todos_estudiantes(lista_datos)
        elif opcion == "buscar estudiante por rut":
            rut = easygui.enterbox("ingrese el rut del estudiante a buscar (formato 12345678-9):")
            estudiante = buscar_estudiante(rut, lista_datos)
            if estudiante:
                easygui.msgbox(f"estudiante encontrado: nombre: {estudiante[0]}, rut: {estudiante[1]}, nota 1: {estudiante[2]}, nota 2: {estudiante[3]}, nota 3: {estudiante[4]}, nota 4: {estudiante[5]}, promedio: {estudiante[6]:.2f}", "Resultado")
            else:
                easygui.msgbox("estudiante no encontrado.", "Resultado")
        elif opcion == "exportar a csv":
            estudiantes_aprobados = [e for e in lista_datos if e[6] >= 4]
            estudiantes_reprobados = [e for e in lista_datos if e[6] < 4]

            exportar_a_csv(estudiantes_aprobados, estudiantes_reprobados)
            easygui.msgbox("datos exportados a csv correctamente.", "Información")
        elif opcion == "salir":
            break

menu()
