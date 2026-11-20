import json 

def guardar_tareas(tareas):
    with open('tareas.json', 'w', encoding='utf-8') as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)

def cargar_tareas():
    try:
        with open('tareas.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

            if isinstance(datos, list):
                if all(isinstance(tarea, str) for tarea in datos):
                    return datos

            print('Error: el archivo no contiene una lista válida de tareas.')
            return []

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print('Error: el archivo JSON está vacío o tiene un formato incorrecto.')
        return []

def anadir_tarea(tareas, tarea):
    if tarea == '':
        return 'vacía'
    elif tarea in tareas:
        return 'dupe'
    else:
        tareas.append(tarea)
        guardar_tareas(tareas)
        return 'anadida'

def eliminar_tarea(tareas, elim):
    if elim in tareas:
        tareas.remove(elim)
        guardar_tareas(tareas)
        return True
    return False

def mostrar_tareas(tareas):
    cont = 1
    if len(tareas) == 0:
        print('No tienes tareas que mirar!')
    else:
        for i in tareas:
            print('TAREA nª', cont, i)
            cont += 1

def mostrar_menu():
    print('*1 - AÑADIR UNA TAREA A LA LISTA*')
    print('*2 . ELIMINAR UNA TAREA DE LA LISTA*')
    print('*3 - MIRAR TU LISTA DE TAREAS*')
    print('*0 - SALIR DE FOCUSQUEST*')
    print('Disclaimer: cualquier otro número que no sea 1 2 y 3 no obtendrá respuesta')

def main(tareas):

    print('*BIENVENIDO A FOCUSQUEST*')
    print('*Tu programa para asignación, eliminación y listado de tareas*')
    print('*¿Qué quieres hacer hoy?*')

    mostrar_menu()

    res = input('')

    while res != '0':
        if res == '1':
            while input('¿Quieres añadir una tarea?').strip() == 'sí':
                tarea = input('describe la tarea:').strip()
                resultado = anadir_tarea(tareas, tarea)
                if resultado == 'anadida':
                    print('Se ha añadido la tarea.')
                elif resultado == 'dupe':
                    print('La tarea ya existe.')
                elif resultado == 'vacía':
                    print('La tarea no tiene contenido.')
        elif res == '2':
            if len(tareas) == 0:
                print('No tienes tareas que eliminar!')
            else:
                elim = input('¿Qué tarea quieres eliminar?').strip()
                if eliminar_tarea(tareas, elim) == True:
                    print('La tarea', elim, 'se ha eliminado.')
                else:
                    print('La tarea no se ha encontrado.')


        elif res == '3':
            mostrar_tareas(tareas)
        else:
            print('Opción no válida. Prueba otro comando!')
        mostrar_menu()
        res = input('¿Qué quieres hacer ahora?')
if __name__ == "__main__":
    tareas = cargar_tareas()
    main(tareas)
#prueba dia 16
#prueba dia 17 !!!
# Mejora experimental del menú - Día 18
# Versión de master: menú actualizado