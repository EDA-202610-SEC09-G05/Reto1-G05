import time
import csv
from tabulate import tabulate
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.List import list_node as n
from DataStructures.Set import set as s

def new_logic(): 
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #estructura principal es catalog, diccionario que contiene todos los datos 
    catalog = {
        "computer": al.new_list(), 
        #lista de diccionarios de los computadores
        """
        cada fila del csv se convierte ne un diccionario 
        se reccore cada fila con for, creando un dict, y se añade al final de 
        lista 
        todos los comp del csv, cada comp es un diccionario con sus atributos
        ejemplo:
        {
        "brand": "asus",
        "model": "rog strix",
        "price": "1200",
        "ram_gb": "16",
        "cpu_brand": "intel",
        "gpu_brand": "nvidia",
        "release_year": "2022"
        }

    es Array List - elementos en posiciones, para acceso rápido
    lista implementada sobre un arreglo, donde los elementos se almacenan en
    posiciones consecutivas de memoria. Esto permite acceder a cualquier 
    elemento por índice en tiempo constante y recorrer la lista eficientemente.
        """
        
        "brandCPU": {}, 
        #diccionario que sirve como índice por marca de CPU, 
        # llave - marca Cpu , valo- lista de comp q usan esa CPU
        """
        cada vez q se lee un comp se saca la marca, si la marca no existe  se 
        crea una lista nueva, si ya existe, se susa la que ya esta, y se agrega el 
        comp a esa lista
        agrupa computadores por marca de CPU 
        catalog["brandCPU"] = {
            "intel": [comp1, comp2, comp3],
            "amd": [comp4, comp5]
            }
        """
        
        "year": {},
        #dict que agrupa comp por año de lanzamiento
        #llave - año lanz , valor - lista de comp de ese año
    """
    se carga igual que brand cpu 
    
        catalog["year"] = {
        "2020": [comp1, comp2],
        "2021": [comp3],
        "2022": [comp4, comp5]
        }
    """
        
        "brand": {},
        #dict que agrupa comp por marca 
        #llave - brand , valor - lista de comp de esa marca 
    """
    se carga igual que brand cpu 
        catalog["brand"] = {
        "asus": [comp1, comp4],
        "hp": [comp2],
        "lenovo": [comp3, comp5],
        "dell": [comp6]
        }
    """
        "brandGPU": s.new_set(),
        #set-conjunto, guarda valores únicos, no duplicados, no importa el orden 
        """es set pq solo se necesita saber que marcas de gpu existem en el
        data set, no que comp las tienen
        se guradan solo las marcas únicas, los sets no duplican elementos 
        """
        
        "resolution": s.new_set() #igual que brand GPU, guarda resoluciones sin repetirse
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, size):
    """
    FUnción principal que carga todo el dataset
    Parámetros
    catalog - estructura principal donde se guardan todos los datos
    size - tamaño del dataset (para escoger el CSV)
    """
    inicio = get_time() #mide tiempo de ejecución
    url = f"./Data/computer_prices_{size}.csv" #ruta de archivo
    max_precio = {"price":float("-inf")}#se inicializan el comp más barato y másn caro
    min_precio = {"price":float("inf")}
    
    with open(url, encoding="utf-8") as f: #abre el csv
        filas = list(csv.DictReader(f))#lista de comp
    
    for comp in filas: #comp es dic con datos del comp, se recorren todos los comp
        al.add_last(catalog["computer"], comp)# se guarda en la lista principal 
        load_brands(catalog, comp)
        load_years(catalog, comp)
        load_brands_cpu(catalog, comp)
        load_brands_gpu(catalog, comp)
        load_resolutions(catalog, comp)
        
        #se calcula el precion min y max
        if float(comp["price"]) < float(min_precio["price"]):
            min_precio = comp
        if float(comp["price"]) > float(max_precio["price"]):
            max_precio = comp
        
    dtime = delta_time(inicio, get_time())#tiempo de carga de datos
    return catalog, dtime, min_precio, max_precio

def load_brands(catalog, comp):
    """
    Organiza los comp por marca
    """
    brands = catalog["brand"] #obtiene la marca del comp
    brand = comp["brand"].lower() #en lower para evitar duplicados
    
    if brand not in brands:#si la marca no existe crea una lista y se agrega el comp
        brands[brand] = sl.new_list()
    sl.add_last(brands[brand], comp)
    return catalog

