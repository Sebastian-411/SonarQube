import math

def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado."""
    return lado * lado

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado la base y la altura."""
    return base * altura

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado el radio."""
    return math.pi * (radio ** 2)

if __name__ == "__main__":
    print("Área del cuadrado con lado 4:", calcular_area_cuadrado(4))
    print("Área del rectángulo con base 5 y altura 3:", calcular_area_rectangulo(5, 3))
    print("Área del círculo con radio 2:", calcular_area_circulo(2))
