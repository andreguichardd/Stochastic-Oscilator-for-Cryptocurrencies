import krakenex #Parte 0.0
from pykrakenapi import KrakenAPI #Parte 0.0
import pandas as pd

#########################################################################################
# Parte 0.0 
# El código a continuación está basado en el git entregado en el enunciado del proyecto #
# https://github.com/dominiktraxl/pykrakenapi                                           #
#########################################################################################

api = krakenex.API()
k = KrakenAPI(api)


# Esta función recibe como parámetro (stock) la acción de la que se quiere descargar la información de kraken

def obtener_stock(moneda='BTC'):

    df, last = k.get_ohlc_data(f'{moneda}USDT')    
    return(df)

def agrupar_datos(df):

    try:
    
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], unit='s') 
        df['formatted_time'] = df.iloc[:, 0].dt.strftime('%H:%M')
        #Toma la primera columna como el index y lo formatea de acuerdo a eso 
        df_agrupado = df.set_index(df.columns[0]).resample('5T').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
        return df_agrupado
    
    except Exception as e:
        return None
    
def obtener_volumen(df):

    try:
        v_5min = []
        entero = df['volume'].values.tolist()

        cont = 5

        for i in entero:
            if cont == 5:
                v_5min.append(i)
            
            if cont == 1:
                cont = 5
                continue

            else:
                cont -= 1
    except:
        print('Dataframe no tiene la estructura esperada')


    return v_5min


            
  




