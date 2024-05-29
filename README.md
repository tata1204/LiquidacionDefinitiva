# LiquidacionDefinitiva

## Elaborado por:
- Mayezly Tatiana Gafaro Boada
- Miguer Ayala

## ¿Qué es y para qué es?

El proyecto es una calculadora de liquidacion definitiva; se utiliza para calcular el pago de liquidación cuando empleado
sale de la empresa, por despido, renuncia, finalización de contrado, entre otros.

##Pre-requisitos

- Python 3.x instalado en tu sistema.
- La biblioteca Kivy, esta se puede instalar ejecutando pip install kivy.
- La libreria unittest que permite correr las prubas unitarias.
- La libreria sys que permite importar clases de otras carpetas.

  ##¿Cómo esta hecho?

- Carpeta 'sql': Contiene los archivos .sql donde se encuentra la instrucción sql para crear las tablas en NeonDB.
  - create_worker.sql: Se encuentra la instrucción sql para crear las tabla de usuarios en NeonDB.

- Carpeta 'src': Contiene en controller, mmodel y los view tanto por consola como por el gui.

  - Carpeta 'controller': Contiene los controladores de las tablas de la base de datos.
  - Carpeta 'model': Contiene la lógica huffman, ademas de la creación de los objetos historial y usuario.
  - Carpeta 'view-console': Contiene la interfaz por consola conectada a la base de datos.
  - Carpeta 'view-gui': Contiene la interfaz gráfica.
  - Carpeta 'tests': Contiene pruebas unitarias para la lógica de la aplicación.

- Carpeta 'templates': Contiene la lógica de las rutas de la aplicación Web

- app.py : Contiene la lógica para el correcto funcionamiento de la aplicación Web.

- SecretConfig.py : Contiene la conexión a la base de datos NeonDB.

##Uso

Para poder hacer uso de la base de datos debe conectarse a su NeonDB, incluyendo los datos de conexión en SecretConfig-sample.py 
y renombrando el archivo como SecretConfig.py.
Para ejecutarlo por la terminal recuerde especificar la ruta de busqueda.

- Uso por consola: src/console/interfaz.py.
- Uso de la aplicación Web: python app.py
- Uso de las pruebas unitarias:
  - Pruebas unitarias de la lógica: python tests\liquidacionTest.py
  - Pruebas unitarias MVC: python tests\testMVC.py
 
