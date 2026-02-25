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


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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
    # TODO: Modificar el requerimiento 5
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
