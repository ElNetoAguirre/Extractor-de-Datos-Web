"""
Programa Extractor de Datos Web (Web Scraping)
"""

import bs4
import requests

# Crear una URL sin número de página
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# Lista de Títulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar Páginas
for pagina in range(1, 51):
    # Crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina, timeout=10)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # Iterar en los libros
    for libro in libros:
        # Revisar que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            # Guardar título en variable
            titulo_libro = libro.select("a")[1]["title"]

            # Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver los libros de 4 o 5 estrellas en consola e imprimirlos en un archivo .txt
for t in titulos_rating_alto:
    print(t)

with open('lista_libros.txt', 'a', encoding="utf-8") as archivo:
    archivo.writelines('\n'.join(titulos_rating_alto))
