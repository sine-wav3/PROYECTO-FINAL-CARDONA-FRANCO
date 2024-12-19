# Docente: Luis German Toro Pareja
# Proyecto Final 
# Numero del grupo: 9

#miembros del grupo:
# integrante 1: Nicolas Cardona Garcia - 2477349
# integrante 2: Daniela Franco Ibarra - 2477154

# Datos predeterminados de las materias y créditos ya que solo es para el primer semestre


subjects = {
    "111023C": {"name": "Matemáticas Basicas", "credits": 3},
    "404002C": {"name": "Deporte y Salud", "credits": 2},
    "750012C": {"name": "Fundamentos de Programación Imperativa", "credits": 3},
    "701002C": {"name": "Taller de Ingeniería", "credits": 3},
    "701001C": {"name": "Inserción a la Vida Universitaria", "credits": 2},
    "701003C": {"name": "Introducción a la Ingeniería", "credits": 2}
}

students = [] # estudiantes almacenados

def main(): #Funcion del menu 
    while True:
        try:
            option = input("""
=====================================
            BIENVENIDO
         ESCOGE UNA OPCIÓN:
=====================================
        1. Crear estudiantes
        2. Buscar estudiantes
        3. Actualizar estudiantes
        4. Calcular promedio ponderado
        5. Filtrar estudiantes
        6. Eliminar estudiantes
        7. Cargar archivo
        8. Salir                   
=====================================
Elija una opcion: """) #opciones que redirigen al usuario hacia la funcion enumerada que prefiera
            if option == "1":
                create_students()
            elif option == "2":
                search()
            elif option == "3":
                update()
            elif option == "4":
                average_grade()
            elif option == "5":
                filter_students()
            elif option == "6":
                delete()
            elif option == "7": # Cargar estudiantes desde archivo
                load_students_from_file()
            elif option == "8":
                print("Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}. Intente nuevamente.") #excepcion principal de todas las funciones, si falla algo se redirige al menu.
        except KeyboardInterrupt:
            print("No use ctrl + c, elija una opcion valida.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")


