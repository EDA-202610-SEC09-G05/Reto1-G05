import sys
from tabulate import tabulate
from DataStructures.List import array_list as al
from DataStructures.Set import set as s
from App import logic as l
 
def new_logic():
    """
        Se crea una instancia del controlador
    """
    return l.new_logic()
    

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def print_load_data(control, size):
    """
    Carga los datos
    """
    data, dtime, min_precio, max_precio = l.load_data(control, size)
    size = al.size(data["computer"])
    primeros = al.sub_list(data["computer"], 0, 5)
    ultimos = al.sub_list(data["computer"], size-5, size)


    # ===== Resumen de carga =====
    print("\n" + "=" * 80)
    print("RESUMEN DE CARGA")
    print("=" * 80)

    resumen = [
        ["Tiempo de carga (ms)", round(dtime,2)],
        ["Total computadores cargados", size],
    ]

    print(tabulate(resumen, headers=["Campo", "Valor"], tablefmt="fancy_grid"))

    # ===== Mayor precio (formato visual tipo "celdas combinadas") =====
    print("\n" + "-" * 80)
    print("MAYOR PRECIO")
    print("-" * 80)

    rows_mayor = [
        ["Modelo", max_precio["model"]],
        ["Marca", max_precio["brand"]],
        ["Año", max_precio["release_year"]],
        ["OS", max_precio["os"]],
        ["Precio", max_precio["price"]],
    ]

    print(tabulate(rows_mayor, tablefmt="fancy_grid"))

    # ===== Menor precio (mismo formato) =====
    print("\n" + "-" * 80)
    print("MENOR PRECIO")
    print("-" * 80)

    rows_menor = [
        ["Modelo", min_precio["model"]],
        ["Marca", min_precio["brand"]],
        ["Año", min_precio["release_year"]],
        ["OS", min_precio["os"]],
        ["Precio", min_precio["price"]],
    ]

    print(tabulate(rows_menor, tablefmt="fancy_grid"))

    # ===== Primeros 5 =====
    print("\n" + "=" * 80)
    print("PRIMEROS 5 REGISTROS")
    print("=" * 80)

    headers = ["Modelo", "Marca", "Año", "CPU", "GPU", "Precio"]
    rows_primeros = []

    for comp in al.to_py_list(primeros):
        rows_primeros.append([
            comp["model"],
            comp["brand"],
            comp["release_year"],
            comp["cpu_brand"],
            comp["gpu_brand"],
            comp["price"]
        ])

    print(tabulate(rows_primeros, headers=headers, tablefmt="fancy_grid", showindex=False))

    # ===== Últimos 5 =====
    print("\n" + "=" * 80)
    print("ÚLTIMOS 5 REGISTROS")
    print("=" * 80)

    rows_ultimos = []

    for comp in al.to_py_list(ultimos):
        rows_ultimos.append([
            comp["model"],
            comp["brand"],
            comp["release_year"],
            comp["cpu_brand"],
            comp["gpu_brand"],
            comp["price"]
        ])

    print(tabulate(rows_ultimos, headers=headers, tablefmt="fancy_grid", showindex=False))
    return data


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    while True:
        marca = input("Ingrese la marca del computador: ").lower()
        if marca in control["brand"]:
            break
        print("Marca no encontrada, vuelva a ingresar.\n")
    
    lista_estadisticas, lista_modelos = l.req_1(control, marca)
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 1")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("MODELOS EXTREMOS POR PRECIO")
    print("-" * 80)
    print(tabulate(lista_modelos, headers=["Tipo", "Modelo", "Precio"], tablefmt="fancy_grid"))
    return control


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    while True:
        pmin = input("Ingrese el precio mínimo: ")
        pmax = input("Ingrese el precio máximo: ")
        if pmin.replace(".","",1).isdigit() and pmax.replace(".","",1).isdigit() and float(pmin) <= float(pmax):
            break
        print("Precios no válidos, vuelva a ingresar.\n")
    lista_estadisticas, menor_precio, mayor_precio, mas_moderno = l.req_2(control, pmin, pmax)
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 2")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("COMPUTADOR MENOR PRECIO")
    print("-" * 80)
    print(tabulate(menor_precio, tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("COMPUTADOR MAYOR PRECIO")
    print("-" * 80)
    print(tabulate(mayor_precio, tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("COMPUTADOR MÁS MODERNO")
    print("-" * 80)
    print(tabulate(mas_moderno, tablefmt="fancy_grid"))
        
    return control


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    while True:
        cpu_brand = input("Ingrese la marca de la CPU: ").lower()
        cpu_tier = input("Ingrese el tier de la CPU: ")
        if cpu_brand in control["brandCPU"] and cpu_tier in ["1", "2", "3", "4", "5", "6"]:
            break
        print("Marca o tier no válidos, vuelva a ingresar.\n")
    lista_estadisticas = l.req_3(control, cpu_brand, cpu_tier)
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 3")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    
    return control


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    while True:
        cpu_brand = input("Ingrese la marca de la CPU: ").lower()
        gpu_brand = input("Ingrese la marca de la GPU: ").lower()
        if cpu_brand in control["brandCPU"] and s.is_in(control["brandGPU"], gpu_brand):
            break
        print("Marca no válida, vuelva a ingresar.\n")
    lista_estadisticas, top1, top2 = l.req_4(control, cpu_brand, gpu_brand)
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 4")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("TOP 1 COMPUTADOR")
    print("-" * 80)
    print(tabulate(top1, tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("TOP 2 COMPUTADOR")
    print("-" * 80)
    print(tabulate(top2, tablefmt="fancy_grid"))
    
    return control


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    while True:
        resolucion = input("Ingrese la resolución (ej: 1920x1080): ")
        bool_input = input("Filtro por (CARO/BARATO): ").lower()
        year_min = input("Ingrese el año mínimo: ")
        year_max = input("Ingrese el año máximo: ")
        if s.is_in(control["resolution"], resolucion) and bool_input in ["caro", "barato"] and year_min.isdigit() and year_max.isdigit() and int(year_min) <= int(year_max):
            break
        print("Resolución o filtro o año no válida, vuelva a ingresar.\n")
    
    boolean = True if bool_input == "caro" else False
    lista_estadisticas, precio = l.req_5(control, boolean, resolucion, int(year_min), int(year_max))
    
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 5")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("COMPUTADOR MAS CARO" if boolean else "COMPUTADOR MÁS BARATO")
    print("-" * 80)
    print(tabulate(precio, tablefmt="fancy_grid"))

    return control


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    while True:
        year_min = input("Ingrese el año mínimo: ")
        year_max = input("Ingrese el año máximo: ")
        if year_min.isdigit() and year_max.isdigit() and int(year_min) <= int(year_max):
            break
        print("Año no válido, vuelva a ingresar.\n")
 
    lista_estadisticas, mejor_os, os_estadisticas = l.req_6(control, int(year_min), int(year_max))
    print("\n" + "=" * 80)
    print("RESULTADO REQUERIMIENTO 6")
    print("=" * 80)
    print(tabulate(lista_estadisticas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("SISTEMA OPERATIVO MEJOR CLASSIFICADO")
    print("-" * 80)
    print(tabulate(mejor_os, headers=["Campo", "OS", "Cantidad", "Recaudo"], tablefmt="fancy_grid"))
    print("\n" + "-" * 80)
    print("ESTADÍSTICAS DE LOS SISTEMAS OPERATIVOS")
    print("-" * 80)
    print(tabulate(os_estadisticas, headers=["OS", "Precio Promedio", "Peso Promedio", "Computador mas Costoso", "Computador mas Barato"], tablefmt="fancy_grid", floatfmt=".2f"))

    return control

def tiempo(t):
    """
        Función que imprime el tiempo de ejecución de un requerimiento
    """
    print(f"Tiempo de ejecución: {t} ms")

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            while True:
                opcion = input("Ingrese el número del tamaño de los datos a cargar: 1-small  2-medium  3-large ")
                if opcion in ["1", "2", "3"]:
                    break
                print("Opción errónea, vuelva a elegir.\n")
            print("Cargando información de los archivos ....\n")
            
            size = "small" if opcion == "1" else "medium" if opcion == "2" else "large"
            print_load_data(control, size)
            
            
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)