def load_years(catalog, comp):
    """
    Agrupa computadores por año de lanzamiento
    saca el diccionario de años, el año del comp, si alo no existe, crea una lista, 
    y se agrega el comp
    """
    years = catalog["year"]
    year = comp["release_year"]
    
    if year not in years:
        years[year] = sl.new_list()
    sl.add_last(years[year], comp)
    return catalog

def load_brands_cpu(catalog, comp):
    """
    Agrupa los comp por marca de CPU
    obtiene el dict, marca del cpu, si no existe crea una lista, y se agrega el comp
    """
    brands = catalog["brandCPU"]
    brand = comp["cpu_brand"].lower()
    
    if brand not in brands:
        brands[brand] = al.new_list()
    al.add_last(brands[brand], comp)
    return catalog

def load_brands_gpu(catalog, comp):
    """
    Guarda las marcas de GPU únicas 
    obtiene el set, obtiene la marca de GPU, se agrega al set, como es set no se repite
    """
    brands = catalog["brandGPU"]
    brand = comp["gpu_brand"].lower()
    
    s.add_element(brands, brand)
    return catalog

def load_resolutions(catalog, comp):
    """
    Guarda las resoluciones únicas de pantalla
    obtiene el set, la resolución, se agrega al set
    """
    resolutions = catalog["resolution"]
    resolution = comp["resolution"]
    
    s.add_element(resolutions, resolution)
    return catalog

# Funciones de consulta sobre el catálogo


def req_1(catalog, marca):
    """
    Promedio de características para una marca específica  
    catalog → el catálogo con todos los computadores
    marca → la marca que el usuario quiere analiza
    """
    inicio = get_time() #Se guarda el tiempo actual para luego calcular cuánto tardó el requerimiento.
    lista = catalog["brand"][marca] #Se obtiene la lista de computadores de esa marca
    size = sl.size(lista)# se obtiene el tamaño de la lista
    nodo = lista["first"] # se obtiene el primer nodo de la lista
    comp = n.get_info(nodo) #es SINGLE LINKED LIST, ent se accede al primer nodo 
    #comp es el priemr comp de la lista, de usan los datos del primer comp como referencia inidial
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
    #variables para cálcular promedios 
    total_precio = 0
    total_ram = 0
    total_vram = 0
    total_nucleos = 0
    total_year = 0
    
    for _ in range(size-1): #se recorren todos los comp de la marca 
        #calc precio max y min
        if float(comp["price"]) < float(min_precio["price"]):
            min_precio = comp
        elif float(comp["price"]) == float(max_precio["price"]):
                max_precio = comp if float(comp["weight_kg"]) < float(max_precio["weight_kg"]) else max_precio
        if float(comp["price"]) > float(max_precio["price"]):
            max_precio = comp
        elif float(comp["price"]) == float(min_precio["price"]):
                min_precio = comp if float(comp["weight_kg"]) < float(min_precio["weight_kg"]) else min_precio
               
                #valor_si_true if condicion else valor_si_false
        #calc de min y max en las demas caract
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
        
        #suma para promedios
        total_precio += float(comp["price"])
        total_ram += float(comp["ram_gb"])
        total_vram += float(comp["vram_gb"])
        total_nucleos += int(comp["cpu_cores"])
        total_year += int(comp["release_year"])
        
        #avance al siguiente nodo, mueve el recorrido al siguiente comp
        nodo = n.get_next(nodo)
        comp = n.get_info(nodo)
        
    #calc promedios
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
    
    #se guardan los resultados
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
    
# se guarda el modelo mas caro y el mas barato
    lista_modelos = [
        ["Modelo mayor precio", max_precio["model"], float(max_precio["price"])],
        ["Modelo menor precio", min_precio["model"], float(min_precio["price"])]
    ]

    return lista_estadisticas, lista_modelos


def req_2(catalog, pmin, pmax):
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


