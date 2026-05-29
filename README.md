# TRABAJO PARA EL APTO, PATRONES DE DISEÑO

# INTRO (qué son y como se usan)

Voy a explicar e implementar varios ejemplos de patrones de diseño en Python.

- Los patrones de diseño son soluciones habituales a problemas comunes que aparecen durante el diseño de software. No son programas completos que se copian directamente sino formas de organizar el código para que sea más claro, flexible....
Refactoring Guru explica que cada patrón funciona como un plano que se puede adaptar para resolver un problema concreto dentro del código.

Se suelen usar en situaciones como estas:

- Cuando hay que crear objetos de distintos tipos.
- Cuando se quiere evitar repetir código.
- Cuando el programa puede crecer en el futuro.
- Cuando se quiere reducir el acoplamiento entre clases.
- Cuando existen varias formas de realizar una misma tarea.
- Cuando se quiere que el código sea más fácil de probar y mantener.

Por ejemplo, por hablar del pryecyo que hicimos de esta asigntura en grupo, si una biblioteca tiene distintos tipos de usuarios, como alumno, profesor o bibliotecario, puede ser útil usar Factory Method para crear cada tipo de usuario sin llenar el código principal de condiciones.

- Són útiles porque ayudan a no repetir siempre las mismas soluciones desde 0. Si un problema ya ha aparecido muchas veces, un patrón ofrece una forma ya  de resolverlo. Además, también sirven como lenguaje común entre programadores porque permiten explicar una solución de forma rápida. 
Por ejemplo en una app puede aparecer muchas veces el problema de crear objetos de distintos tipos. En lugar de llenar el programa de condiciones y crear los objetos directamente en muchas partes del código, se puede usar un patrón como Factory Method.

En este trabajo explicaré dos patrones:

- Factory Method --> Como patrón creacional.
- Strategy --> Como patrón de comportamiento.

Además ondré ejemplos en cada uno.

# Por qué son útiles

Los patrones de diseño son útiles porque mejoran la calidad interna del software pese a que añ principio pueden parecer más largos que una solución directa, suelen facilitar mucho el mantenimiento cuando el proyecto crece.

Sus principales ventajas son:

- Hacen que el código esté mejor organizado.
- Evitan repetir soluciones improvisadas.
- Facilitan añadir nuevas funcionalidades.
- Mejoran la comunicación entre programadores.

# Diseño, arquitectura y microarquitectura

Los patrones de diseño forman parte principalmente del diseño del software. Para entenderlo bien hay que iferenciar entre arquitectura, diseño y microarquitectura.

* Arrquitectura del software: Decisiones más generales del sistema como podría ser decidir si una aplicación va a funcionar como una aplicación web, si va a tener una API, si usará una BD etc....

* El diseño del software se centra más en cómo se organizan las clases, módulos y las responsabilidades dentro del programa. No es tanto de la estructura general del sistema, sino de cómo se reparte el trabajo entre las distintas partes del código.

* La microarquitectura hace referencia a decisiones todavía más concretas dentro del diseño como decidir que para crear objetos se va a usar Factory Method, o que para cambiar entre distintos algoritmos se va a usar Strategy.

Por tanto, los patrones de diseño no suelen definir la arquitectura completa de una aplicación pero yudan a organizar mejor las clases y a reducir problemas como la repetición de código, el acoplamiento o la dificultad para ampliar el sistema.

Por tnto, los patrones de diseño pertenecen sobre todo al diseño y a la microarquitectura del software.

## 1er PATRÓN --> Patrón creacional: Factory Method

Es un patrón creacional, es decir, relacionado con la creación de objetos.

Factory Method permite crear objetos sin tener que escribir directamente en el código principal la clase concreta que se va a utilizar. En lugar de hacer muchas condiciones con if, hay una función o clase que lo hace. Este patrón es útil cuando un programa necesita trabajar con varios tipos de objetos parecidos, pero no quiere depender directamente de sus clases concretas. Volviendo al ejemplo de la biblioteca; para que podamo ver tipos de usuarios:

- Alumno
- Profesor
- Bibliotecario

Todos son usuarios, pero cada uno puede tener permisos diferentes. Un alumno puede pedir libros prestados, un profesor puede tener más días de préstamo y un bibliotecario puede gestionar el catálogo. En este caso, Factory Method permite crear cada tipo de usuario de forma ordenada  sin llenar el programa principal de condiciones repetidas.

# Ventajas de este método (Factory Method)

- Separa la creación de objetos del resto del programa.
- Hace el código más ordenado.
- Facilita añadir nuevos tipos de objetos.
- Reduce la repetición de condiciones..

Por ejemplo, si en el futuro se quiere añadir un nuevo tipo de usuario, como "investigador", solo habría que añadir una nueva clase sin cambiar todo el programa.

# Cuándo utilizarlo

Principalmente cuando el programa necesita crear distintos tipos de objetos pero no quieres que el código principal dependa de clases concretas o si quieres entralizar la lógica de creación.

