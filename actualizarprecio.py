from conexion import  conexion
from datetime import date
from datetime import datetime

con_pos = conexion.con_pos()
con = conexion.con_dyjon()

def log(texto):
    with open('log.log','a+') as f:
        f.read()
        f.write(str(datetime.now())+': '+texto+'\n') 
        f.close()

def consulta_productos_a_cambiar():
    try:
        cursor = con_pos.cursor()
        sql = "select b.pr_producto,round(b.pr_costoultimo*1.2,0) costo,  b.pr_precioultimo tiquete from  productos@posoceanic a   "\
               " join   productos b on (a.pr_producto = b.pr_producto ) "\
               " where  a.pr_precioultimo <> b.pr_precioultimo or round(b.pr_costoultimo*1.2,0) <> round(a.pr_costoultimo*1.2,0)"\
        #print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        #print(data)
        cursor.close()
        con_pos.close()
        return data
    except Exception as e:
        log('error en consulta de porductos '+str(e))
        return 'error'
            
def is_list_empty(list):
    # checking the length
    if len(list) == 0:
    # returning true as length is 0
        return True
# returning false as length is greater than 0
    return False

         
def actualizar_productos():
    sql = "update productos set pr_precioultimo = :tiquete , pr_costoultimo = :costo where pr_producto = :producto"
    try:
        datos = consulta_productos_a_cambiar()
        if datos == 'error':
            log('hubo un error al consultar los datos')
        elif is_list_empty(datos):
            log('no hay datos en la consulta')
        else :
            for d in datos:  
                try:
                    cursor = con.cursor()
                    cursor.execute(sql, tiquete=d[2],costo=d[1],producto=d[0])
                    con.commit()
                    log('se actulizo el producto  '+str(d[0]+' con un precio de: ' + str(d[2]) + ' y un costo de: ' + str(d[1])))   
                except Exception as e:
                    print(e)
                    log('error insertando documentos'+ str(e))
                    con.rollback()
        con.close()
    except Exception as e1:
        log(str(e1))
                
if __name__ =='__main__':
    actualizar_productos()
    
