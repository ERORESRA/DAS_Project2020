La clean architecure es un diseno que se utiliza para enfatizar la estructura y la relacion de diversos componentes del codigo para promover la idea de la regla de la dependencia, de modo que las dependencias del codigo fuente solo apuntan hacia adentro. 

1. Independiente de Frameworks: La arquitectura no depende de la existencia alguna de la biblioteca software.
2. Comprobable: Las reglas comerciales se pueden probar sin la IU, la base de datos, servidor web o cualquier otro elemento.
3. Independiente de la IU: La IU puede cambiar facilmente sin cambiar el resto del sistema
4. Independiente de la base de datos: Puede utilizar cualquier base de datos ya que sus reglas comerciales no estan vinculadas a esta (Oracle, SQL, Mongo).
5. Independiente de cualquier agencia externa

Dentro del diagrama podemos ver que este es separado en 4 capas
- Capa de Entidades: describe el comportamiento universal de cualquier objeto dentro de toda la aplicacion
- Capa de Casos de uso: Define como tu aplicacion interactua con la capa de las identidades
- Capa de Adaptador de interfaz: La capa que implementa varias interfaces, esta se define en la capa de casos de uso
- Capa Configuracion: Esta capa es la encargada de reunir todos los componentes de codigo y exponerlas para ser usadas.