"""
Your module description
"""

def funcion(arreglo):
    men=arreglo[0]
    for x in range(1,len(arreglo)):
        if arreglo[x]<men:
            men=arreglo[x]
    return men
            
            