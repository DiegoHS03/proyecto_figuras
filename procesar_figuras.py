import pandas as pd
from figuras import rectangulo, circulo, triangulo

df = pd.read_csv("figuras.csv")
print("leemos el archivo")

for index, row in df.iterrows():
    figura = row['FIGURA']
    m1 = row['MEDIDA1']
    m2 = row['MEDIDA2']
    if figura == 'r':
        area, perimetro = rectangulo(m1, m2)
    elif figura == 'c':
        area, perimetro = circulo(m1)
    elif figura == 't':
        area, perimetro = triangulo(m1, m2)
    print(f"Fila {index}: FIGURA={figura}, AREA={area}, PERIMETRO={perimetro}")