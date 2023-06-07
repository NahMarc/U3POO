from ManejaEmpleados import ManejadorEmpleados


if __name__ == "__main__":
    ManejaEmpleados = ManejadorEmpleados()
    print("la cantidad ingresada debe ser el total de empleados que esta en los archivo")
    cantidad = int(input("Ingresar cantidad total de Empleados: "))
    ManejaEmpleados = ManejadorEmpleados(cantidad)
    ManejaEmpleados.coleccion()
    print("1):Registar Horas")
    dni = int(input("Ingresar dni del empleado: "))
    hora = int(input("Ingresar horas actuales: "))
    ManejaEmpleados.item1(dni, hora)
    print("2):Total de tareas/arreglar/")
    tarea = str(input("Ingresar tarea: "))
    ManejaEmpleados.item2(tarea)
    print("3):Ayuda.")
    ManejaEmpleados.item3()
    print("4):Calcular sueldo")
    ManejaEmpleados.item4()