# Crear estudiantes 
def create_students():
    print("\n--- Crear Estudiante ---")
    while True:
        try:
            name = input("Ingrese el nombre del estudiante: ")
            if not name.replace(" ", "").isalpha(): #metodo .isalpha para no permitir que el usuario ingrese un codigo con strings
                print("El nombre solo deben contener letras.")
                continue
            break
        except (ValueError, KeyboardInterrupt):
            print("informacion invalida, intentelo otra vez.")
    
    while True:
        try:
            code_students = input("Ingrese el código del estudiante (solo números): ")
            if not code_students.isdigit(): #metodo .isdigit para confirmar que el codigo si es numerico
                raise ValueError("El código debe ser numérico.")
            code_students = int(code_students)
            if any(est["code_students"] == code_students for est in students):
                raise ValueError("Ya existe un estudiante con este código.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
        except (KeyboardInterrupt, EOFError):
            print("Operación interrumpida. Por favor, intente nuevamente.")


    grades = {}
    for code_subject, data_subject in subjects.items(): #se accede a los items del diccionario a traves de los iteradores para los valores de las llaves
        while True:
            try:
                try:
                    grade = float(input(f"Ingrese la nota para {data_subject['name']} ({code_subject}) (0.0 - 5.0): "))
                except ValueError:
                    print("ingrese un dato valido.")
                    continue 
                if 0.0 <= grade <= 5.0:
                    grades[code_subject] = grade
                    break
                else:
                    print("La nota debe estar entre 0.0 y 5.0.")
                if grade is KeyboardInterrupt:
                    print("Entrada invalida.")
                elif grade is ValueError:
                    print("Entrada invalida.")
                else: 
                    continue 
            except (KeyboardInterrupt, ValueError):
                print("Entrada invalida.")

    students.append({"name": name, "code_students": code_students, "grades": grades})
    print("Estudiante creado exitosamente.")


# Eliminar estudiante
def delete():
    print("\n--- Eliminar Estudiante ---")
    code_students = input("Ingrese el código del estudiante que desea eliminar: ")
    student = next((est for est in students if est["code_students"] == code_students), None)

    if student:
        students.remove(student)
        print(f"Estudiante con código {code_students} eliminado exitosamente.")
    else:
        print("Estudiante no encontrado.")


# Buscar estudiantes divido en dos opciones
def search():
    print("\n--- Buscar Estudiantes ---")
    while True:
        try:
            option = input("1. Buscar por código\n2. Mostrar todos\n3. Volver al menú principal\nSeleccione una opción: ")
        except (KeyboardInterrupt, ValueError):
            print("ingrese una opcion valida.")
            break 
        if option == "1":
            try:
                code_students = int(input("Ingrese el código del estudiante: "))
            except (KeyboardInterrupt, ValueError):
                print("Dato invalido, vuelve a intentar.")
                break
            student = next((est for est in students if est["code_students"] == code_students), None)
            if student in students:
                show_student(student)
            elif student not in students:
                print("Estudiante no encontrado.")
                break 
        elif option == "2":
            if students:
                for student in students:
                    show_student(student)
                break 
            else:
                print("No hay estudiantes registrados.")
                break
        elif option == "3":
            print("Volviendo al menú principal.")
            main()
            break
        else:
            print("Opción inválida.")
            break 
    while True:
        try:
            opt = input("¿desea volver a buscar? s/n: ") #opt = option
        except (KeyboardInterrupt, ValueError):
            print("opcion invalida, vuelvalo a intentar.")
            break
        if opt.lower() == "s": 
            search()
        elif opt.lower() == "n":
            break
        else:
            print("Opción inválida, intentalo otra vez")

# con esto se busca mostrar la información de un estudiante o de varios dependiendo e la opcion de arriba
def show_student(student):
    print(f"\nNombre: {student['name']}\nCódigo: {student['code_students']}")
    for code_subject, grade in student["grades"].items():
        subject = subjects[code_subject]["name"]
        print(f"  {subject} ({code_subject}): {grade}")
        
def load_students_from_file():
    print("\n--- Cargar Estudiantes desde Archivo ---")
    file_path = input("Ingrese la ruta del archivo .txt: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file: #con enconding se asegura que se pueda desencriptar el archivo correctamente
            for line in file:
                data = line.strip().split(',') #se quitan las comas que separan las llaves y los valores del archivo "NotasEstudiantesDeIngenieria2"
                if len(data) < 2: # respecto a lo anterior, solo se puede cargar el archivo 2 y no el 1. 
                    print(f"Línea ignorada: {line.strip()} (datos insuficientes)")
                    continue

                code_students = (data[0].strip())
                if any(est["code_students"] == code_students for est in students):
                    print(f"Ya existe un estudiante con este código: {code_students}")
                    continue

                code_students = data[0].strip()
                name = data[1].strip()
                grades = {}

                try:
                    for i in range(2, len(data), 4):
                        subject_name = data[i].strip()
                        subject_code = data[i + 1].strip()
                        grade = float(data[i + 2].strip())
                        credits = int(data[i + 3].strip())

                        if subject_code in subjects and 0.0 <= grade <= 5.0:
                            grades[subject_code] = grade
                        else:
                            print(f"Datos inválidos para la materia {subject_name} ({subject_code}).")
                            break
                    else:
                        students.append({"name": name, "code_students": code_students, "grades": grades})
                        print(f"Estudiante {name} cargado exitosamente.")
                except (ValueError, IndexError):
                    print(f"Línea malformada: {line.strip()}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente nuevamente.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        

# Actualizar datos de los estudiantes
def update(): 
    print("\n--- Actualizar Estudiantes ---")
    code_students = input("Ingrese el código del estudiante: ")
    student = next((est for est in students if str(est["code_students"]) == code_students), None)

    if student:
        while True:
            print("\n1. Actualizar nombre")
            print("2. Actualizar notas")
            print("3. Regresar al menú principal")
            option = input("Seleccione una opción: ")

            if option == "1":
                new_name = input("Ingrese el nuevo nombre: ")
                if new_name.strip():
                    student["name"] = new_name.strip()
                    print("Nombre actualizado exitosamente.")
                else:
                    print("El nombre no puede estar vacío. Intente nuevamente.")
                break  # Salir después de actualizar

            elif option == "2":
                while True:
                    code_subject = input("Ingrese el código de la subject que desea actualizar: ").upper()
                    if code_subject in student["grades"]:
                        while True:
                            try:
                                new_grade = float(input("Ingrese la nueva nota (0.0 - 5.0): "))
                                if 0.0 <= new_grade <= 5.0:
                                    student["grades"][code_subject] = new_grade
                                    print("Nota actualizada exitosamente.")
                                    break  # Salir del bucle de ingreso de nota
                                else:
                                    print("La nota debe estar entre 0.0 y 5.0. Intente nuevamente.")
                            except ValueError:
                                print("Entrada invalida válido.")
                    else:
                        print("El código de la materia no existe en los registros del estudiante.")

                    # Preguntar si quiere actualizar otra nota
                    continue_updating = input("¿Desea actualizar otra nota? (s/n): ").lower()
                    if continue_updating != "s":
                        break  # Salir del bucle de actualización de notas
                break  # Salir después de intentar actualizar

            elif option == "3":
                print("Regresando al menú principal.")
                break  # Salir al menú principal

            else:
                print("Opción inválida. Intente nuevamente.")
    else:
        print("Estudiante no encontrado. Verifique el código ingresado.")



# Promedio ponderado de un estudiante
def average_grade():
    print("\n--- Calcular Promedio Ponderado ---")
    code_students = int(input("Ingrese el código del estudiante: "))
    student = next((est for est in students if est["code_students"] == code_students), None)

    if student:
        total_points = sum(student["grades"][code_subject] * data_subject["credits"] for code_subject, data_subject in subjects.items())
        total_credits = sum(data_subject["credits"] for data_subject in subjects.values())
        promedio_ponderado = total_points / total_credits
        print(f"Promedio ponderado: {promedio_ponderado:.2f}")
    else:
        print("Estudiante no encontrado.")
        #solo se calcula el promedio ponderado de un solo estudiante y es el que elija 

# filtro de estudiantes dividido en dos opciones
def filter_students():
    print("\n--- Filtrar Estudiantes ---")
    print("1. Ordenar por promedio ponderado (mayor a menor)")
    print("2. Mostrar mejor nota de cada estudiante")
    option = input("Seleccione una opción: ")

    if option == "1": # ordenar por promedio ponderado
        averages = []
        for student in students:
            total_points = sum(student["grades"][code_subject] * data_subject["credits"] for code_subject, data_subject in subjects.items())
            total_credits = sum(data_subject["credits"] for data_subject in subjects.values())
            average_grade = total_points / total_credits
            averages.append((average_grade, student))

        averages.sort(reverse=True, key=lambda x: x[0])
        for average_grade, student in averages:
            print(f"{student['name']} ({student['code_students']}): Promedio ponderado: {average_grade:.2f}")

    elif option == "2": # mostrar mejor nota de cada estudiante
        for student in students:
            better_subject_code = max(student["grades"], key=student["grades"].get)
            better_grade = student["grades"][better_subject_code]
            better_subject_name = subjects[better_subject_code]["name"]
            print(f"{student['name']} ({student['code_students']}): Mejor nota en {better_subject_name} ({better_subject_code}): {better_grade}")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()