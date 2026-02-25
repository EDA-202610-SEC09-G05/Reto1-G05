import time
import csv
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.List import sort as s

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "computer": al.new_list(),
        "brandCPU": {},
        "year": {},
        "brand": {}
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, size):
    """
    Carga los datos del reto
    """
    inicio = get_time()
    url = f"./Data/computer_prices_{size}.csv"
    max_precio = {"price":float("-inf")}
    min_precio = {"price":float("inf")}
    
    with open(url, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    
    for comp in filas:
        al.add_last(catalog["computer"], comp)
        load_brands(catalog, comp)
        load_years(catalog, comp)
        load_brands_cpu(catalog, comp)
        
        if float(comp["price"]) < float(min_precio["price"]):
            min_precio = comp
        if float(comp["price"]) > float(max_precio["price"]):
            max_precio = comp
        
    dtime = delta_time(inicio, get_time())
    return catalog, dtime, min_precio, max_precio

def load_brands(catalog, comp):
    """
    Carga las marcas de los computadores
    """
    brands = catalog["brand"]
    brand = comp["brand"]
    
    if brand not in brands:
        brands[brand] = sl.new_list()
    sl.add_last(brands[brand], comp)
    return catalog

def load_years(catalog, comp):
    """
    Carga los años de los computadores
    """
    years = catalog["year"]
    year = comp["release_year"]
    
    if year not in years:
        years[year] = sl.new_list()
    sl.add_last(years[year], comp)
    return catalog

def load_brands_cpu(catalog, comp):
    """
    Carga las marcas de los CPU de los computadores
    """
    brands = catalog["brandCPU"]
    brand = comp["cpu_brand"]
    
    if brand not in brands:
        brands[brand] = al.new_list()
    al.add_last(brands[brand], comp)
    return catalog

# Funciones de consulta sobre el catálogo


def req_1(catalog, marca):
    """
    Retorna el resultado del requerimiento 1
    """
    inicio = get_time()
    lista = catalog["brand"][marca]
    size = sl.size(lista)
    nodo = lista["first"]
    comp = n.get_info(nodo)
    
    max_precio = comp
    min_precio = comp
    max_ram = float(comp["ram_gb"])
    min_ram = float(comp["ram_gb"])
    max_vram = float(comp["vram_gb"])
    min_vram = float(comp["vram_gb"])
    max_nucleos = float(comp["cpu_cores"])
    min_nucleos = float(comp["cpu_cores"])
    max_year = int(comp["release_year"])
    min_year = int(comp["release_year"])
    
    total_precio = 0
    total_ram = 0
    total_vram = 0
    total_nucleos = 0
    total_year = 0
    
    for _ in range(size-1):
        
        if float(comp["price"]) < float(min_precio["price"]):
            min_precio = comp
        elif float(comp["price"]) == float(max_precio["price"]):
                max_precio = comp if float(comp["weight_kg"]) < float(max_precio["weight_kg"]) else max_precio
        if float(comp["price"]) > float(max_precio["price"]):
            max_precio = comp
        elif float(comp["price"]) == float(min_precio["price"]):
                min_precio = comp if float(comp["weight_kg"]) < float(min_precio["weight_kg"]) else min_precio
        if float(comp["ram_gb"]) < min_ram:
            min_ram = float(comp["ram_gb"])
        if float(comp["ram_gb"]) > max_ram:
            max_ram = float(comp["ram_gb"])
        if float(comp["vram_gb"]) < min_vram:
            min_vram = float(comp["vram_gb"])
        if float(comp["vram_gb"]) > max_vram:
            max_vram = float(comp["vram_gb"])
        if float(comp["cpu_cores"]) < min_nucleos:
            min_nucleos = float(comp["cpu_cores"])
        if float(comp["cpu_cores"]) > max_nucleos:
            max_nucleos = float(comp["cpu_cores"])
        if int(comp["release_year"]) < min_year:
            min_year = int(comp["release_year"])
        if int(comp["release_year"]) > max_year:
            max_year = int(comp["release_year"])
        
        total_precio += float(comp["price"])
        total_ram += float(comp["ram_gb"])
        total_vram += float(comp["vram_gb"])
        total_nucleos += int(comp["cpu_cores"])
        total_year += int(comp["release_year"])
        
        nodo = n.get_next(nodo)
        comp = n.get_info(nodo)
        
    if size > 0:
        promedio_precio = round(total_precio/size, 2)
        promedio_ram = round(total_ram/size, 2)
        promedio_vram = round(total_vram/size, 2)
        promedio_nucleos = round(total_nucleos/size, 2)
        promedio_year = round(total_year/size)
    else:
        promedio_precio = 0
        promedio_ram = 0
        promedio_vram = 0
        promedio_nucleos = 0
        promedio_year = 0
        max_precio = {"price": 0}
        min_precio = {"price": 0}
        max_ram = 0
        min_ram = 0
        max_vram = 0
        min_vram = 0
        max_nucleos = 0
        min_nucleos = 0
        max_year = 0
        min_year = 0
    
    lista_estadisticas = [
    ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
    ["Total computadores marca", size],
    ["Precio promedio", promedio_precio],
    ["Precio mínimo", float(min_precio["price"])],
    ["Precio máximo", float(max_precio["price"])],
    ["RAM promedio", promedio_ram],
    ["RAM mínima", min_ram],
    ["RAM máxima", max_ram],
    ["VRAM promedio", promedio_vram],
    ["VRAM mínima", min_vram],
    ["VRAM máxima", max_vram],
    ["CPU cores promedio", promedio_nucleos],
    ["CPU cores mínimo", min_nucleos],
    ["CPU cores máximo", max_nucleos],
    ["Año promedio", promedio_year],
    ["Año mínimo", min_year],
    ["Año máximo", max_year]
    ]

    lista_modelos = [
        ["Modelo mayor precio", max_precio["model"], float(max_precio["price"])],
        ["Modelo menor precio", min_precio["model"], float(min_precio["price"])]
    ]

    return lista_estadisticas, lista_modelos


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    inicio = get_time()
    lista = al.to_py_list(catalog["computer"])
    
    max_precio = {"price":float("-inf")}
    min_precio = {"price":float("inf")}
    max_year = {"release_year": "2018"}
    
    total_precio = 0
    total_ram = 0
    total_vram = 0
    size = 0
    
    for comp in lista:
        if float(comp["price"]) >= float(pmin) and float(comp["price"]) <= float(pmax):
            if float(comp["price"]) < float(min_precio["price"]):
                min_precio = comp
            if float(comp["price"]) > float(max_precio["price"]):
                max_precio = comp
            if int(comp["release_year"]) > int(max_year["release_year"]):
                max_year = comp
            total_precio += float(comp["price"])
            total_ram += float(comp["ram_gb"])
            total_vram += float(comp["vram_gb"])
            size += 1
    
    if size > 0:
        promedio_precio = round(total_precio/size, 2)
        promedio_ram = round(total_ram/size, 2)
        promedio_vram = round(total_vram/size, 2)
    else:
        promedio_precio = 0
        promedio_ram = 0
        promedio_vram = 0
    
    lista_estadisticas = [
        ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
        ["Total computadores en rango", size],
        ["Precio promedio", promedio_precio],
        ["RAM promedio", promedio_ram],
        ["VRAM promedio", promedio_vram]
    ]
    
    if size>0:
        menor_precio = [
            ["Modelo", min_precio["model"]],
            ["Marca", min_precio["brand"]],
            ["Año", min_precio["release_year"]],
            ["CPU", min_precio["cpu_brand"]],
            ["GPU", min_precio["gpu_brand"]],
            ["Precio", min_precio["price"]],
        ]
        
        mayor_precio = [
            ["Modelo", max_precio["model"]],
            ["Marca", max_precio["brand"]],
            ["Año", max_precio["release_year"]],
            ["CPU", max_precio["cpu_brand"]],
            ["GPU", max_precio["gpu_brand"]],
            ["Precio", max_precio["price"]],
        ]
        
        mas_moderno = [
            ["Modelo", max_year["model"]],
            ["Marca", max_year["brand"]],
            ["Año", max_year["release_year"]],
            ["CPU", max_year["cpu_brand"]],
            ["GPU", max_year["gpu_brand"]],
            ["Precio", max_year["price"]],
        ]
    else:
        menor_precio = [
            ["Modelo", "N/A"],
            ["Marca", "N/A"],
            ["Año", "N/A"],
            ["CPU", "N/A"],
            ["GPU", "N/A"],
            ["Precio", "N/A"],
        ]
        
        mayor_precio = [
            ["Modelo", "N/A"],
            ["Marca", "N/A"],
            ["Año", "N/A"],
            ["CPU", "N/A"],
            ["GPU", "N/A"],
            ["Precio", "N/A"],
        ]
        
        mas_moderno = [
            ["Modelo", "N/A"],
            ["Marca", "N/A"],
            ["Año", "N/A"],
            ["CPU", "N/A"],
            ["GPU", "N/A"],
            ["Precio", "N/A"],
        ]
    
    return lista_estadisticas, menor_precio, mayor_precio, mas_moderno
    pass


def req_3(catalog, cpu_brand, cpu_tier):
    """
    Retorna el resultado del requerimiento 3
    """
    inicio = get_time()
    lista = al.to_py_list(catalog["brandCPU"][cpu_brand])
    
    total_precio = 0
    total_ram = 0
    total_vram = 0
    total_threads = 0
    size = 0
    
    freciencia_gpu = {}
    freciencia_year = {}
    gpu_boolean = True
    year_boolean = True
    
    for comp in lista:
        if comp["cpu_tier"] == cpu_tier:
            total_precio += float(comp["price"])
            total_ram += float(comp["ram_gb"])
            total_vram += float(comp["vram_gb"])
            total_threads += int(comp["cpu_threads"])
            size += 1
            
            gpu = comp["gpu_brand"]
            if gpu not in freciencia_gpu:
                freciencia_gpu[gpu] = 0
                if gpu_boolean:
                    mas_frecuente_gpu = comp
                    gpu_boolean = False
            freciencia_gpu[gpu] += 1
            if freciencia_gpu[mas_frecuente_gpu["gpu_brand"]] < freciencia_gpu[gpu]:
                mas_frecuente_gpu = comp
            
            year = comp["release_year"]
            if year not in freciencia_year:
                freciencia_year[year] = 0
                if year_boolean:
                    mas_frecuente_year = comp
                    year_boolean = False
            freciencia_year[year] += 1
            if freciencia_year[mas_frecuente_year["release_year"]] < freciencia_year[year]:
                mas_frecuente_year = comp

    if size > 0:
        promedio_precio = round(total_precio/size, 2)
        promedio_ram = round(total_ram/size, 2)
        promedio_vram = round(total_vram/size, 2)
        promedio_threads = round(total_threads/size, 2)

    else:
        promedio_precio = 0
        promedio_ram = 0
        promedio_vram = 0
        promedio_threads = 0
        mas_frecuente_gpu = {"gpu_brand": "N/A"}
        mas_frecuente_year = {"release_year": "N/A"}

    lista_estadisticas = [
        ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
        ["Total computadores", size],
        ["Precio promedio", promedio_precio],
        ["RAM promedio", promedio_ram],
        ["VRAM promedio", promedio_vram],
        ["Threads promedio", promedio_threads],
        ["GPU más frecuente", mas_frecuente_gpu["gpu_brand"]],
        ["Año más frecuente", mas_frecuente_year["release_year"]]
    ]
    

    return lista_estadisticas


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    inicio = get_time()
    year = catalog["year"]
    min_year = min_year if min_year >=2018 else 2018
    max_year = max_year if max_year <=2025 else 2025
    
    mayor_precio = {"price":float("-inf")}
    min_precio = {"price":float("inf")}
    
    total_precio = 0
    total_tier = 0
    total_pantalla = 0
    size = 0
    
    for y in range(int(min_year), int(max_year)+1):
        lista = year[str(y)]
        nodo = lista["first"]
        for _ in range(sl.size(lista)):
            comp = n.get_info(nodo)
            if comp["resolution"] == resolucion:
                if (float(comp["price"]) < float(min_precio["price"])) or (float(comp["price"]) == float(min_precio["price"]) and float(comp["weight_kg"]) < float(min_precio["weight_kg"])):
                    min_precio = comp
                if (float(comp["price"]) > float(mayor_precio["price"])) or (float(comp["price"]) == float(mayor_precio["price"]) and float(comp["weight_kg"]) < float(mayor_precio["weight_kg"]))  :
                    mayor_precio = comp
                
                total_precio += float(comp["price"])
                total_tier += int(comp["gpu_tier"])
                total_pantalla += float(comp["display_size_in"])
                size += 1
                
            nodo = n.get_next(nodo)
        
    if size > 0:
        promedio_precio = round(total_precio/size, 2)
        promedio_tier = round(total_tier/size)
        promedio_pantalla = round(total_pantalla/size, 2)
    else:
        promedio_precio = 0
        promedio_tier = 0
        promedio_pantalla = 0
        mayor_precio = {"weight_kg": "N/A", "gpu_tier": "N/A", "release_year": "N/A", "resolution": "N/A", "price": "N/A", "display_type": "N/A"}
        min_precio = {"weight_kg": "N/A", "gpu_tier": "N/A", "release_year": "N/A", "resolution": "N/A", "price": "N/A", "display_type": "N/A"}

    lista_estadisticas = [
        ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
        ["Filtro Seleccion", "CARO" if boolean else "BARATO"],
        ["Total computadores", size],
        ["Precio promedio", promedio_precio],
        ["Tamaño Pantalla promedio (in)", promedio_pantalla],
        ["Tier promedio", promedio_tier]
    ]
    
    precio = [
        ["Precio", mayor_precio["price"] if boolean else min_precio["price"]],
        ["Tamaño Pantalla", mayor_precio["display_size_in"] if boolean else min_precio["display_size_in"]],
        ["GPU Tier", mayor_precio["gpu_tier"] if boolean else min_precio["gpu_tier"]],
        ["Display", mayor_precio["display_type"] if boolean else min_precio["display_type"]],
        ["Año", mayor_precio["release_year"] if boolean else min_precio["release_year"]],
        ["Peso", mayor_precio["weight_kg"] if boolean else min_precio["weight_kg"]],
    ]
    
    return lista_estadisticas, precio
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
