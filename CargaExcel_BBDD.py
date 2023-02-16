from datetime import datetime, date,time
import pandas as pd
from os import path
import sys

import numpy as np
import mysql.connector




def leer_excel(ruta,name_hoja):
    """
    Función encargada de leer el archivo Excel con formato igual al de la BBDD.

    Parameters 
    -----------

    ruta : String
        String con la ruta al archivo excel que se quiere leer
    
    name_hoja : String
        String con la hoja del excel que se desea leer


    Returns
    ----------

    DataFrame
    """

    if isinstance(ruta, str) and isinstance(name_hoja,str):
        
        df = pd.read_excel(ruta, sheet_name = name_hoja)
        
        df = df.fillna('Null') #Las celdas vacías del Excel se rellenan con un NULL para que SQL lo entienda
        print("Lectura Correcta")
        return df

    else:
        raise TypeError("Ruta y nombre de la hoja deben ser STR y existir. ")





def Cargar_Excel_BBDD(Excel,Conexion):
    
    cursor = Conexion.cursor()

    for index, rows in Excel.iterrows():

        my_list=[rows.N_Registro,rows.Titulo,rows.Autor,rows.Fecha_compra,rows.Año_compra,rows.Valor_adquisicion,rows.Tasacion_actual,rows.Ubicacion,rows.Serie,rows.Edicion,rows.Ediciones_Totales	,
                rows.CEF_Autor	,rows.CEF_Galeria	,rows.Foto_HD	,rows.Historial_Procedencia	,rows.Año ,rows.Categoria	,rows.Caracteristicas, rows.Marco ,rows.Cristal,
                rows.Firma	,rows.Firma2,
                rows.Observaciones	,rows.OTROS_NOMBRES	,rows.Referencias	,rows.Proveedor	,rows.Embalaje,
                rows.Mol_Obra	,rows.Moa_Obra	,rows.Mop_Obra	,rows.Medidas_obra	,rows.Mml_marco	,rows.Mma_marco	,rows.Mmp_marco	,
                rows.Medidas_con_Marco	,rows.MCL_embalaje	,rows.MCA_embalaje	,rows.MCP_embalaje	,rows.Medidas_embalaje	,rows.Fecha_caja]


       
        
        
        query = "INSERT INTO Obras (N_Registro, Titulo, archivo_jpg ,Autor, Fecha_compra, Año_compra, Valor_adquisicion, Tasacion_actual, Ubicacion, Serie, Edicion, Ediciones_Totales, CEF_Autor, CEF_Galeria, Foto_HD, Historial_Procedencia, Año, Categoria, Caracteristicas, Marco,Cristal,Firma,Firma2,Observaciones,OTROS_NOMBRES,Referencias,Proveedor,Embalaje,Mol_Obra,Moa_Obra,Mop_Obra,Medidas_obra,Mml_marco,Mma_marco,Mmp_marco,Medidas_con_Marco,MCL_embalaje,MCA_embalaje,MCP_embalaje,Medidas_embalaje,Fecha_caja) VALUES ({},'{}','archivo1.jpg','{}','{}',{},{},{},'{}','{}',{},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(*my_list)
        
        cursor.execute(query)

        Conexion.commit()


def main():

    db = mysql.connector.connect(user='root', 
                            password='20cancrilA',
                            host='localhost',
                            database = 'proyectonatalia')



    df = leer_excel("data.xlsx","obras")

    Cargar_Excel_BBDD(df,db)

main()