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

# 1er PATRÓN --> Patrón creacional: Factory Method

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

# Resumen de ejepmlos 1 y 2

En estos dos ejemplos se aplica el patrón Factory Method en dos situaciones diferentes.

1er EJEMPLO --> En el primer ejemplo se usa para crear distintos tipos de usuarios dentro de una biblioteca. El programa tiene una clase general llamada Usuario y varias clases concretas: Alumno, Profesor y Bibliotecario. Cada una representa un tipo de usuario distinto y tiene permisos diferentes. 
La clase UsuarioFactory se encarga de crear el usuario correcto según el tipo que se le indique. Asñí, el programa no tiene que crear una clase directamente

2º EJEMPLO --> Usé Factory Method para crear distintos tipos de notificaciones. 
- La biblioteca puede enviar avisos por email, SMS o WhatsApp.

Para eso se crea una clase general llamada "Notificacion" y varias clases concretas  (NotificacionEmail, NotificacionSMS y NotificacionWhatsApp)
La clase NotificacionFactory decide el  tipo de notificación se crea según el valor que recibe.

# 2º PATRÓN --> Patrón de comportamiento: Strategy

El segundo patrón que he eñegido es Strategy. Este patrón pertenece al grupo de patrones de comportamiento porque no se centra tanto en crear objetos, sino en organizar cómo actúan esos objetos dentro del programa.

El objetivo principal de Strategy es separar distintas formas de hacer una misma tarea. En lugar de meter toda la lógica en una función llena de condiciones, crea una clase para cada forma de resolver el problema y asi el el programa puede elegir qué estrategia usar según la situación.

Esto es útil cuando una aplicación puede realizar una operación de varias maneras. Por ejemplo, en una biblioteca se puede calcular una multa de forma diferente dependiendo del tipo de usuario. Un alumno puede pagar una cantidad normal por cada día de retraso, un profesor puede pagar menos y un bibliotecario puede no pagar multa. Si todo eso se metiera en una sola función con muchos if, el codigo seria mucho mas complejo. En cambio con Strategy cada cálculo de multa queda separado en su propia clase. Strategy también facilita ampliar el programa por ejemplo si en adelante quiero añadir otro tipo de multa, no habría que modificar toda la clase principal y bastaría con crear una nueva estrategia.

# Resumen de los ejemplos de Strategy

En estos 2 ejemplos uso el patrón Strategy en dos situaciones diferentes dentro de una biblioteca.

- En el primer ejemplo para calcular multas por retraso en la devolución de libros.

La clase principal se llama Prestamo, pero esta clase no calcula directamente la multa suno que recibe una estrategia concreta según el tipo de usuario. 
Por ejemplo, un alumno paga una multa normal, un profesor paga una multa más baja y otro tipo de usuario puede no pagar multa. Gracias a esto, el cálculo de la multa no está mezclado dentro de una sola función con muchos "if", sino que cada forma de calcularla está separada en una clase diferente.

- En el segundo ejemplo para ordenar libros dentro del catálogo de la biblioteca.

El programa puede ordenar los libros de varias formas (título, año, autor...). En vez de crear una función enorme con todas las posibilidades, se crea una estrategia distinta para cada criterio de ordenación oudiendo así el catálogo ¡ cambiar la forma de ordenar los libros sin modificar el código principal.

En ambos, Strategy deja eEl programa  más limpio, porque cada comportamiento está en su propia clase. Además, si en el futuro se quiere añadir una nueva forma de calcular multas o una nueva forma de ordenar libros, se puede crear una nueva estrategia sin tener que cambiar demasiado el resto del programa.

# Conclusión final

En este trabajo he explicado e implementado dos patrones de diseño: 

- Factory Method
- Strategy

Ambos ayudan a organizar mejor el código, aunque cada uno se utiliza para resolver un problema diferente.

- Factory Method es un patrón creacional centrado en la creación de objetos.Gracias a este patrón, el programa principal no tiene que crear directamente cada objeto concreto, sino que delega esa tarea en una clase fábrica. Esto hace que el código quede más ordenado y sea más fácil añadir nuevos tipos en el futuro.

- Strategy, por otro lado, es un patrón de comportamiento que separa distintas formas de hacer una misma tarea. En vez de meter muchas condiciones dentro de una sola función, cada comportamiento se coloca en una clase diferente. Así, el programa puede cambiar de estrategia sin modificar demasiado la clase principal.

Después de hacer los ejemplos he entendido que os patrosnes resuelven problemas y ayudan a que el programa sea más fácil de entender, mantener y ampliar. 

