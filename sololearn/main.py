"""
Títulos de libros

Se le ha pedido que cree un programa especial de categorización de libros, que asigna a cada libro un código especial basado en su título.
El código es igual a la primera letra del libro, seguido del número de caracteres del título.
Por ejemplo, para el libro "Harry Potter", el código sería: H12, ya que contiene 12 caracteres (incluido el espacio).

Se le proporciona un archivo books.txt, que incluye los títulos de los libros, cada uno escrito en una línea separada.
Lea el título uno por uno y genere el código para cada libro en una línea separada.

Por ejemplo, si el archivo books.txt contiene:
Some book
Another book

Su programa debe producir:
S9
A12
"""

file = open("dbLibros.txt", "r")

indexLetra = slice(0, 1)

for i in file:
    content = i.rstrip()
    numL = len(content)
    inicial = i[indexLetra]
    print(inicial + str(numL))

file.close()