def req_4(catalog, cpu_brand, gpu_brand):
    """
    Obtener el precio promedio para una combinación CPU brand GPU Model    
    catalog - el catálogo con todos los computadores
    cpu_brand - marca del procesador 
    gpu_brand - modelo de GPU
    """
    inicio = get_time()#Se guarda el tiempo inicial para luego calcular cuánto tardó el requerimiento
    lista = al.to_py_list(catalog["brandCPU"][cpu_brand])#se obtienen los comp con esa CPU
    
    #variables para los comp más caros, -inf pra que cualquier precio sea mayor 
    mayor_precio1 = {"price":float("-inf")}
    mayor_precio2 = {"price":float("-inf")}
    
    #variables para estadisticas
    size = 0 
    total_precio = 0
    total_ram = 0
    total_vram = 0
    total_boost = 0
    
    for comp in lista: # se revisa cada comp con esa CPU
        if comp["gpu_brand"].lower() == gpu_brand: #filtro por GPU (Creq PU Brand – GPU Model)
            size += 1
            total_precio += float(comp["price"])
            total_ram += float(comp["ram_gb"])
            total_vram += float(comp["vram_gb"])
            total_boost += float(comp["cpu_boost_ghz"])
            
            #encontrar el comp más caro
            #or. si hay empate por precio se toma el de menor peso
            if float(comp["price"]) > float(mayor_precio1["price"]) or (float(comp["price"]) == float(mayor_precio1["price"]) and float(comp["weight_kg"]) < float(mayor_precio1["weight_kg"])):
                #cuando se encuentra el nuevo primero, el antiguo primero pasa a ser el segundo
                mayor_precio2 = mayor_precio1
                mayor_precio1 = comp
            #encontrar el segundo más caro
            if (float(comp["price"]) > float(mayor_precio2["price"]) and comp != mayor_precio1) or (float(comp["price"]) == float(mayor_precio2["price"]) and float(comp["weight_kg"]) < float(mayor_precio2["weight_kg"])):
                mayor_precio2 = comp
   
    #calc promedios
    if size > 0:
        promedio_precio = round(total_precio/size, 2)
        promedio_ram = round(total_ram/size, 2)
        promedio_vram = round(total_vram/size, 2)
        promedio_boost = round(total_boost/size, 2)
    # si ninguno cumple le fintro, 0 prom y N/A comp
    else:
        promedio_precio = 0
        promedio_ram = 0
        promedio_vram = 0
        promedio_boost = 0
        mayor_precio1 = {"model": "N/A", "brand": "N/A", "release_year": "N/A", "cpu_model": "N/A", "price": "N/A"}
        mayor_precio2 = {"model": "N/A", "brand": "N/A", "release_year": "N/A", "cpu_model": "N/A", "price": "N/A"}

    #guarda los resultados
    lista_estadisticas = [
        ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
        ["Total computadores", size],
        ["Precio promedio", promedio_precio],
        ["RAM promedio", promedio_ram],
        ["VRAM promedio", promedio_vram],
        ["Boost Clock promedio", promedio_boost]
    ]
    
    #info del comp mas caro
    top1 = [
        ["Modelo", mayor_precio1["model"]],
        ["Marca", mayor_precio1["brand"]],
        ["Año", mayor_precio1["release_year"]],
        ["Modelo CPU", mayor_precio1["cpu_model"]],
        ["Precio", mayor_precio1["price"]]
    ]
    
    #info del segundo comp más caro
    top2 = [
        ["Modelo", mayor_precio2["model"]],
        ["Marca", mayor_precio2["brand"]],
        ["Año", mayor_precio2["release_year"]],
        ["Modelo CPU", mayor_precio2["cpu_model"]],
        ["Precio", mayor_precio2["price"]]
    ]

    return lista_estadisticas, top1, top2

