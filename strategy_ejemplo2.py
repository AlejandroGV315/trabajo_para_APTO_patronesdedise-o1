# Ejemplo 2 de Strategy --> Orrdenar libros por distintos criterios

class EstrategiaOrdenacion:
    def ordenar(self, libros):
        pass

class OrdenarPorTitulo(EstrategiaOrdenacion):
    def ordenar(self, libros):
        def obtener_titulo(libro):
            return libro["titulo"]

        return sorted(libros, key=obtener_titulo)

class OrdenarPorAutor(EstrategiaOrdenacion):
    def ordenar(self, libros):
        def obtener_autor(libro):
            return libro["autor"]

        return sorted(libros, key=obtener_autor)

class OrdenarPorAnio(EstrategiaOrdenacion):
    def ordenar(self, libros):
        def obtener_anio(libro):
            return libro["anio"]

        return sorted(libros, key=obtener_anio)


class Catalogo:
    def __init__(self, libros, estrategia_ordenacion):
        self.libros = libros
        self.estrategia_ordenacion = estrategia_ordenacion

    def mostrar_libros_ordenados(self):
        libros_ordenados = self.estrategia_ordenacion.ordenar(self.libros)

        for libro in libros_ordenados:
            texto = libro["titulo"] + " - " + libro["autor"] + " - " + str(libro["anio"])
            print(texto)


if __name__ == "__main__":
    libros = [
        {"titulo": "1984", "autor": "George Orwell", "anio": 1949},
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "anio": 1605},
        {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafon", "anio": 2001}
    ]

    print("Ordenado por titulo:")
    catalogo1 = Catalogo(libros, OrdenarPorTitulo())
    catalogo1.mostrar_libros_ordenados()

    print("")

    print("Ordenado por autor:")
    catalogo2 = Catalogo(libros, OrdenarPorAutor())
    catalogo2.mostrar_libros_ordenados()

    print("")

    print("Ordenado por anio:")
    catalogo3 = Catalogo(libros, OrdenarPorAnio())
    catalogo3.mostrar_libros_ordenados()
