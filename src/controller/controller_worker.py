import psycopg2

import sys
sys.path.append( "." )
sys.path.append("src")

import SecretConfig
from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction, Worker

class ControllerWorker:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute("""create table worker (
  id int primary key not null,
  salary_base float not null,
  months_worked int not null,
  vacation_day int not null,
  hours_extras int not null,
  extra_hours_nigth int not null,
  days_finish int not null
);""")
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute("""drop table worker""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def EliminarWorker(id):
        """ Borra el trabajador de la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute(f"""
        DELETE FROM worker
        WHERE id= {id};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def validar_modificacion(modificar, valor):
        if modificar == 'months_worked' and int(valor) <= 0:
            raise Months_workendExcepction()
        if modificar == 'salary_base' and float(valor) <= 0:
            raise SalarybaseExcepction()


    def ModificarWorker(id, modificar, valor):
        """Modificar trabajador"""
        ControllerWorker.validar_modificacion(modificar, valor)
        
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute(f"""
        UPDATE worker
        SET {modificar} = {valor}
        WHERE id = {id};
        """)
        cursor.connection.commit()

    def InsertarWorker( worker : Worker ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        try:
            cursor = ControllerWorker.ObtenerCursor()
            cursor.execute( f"""insert into worker (id, salary_base,months_worked, vacation_day,
                                hours_extras, extra_hours_nigth, 
                                days_finish) 
                            values ('{worker.id}', '{worker.salary_base}', '{worker.months_worked}',  
                                '{worker.vacation_day}', '{worker.hours_extra}',
                                '{worker.hours_extra_nigth}', '{worker.days_finish}')""" )
            cursor.connection.commit()

        except:
            cursor.connection.rollback()
            raise Exception ("No fue posible insertar el usuario " )

    def BuscarWorkerId( id ):
        """ Trae un usuario de la tabla de usuarios por la id """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute(f"""select id, salary_base, months_worked, vacation_day, hours_extras, extra_hours_nigth, days_finish
        from worker where id = {id}""" )

        try:
            fila = cursor.fetchone()
            resultado = Worker( id=fila[0], salary_base=fila[1], months_worked=fila[2], vacation_days=fila[3],
                                hours_extra=fila[4], hours_extra_nigth=fila[5], days_finish=fila[6] )
            return resultado
        except:
            raise ValueError("No se encontró ningún usuario con el ID buscado.")

    def calculate_liquidacion(worker_id):
        try:
            worker = ControllerWorker.BuscarWorkerId(id=worker_id)
            changeable_variables = {
                "vacation": worker.vacation_day,
                "extra_hours": worker.hours_extra,
                "extra_hours_nigth": worker.hours_extra_nigth,
                "days_finish": worker.days_finish
            }
            settlement_calculator = Settlementcalculator(worker.salary_base, worker.months_worked, changeable_variables)
            net_total = settlement_calculator.Calculate_net_total()
            return net_total
        except Exception as e:
            raise Exception(e)




    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        # Do not expose your Neon credentials to the browser
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor


def option(modificar):
    if modificar == 1:
        modificar= "id"
    if modificar == 2:
        modificar= "salary_base"
    if modificar == 3:
        modificar= "months_worked"
    if modificar == 4:
        modificar= "vacation_day"
    if modificar == 5:
        modificar= "hours_extras"
    if modificar == 6:
        modificar= "extra_hours_nigth"
    if modificar == 7:
        modificar= "days_finish"
    return modificar