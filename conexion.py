import cx_Oracle 
from datetime import date
from datetime import datetime


cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_11")

def log(texto):
    with open('log.log','a+') as f:
        f.read()
        f.write(str(datetime.now())+': '+texto+'\n') 
        f.close()
        
class conexion():
    def con_pos():
        conexion = None
        try:
            conexion =   cx_Oracle.connect(user='ka',password='K#0stazul',dsn='10.10.5.112:1521/oceanic',encoding='UTF-8')
            #print(f'verison bd: {conexion.version}')  
            return conexion
        except Exception as e:
            log('error verison bd:'+ str(e))    
            
            
    def con_dyjon():
        conexion = None
        try:
            conexion =   cx_Oracle.connect(user='kostaazul1',password='ocsxxi',dsn='s03.oceanicsa.com:1521/oceanic',encoding='UTF-8')
            #print(f'verison bd: {conexion.version}')  
            return conexion
        except Exception as e:
            log('error verison bd dyjon:'+ str(e))  
        #finally:
        #    conexion.close() 