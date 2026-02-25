

def new_single_node(element):
    """
    Crea un nodo simple (list_node) con el elemento dado.

    El nodo creado tiene la estructura:
    {
        "info": element,
        "next": None
    }

    Parameters
    ----------
    element : any
        Elemento que se almacenará en el nodo.

    Returns
    -------
    dict
        Nodo recién creado con las llaves "info" y "next".

    Examples
    --------
    >>> nodo = new_single_node({"nombre": "Juan", "edad": 20})
    >>> nodo
    {'info': {'nombre': 'Juan', 'edad': 20}, 'next': None}
    """
    return {"info": element, "next": None}


def get_info(node):
    """
    Retorna la información almacenada en un nodo.

    Parameters
    ----------
    node : dict
        Nodo del cual se desea obtener la información.

    Returns
    -------
    any
        Valor almacenado en la llave "info" del nodo.

    Examples
    --------
    >>> nodo = new_single_node(10)
    >>> get_info(nodo)
    10
    """
    return node["info"]


def get_next(node):
    """
    Retorna la referencia al siguiente nodo.

    Parameters
    ----------
    node : dict
        Nodo del cual se desea obtener la referencia al siguiente nodo.

    Returns
    -------
    dict | None
        Nodo siguiente si existe, o None si no hay siguiente nodo.

    Examples
    --------
    >>> nodo1 = new_single_node(1)
    >>> nodo2 = new_single_node(2)
    >>> nodo1["next"] = nodo2
    >>> get_next(nodo1)
    {'info': 2, 'next': None}
    """
    return node["next"]