def req_5(catalog, boolean, resolucion, min_year, max_year):
    """
    Identificar el computador más barato/caro que tenga una resolución dada en un rango de años   
    filtrar comp por resolución, rango de años, luego contar cuantos cumplen, calc promedios, 
    encontrar el más caro o el más barato, dependiento de: true - caro, false - barato
    """
    inicio = get_time()
    year = catalog["year"]
    #ajuste del rango de años, para que el rango este en el dataset
    #si se pide 2015-2030, se ajusta a 2018 - 2025
    min_year = min_year if min_year >=2018 else 2018
    max_year = max_year if max_year <=2025 else 2025
    
    #variables para encontrar el mas caro y el mas barato
    mayor_precio = {"price":float("-inf")} #-inf cualquier precio será mayor
    min_precio = {"price":float("inf")} #-inf cualquier precio sera menor
    
    total_precio = 0
    total_tier = 0
    total_pantalla = 0
    size = 0
    
    #recorer los años
    for y in range(int(min_year), int(max_year)+1):
        lista = year[str(y)] #sacar la lista de comp de ese año
        nodo = lista["first"] #recorer la sl (lista enlazada)
        for _ in range(sl.size(lista)): #recorer todos los nodos
            comp = n.get_info(nodo) #obtener el comp, devuelve el dict el comp
            if comp["resolution"] == resolucion: #filtro de resolucioon
                if (float(comp["price"]) < float(min_precio["price"])) or (float(comp["price"]) == float(min_precio["price"]) and float(comp["weight_kg"]) < float(min_precio["weight_kg"])):
                    min_precio = comp #encontrar el más barato, revisar si hay empate, se da el de menor peso
                if (float(comp["price"]) > float(mayor_precio["price"])) or (float(comp["price"]) == float(mayor_precio["price"]) and float(comp["weight_kg"]) < float(mayor_precio["weight_kg"]))  :
                    mayor_precio = comp #encontrar el más caro
                
                #acimilar promedios
                total_precio += float(comp["price"])
                total_tier += int(comp["gpu_tier"])
                total_pantalla += float(comp["display_size_in"])
                size += 1
           #pasa al siguiente nodo     
            nodo = n.get_next(nodo)
   
    #calc promedios    
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
        ["Filtro Seleccion", "CARO" if boolean else "BARATO"], #mostrar si el filtro fue caro o barato
        ["Total computadores", size],
        ["Precio promedio", promedio_precio],
        ["Tamaño Pantalla promedio (in)", promedio_pantalla],
        ["Tier promedio", promedio_tier]
    ]
    
    precio = [
        ["Precio", mayor_precio["price"] if boolean else min_precio["price"]], #si boolean =true, Caro, si boolean=falase, barato
        ["Tamaño Pantalla", mayor_precio["display_size_in"] if boolean else min_precio["display_size_in"]],
        ["GPU Tier", mayor_precio["gpu_tier"] if boolean else min_precio["gpu_tier"]],
        ["Display", mayor_precio["display_type"] if boolean else min_precio["display_type"]],
        ["Año", mayor_precio["release_year"] if boolean else min_precio["release_year"]],
        ["Peso", mayor_precio["weight_kg"] if boolean else min_precio["weight_kg"]],
    ]
    
    return lista_estadisticas, precio

