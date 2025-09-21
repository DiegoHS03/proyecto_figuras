def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def circulo(radio):
    area = 3.1416 * radio * radio
    perimetro = 2 * 3.1416 * radio
    return area, perimetro

def triangulo(base, altura):
    area = (base * altura) / 2
    return area, None