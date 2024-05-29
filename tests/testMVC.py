import unittest
import sys
sys.path.append("src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import Worker, Months_workendExcepction,SalarybaseExcepction
from controller.controller_worker import ControllerWorker

class TestWorkerController(unittest.TestCase):

    def setUpClass():
        # Llamar a la clase Controlador para que cree las tablas
        try:
            ControllerWorker.EliminarTabla()
            ControllerWorker.CrearTabla()
        except:
            ControllerWorker.CrearTabla()

    def testInsertaryBucarWorker( self ):
        """Prueba que se inserta y se busca un trabajador."""

        #Insertar usuario en la tabla
        usuario_prueba = Worker( id = 12345, salary_base='1000000', months_worked = '60', 
                                vacation_days = '30', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(12345)

        #Verificar si lo trajo correctamente
        self.assertEqual(  usuario_prueba.id, usuario_buscado.id )

    def testInsertaryBucarWorker2( self ):
        """Prueba que se inserta y se busca un trabajador."""

        #Insertar usuario en la tabla
        usuario_prueba = Worker( id = 98765, salary_base='3000000', months_worked = '30', 
                                vacation_days = '40', hours_extra = '50', 
                                hours_extra_nigth = '13', days_finish = '20' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(98765)

        #Verificar si lo trajo correctamente
        self.assertEqual(  usuario_prueba.id, usuario_buscado.id )


    def testClavePrimaria ( self ):
        """Prueba que dispara un error al insertar dos trabajadores con la misma clave primaria."""
        #Insertar usuario en la tabla
        usuario_prueba = Worker( id = 00000, salary_base='1000000', months_worked = '60', 
                                vacation_days = '30', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30'  )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Insertar usuario con misma id
        usuario_otro = Worker (id = 00000, salary_base='1000000', months_worked = '120', 
                                vacation_days = '50', hours_extra = '30', 
                                hours_extra_nigth = '199', days_finish = '30' )

        #Verificar si salta la excepcion
        self.assertRaises(Exception, ControllerWorker.InsertarWorker, usuario_otro )

    def testErrorBuscarWorker( self ):
        """ Prueba que dispara un error al buscar una Id no existenta"""
        id=12344

        #Verificar si se disparo el error 
        self.assertRaises(Exception, ControllerWorker.BuscarWorkerId, id )

    def testEliminarWorker(self):
        """Prueba para verificar que se elimino correctamente un trabajador"""
        #Insertar trabajador en la tabla
        usuario_prueba = Worker( id = 98765, salary_base='2000000', months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Eliminar trabajador de la tabla
        ControllerWorker.EliminarWorker(98765)

        #Verificar si salta una excepcion al buscar un Worker elimado
        self.assertRaises(Exception, ControllerWorker.BuscarWorkerId, 98765)

    def testModificarSalarioBase(self):
        """Prueba que se modifica correctamente el salario base de un trabajador"""
        usuario_prueba = Worker( id= 44444, salary_base='4000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar salario base de la tabla
        modificar = 'salary_base'
        nuevo_salario = 8000000
        ControllerWorker.ModificarWorker(44444, modificar, nuevo_salario)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(44444)

        #Verificar el cambio en el salario base
        self.assertEqual( nuevo_salario, usuario_buscado.salary_base )


    def testErrorModificarSalarioBase(self):
        """Prueba que se lanza la excepción al intentar modificar el salario base a 0"""
        usuario_prueba = Worker(id=55555, salary_base='7000000', months_worked='20', 
                                vacation_days='45', hours_extra='30', 
                                hours_extra_nigth='15', days_finish='30')
        ControllerWorker.InsertarWorker(usuario_prueba)

        # Modificar salario base de la tabla
        modificar = 'salary_base'
        nuevo_salario_base = 0

        # Verificar si salta una excepcion al intentar modificar el salario base a 0
        with self.assertRaises(SalarybaseExcepction):
            ControllerWorker.ModificarWorker(55555, modificar, nuevo_salario_base)


    def testModificarMesesTrabajados(self):
        """Prueba que se modifica correctamente los meses trabajados de un trabajador"""
        usuario_prueba = Worker( id= 33333, salary_base='7000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar meses trabajados de la tabla
        modificar = 'months_worked'
        nuevo_meses_trabajados = 50
        ControllerWorker.ModificarWorker(33333, modificar, nuevo_meses_trabajados)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(33333)

        #Verificar el cambio en los meses trabajados
        self.assertEqual( nuevo_meses_trabajados, usuario_buscado.months_worked )



    def testErrorModificarMesesTrabajados(self):
        """Prueba que se lanza la excepción al intentar modificar los meses trabajados a 0"""
        usuario_prueba = Worker(id=22222, salary_base='7000000', months_worked='20', 
                                vacation_days='45', hours_extra='30', 
                                hours_extra_nigth='15', days_finish='30')
        ControllerWorker.InsertarWorker(usuario_prueba)

        # Modificar meses trabajados de la tabla
        modificar = 'months_worked'
        nuevo_meses_trabajados = 0

        # Verificar si salta una excepcion al intentar modificar los meses trabajados a 0
        with self.assertRaises(Months_workendExcepction):
            ControllerWorker.ModificarWorker(22222, modificar, nuevo_meses_trabajados)


    def testModificarDiasdeVacaciones(self):
        """Prueba que se modifica correctamente los meses trabajados de un trabajador"""
        usuario_prueba = Worker( id= 45623, salary_base='7000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar dias de vacaciones de la tabla
        modificar = 'vacation_day'
        nuevo_dias_vacaciones = 50
        ControllerWorker.ModificarWorker(45623, modificar, nuevo_dias_vacaciones)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(45623)

        #Verificar el cambio en los dias de vacaciones
        self.assertEqual( nuevo_dias_vacaciones, usuario_buscado.vacation_day )


    def testModificarHorasExtra(self):
        """Prueba que se modifica correctamente los meses trabajados de un trabajador"""
        usuario_prueba = Worker( id= 10938, salary_base='7000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar horas extra de la tabla
        modificar = 'hours_extras'
        nuevo_horas_extra = 50
        ControllerWorker.ModificarWorker(10938, modificar, nuevo_horas_extra)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(10938)

        #Verificar el cambio en las horas extra
        self.assertEqual( nuevo_horas_extra, usuario_buscado.hours_extra )


    def testModificarHorasExtraNoche(self):
        """Prueba que se modifica correctamente los meses trabajados de un trabajador"""
        usuario_prueba = Worker( id= 10001, salary_base='7000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar horas extra nocturnas de la tabla
        modificar = 'extra_hours_nigth'
        nuevo_horas_extra_noche = 50
        ControllerWorker.ModificarWorker(10001, modificar, nuevo_horas_extra_noche)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(10001)

        #Verificar el cambio en las horas extra nocturnas
        self.assertEqual( nuevo_horas_extra_noche, usuario_buscado.hours_extra_nigth )

    def testModificarDiasFinalizar(self):
        """Prueba que se modifica correctamente los meses trabajados de un trabajador"""
        usuario_prueba = Worker( id= 50001, salary_base='7000000',  months_worked = '20', 
                                vacation_days = '45', hours_extra = '30', 
                                hours_extra_nigth = '15', days_finish = '30' )
        ControllerWorker.InsertarWorker(usuario_prueba)

        #Modificar dias para finalizar contrato de la tabla
        modificar = 'days_finish'
        nuevo_dias_final = 50
        ControllerWorker.ModificarWorker(50001, modificar, nuevo_dias_final)

        #Buscar el usuario
        usuario_buscado = ControllerWorker.BuscarWorkerId(50001)

        #Verificar el cambio en los dias para finalizar contrato
        self.assertEqual( nuevo_dias_final, usuario_buscado.days_finish )

if __name__ == "__main__":
    unittest.main()