def req_6(catalog, min_year, max_year):
    """
    Identificar el sistema operativo más usado y el de mayor recaudación en un rango de tiempo    
    filtrar comp por año inicial, año final, luego calcular OS mas usado (el que tiene más computadores), OS que 
    mas reacauda(el que suma más precios), y para cada OS mostrar el precio prom, peso prom, comp más caro y el más barato
    """
    # dict OS : [total_count , total_precio, total_peso, comp_barato, comp_caro]
    inicio = get_time()
    #ajustar el rango de años, revisar que el rango este en dataset
    min_year = min_year if min_year >=2018 else 2018
    max_year = max_year if max_year <=2025 else 2025
    year = catalog["year"]
    sys_op = {} #dict para agrupar por OS, guarda la info por sistema operativo
   
    #variables para encontrar los mejores OS
    mejor_os_precio = float("-inf")
    mejor_os_uso = float("-inf")
    mejor_os_precio_nombre = ""
    mejor_os_uso_nombre = ""
    size = 0
    
    #recorer los años
    for y in range(int(min_year), int(max_year)+1):
        lista = year[str(y)] #obtener lista de comp de ese año
        nodo = lista["first"] #recorrer lista enlazasa
        for _ in range(sl.size(lista)):
            comp = n.get_info(nodo) #obtener el comp, devuleve el dict del comp
            size += 1
            
            if comp["os"] not in sys_op: #si el os no esta en el dict se crea
                sys_op[comp["os"]] = sl.to_sl_list([0, 0, 0, {"price": float("inf")}, {"price": float("-inf")}])
            """
            sys_op[comp["os]] es un comp del dataset
                [0] total computadores - 0 pq aun no hay comp
                [1] suma precios - 0 pq aun no se ha sumado nada
                [2] suma pesos
                [3] computador más barato - {"price": inf} se uan infinito para que el primer comp siempre sea menor
                [4] computador más caro - {"price": -inf} porq cualqueir precio sea mayor
            convierte la lista normal en single, 
            [0] -> [0] -> [0] -> [{price: inf}] -> [{price:-inf}]
            """
            os_info = sys_op[comp["os"]] #obtener los datos del os, lista con los datos
            sl.add_number(os_info, 0, 1) #se van actualizando los ocntadores
            sl.add_number(os_info, 1, float(comp["price"])) #sumar precios
            sl.add_number(os_info, 2, float(comp["weight_kg"])) #sumar pesos
            if float(comp["price"]) < float(sl.get_element(os_info, 3)["price"]): #encontrar el comp más barato
                sl.change_info(os_info, 3, comp)
            if float(comp["price"]) > float(sl.get_element(os_info, 4)["price"]):#encontrar el comp más caro
                sl.change_info(os_info, 4, comp)
            nodo = n.get_next(nodo)
    
    #calc promedios precio_total/ cant
    for os, os_info in sys_op.items():
        sl.add_last(os_info, sl.get_element(os_info, 1)/sl.get_element(os_info, 0))
        sl.add_last(os_info, sl.get_element(os_info, 2)/sl.get_element(os_info, 0))
       
        #encontrar el OS q más recauda
        if sl.get_element(os_info, 1) > mejor_os_precio:
            mejor_os_precio = sl.get_element(os_info, 1)
            mejor_os_precio_nombre = os
        #encontrar os más usado
        if sl.get_element(os_info, 0) > mejor_os_uso:
            mejor_os_uso = sl.get_element(os_info, 0)
            mejor_os_uso_nombre = os
            
    #estadisticas generales
    lista_estadisticas = [
        ["Tiempo de ejecución (ms)", delta_time(inicio, get_time())],
        ["Total computadores", size]
    ]
    #info de los mejores os 
    mejor_os = [
        ["OS mas usado", mejor_os_uso_nombre, mejor_os_uso, sl.get_element(sys_op[mejor_os_uso_nombre], 1)],
        ["Os mas recaudo", mejor_os_precio_nombre, sl.get_element(sys_op[mejor_os_precio_nombre], 0), mejor_os_precio]
    ]
    #estadisticas de cada os
    os_estadisticas = [
        [
            os, #primer elemento
            sl.get_element(os_info, 5), #segundo elemento-sacar el elemento den la pos 5 de lista, PROM PRECIO
            sl.get_element(os_info, 6), #tercer elemento - peso promedio
            #cuarto elemento - se hace tabla}
            #comp más caro
            tabulate([
                ["Modelo", sl.get_element(os_info, 4)["model"]], 
                ["Marca", sl.get_element(os_info, 4)["brand"]],
                ["Año", sl.get_element(os_info, 4)["release_year"]],
                ["CPU", sl.get_element(os_info, 4)["cpu_brand"]],
                ["GPU", sl.get_element(os_info, 4)["gpu_brand"]],
                ["Precio", sl.get_element(os_info, 4)["price"]]
            ], tablefmt="fancy_grid"),
            #quinto elemento - comp más barato
            tabulate([
                ["Modelo", sl.get_element(os_info, 3)["model"]],
                ["Marca", sl.get_element(os_info, 3)["brand"]],
                ["Año", sl.get_element(os_info, 3)["release_year"]],
                ["CPU", sl.get_element(os_info, 3)["cpu_brand"]],
                ["GPU", sl.get_element(os_info, 3)["gpu_brand"]],
                ["Precio", sl.get_element(os_info, 3)["price"]]
            ], tablefmt="fancy_grid")
        ] for os, os_info in sys_op.items() 
        
        #recorrer cada OS, crea lista os_estadistica, cada elemento es otra lista 
        
    ]
    return lista_estadisticas, mejor_os, os_estadisticas
    """
    cada elemnto final
       [
        "Windows",
        1500,      # precio promedio
        2.3,       # peso promedio
        tabla_computador_mas_caro,
        tabla_computador_mas_barato
        ]
        
    lista completa ej
    os_estadisticas = [
     ["Windows",1500,2.3, tabla1, tabla2],
     ["MacOS",2200,1.8, tabla3, tabla4],
     ["Linux",1300,2.0, tabla5, tabla6]
    ]
    
    se usa list comprehension (forma corta de crear listas) [expresion for elemento in coleccion]
    normal es 
    os_estadisticas = []

for os, os_info in sys_op.items():

    fila = [
        os,
        sl.get_element(os_info,5),
        sl.get_element(os_info,6),
        tabla1,
        tabla2
    ]

    os_estadisticas.append(fila)
    
        """
        
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
    return round(elapsed,2)
