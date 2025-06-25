# Read the entire line, split by spaces, and convert each part to float
# Lendo a linha inteira, dividindo por espaços e convertendo cada parte para float
values = list(map(float, input().split()))

A = values[0]
B = values[1]
C = values[2]

pi = 3.14159

# Your existing functions (they are correct)
def area_triangulo_retangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return pi * (raio ** 2)

def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

def area_quadrado(lado):
    return lado ** 2

def area_retangulo(lado1, lado2):
    return lado1 * lado2

# Calculate and print areas (also correct)
area_tri = area_triangulo_retangulo(A, C)
area_circ = area_circulo(C)
area_trap = area_trapezio(A, B, C)
area_quad = area_quadrado(B)
area_ret = area_retangulo(A, B)

print(f"TRIANGULO: {area_tri:.3f}")
print(f"CIRCULO: {area_circ:.3f}")
print(f"TRAPEZIO: {area_trap:.3f}")
print(f"QUADRADO: {area_quad:.3f}")
print(f"RETANGULO: {area_ret:.3f}")
