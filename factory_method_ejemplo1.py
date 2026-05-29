# Ejemplo 1 de Factory Method (creación de distintos tipos de usuarios en una biblioteca)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_permisos(self):
        pass

class Alumno(Usuario):
    def mostrar_permisos(self):
        return self.nombre + " puede pedir libros prestados durante 15 días."

class Profesor(Usuario):
    def mostrar_permisos(self):
        return self.nombre + " puede pedir libros prestados durante 30 días."

class Bibliotecario(Usuario):
    def mostrar_permisos(self):
        return self.nombre + " puede gestionar el catálogo de libros."

class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, nombre):
        if tipo == "alumno":
            return Alumno(nombre)
        elif tipo == "profesor":
            return Profesor(nombre)
        elif tipo == "bibliotecario":
            return Bibliotecario(nombre)
        else:
            raise ValueError("Tipo de usuario no válido")

if __name__ == "__main__":
    usuario1 = UsuarioFactory.crear_usuario("alumno", "Jaime")
    usuario2 = UsuarioFactory.crear_usuario("profesor", "Raul")
    usuario3 = UsuarioFactory.crear_usuario("bibliotecaria", "Laura")

    print(usuario1.mostrar_permisos())
    print(usuario2.mostrar_permisos())
    print(usuario3.mostrar_permisos())
