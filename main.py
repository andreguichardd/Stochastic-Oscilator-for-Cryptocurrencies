import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import krakenex #Parte 0.0
from pykrakenapi import KrakenAPI #Parte 0.0
from kraken import obtener_stock,agrupar_datos, obtener_volumen 
from grafico import oscilador_estocastico
import plotly.subplots as sp
import matplotlib.pyplot as plt


#########################################################################################
# El código a continuación está basado en el git entregado en el enunciado del proyecto #
# https://github.com/dominiktraxl/pykrakenapi                                           #
#########################################################################################


api = krakenex.API()
k = KrakenAPI(api)

def main():

    ################################################### PASO 1 ###################################################

    # Pedir el ingreso de distintas cryptos
    monedas = ['BTC','ETH','SOL']
    crypto1 = st.sidebar.selectbox('¿Qué crypto quieres ver?:', monedas)

    # Encabezado de la aplicación Streamlit
    st.title(f'GRÁFICOS {crypto1} vs USDT')

    # Pedir el input del periodo, %K y %D al usuario
    periodo_2 = [14]
    for i in range(1,31):
        periodo_2.append(i)
    k_2 = [3]
    for i in range(1,11):
        k_2.append(i)
    d_2 = [3]
    for i in range(1,11):
        d_2.append(i)

    periodo = st.sidebar.selectbox('¿Qué periodo quieres introducir?: ', periodo_2)
    k = st.sidebar.selectbox('¿Qué valor de %K quieres introducir?: ', k_2)
    d = st.sidebar.selectbox('¿Qué valor de %D quieres introducir?: ', d_2)

    ##############################################################################################################

    ################################################# PASO  2 ####################################################

    # Obtener los datos de kraken en base a las monedas seleccionadas
    df = obtener_stock(crypto1)

    #Obtener el volumen casa 5 minutos
    volume = obtener_volumen(df)

    #Llamar a la funcion para agrupar los datos por cada 5 minutos
    df_agrupado = agrupar_datos(df)

    ##############################################################################################################

    ################################################# PASO  3 #################################################### 

    #Crear la figura fig que posteriormente va a ser graficada en streamlit    
    fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=[f'{crypto1}/USDT'])
    
    #Utilizando candlestick creo un gráfico de velas
    fig.add_trace(go.Candlestick(x=df_agrupado.index,
                             open=df_agrupado['open'],
                             high=df_agrupado['high'],
                             low=df_agrupado['low'],
                             close=df_agrupado['close'],
                             showlegend = False),
                row=1, col=1)

    #Este código se ocupa para darle color verde a las barras de compra y rojo a las barras de venta y graficar el volumen
    fig.add_trace(go.Bar(x = df_agrupado.index,
                         y = volume, 
                         showlegend=False,
                         marker_color=['green' if close_price > open_price else 'red' for open_price,
                                        close_price in zip(df_agrupado['open'],df_agrupado['close'])]),
                         row=2, col=1)
    
    fig.update_layout(title=f'{crypto1}/USDT',yaxis_title='Precio')

    #Graficar el grafico de velas
    st.plotly_chart(fig)

    ##############################################################################################################   

    ################################################# PASO  4 #################################################### 

    #Hacer el calculo de k y d usando la funcion oscilador_estocastico
    nuevo_df = oscilador_estocastico(df_agrupado,periodo=periodo,k=k,d=d)

    #Título gráfico estocástico
    st.subheader(f"Gráfico estocástico:  {crypto1}")

    # Crear figura nueva
    fig = go.Figure()

    # Graficar lineas %K y %D
    fig.add_trace(go.Scatter(x=nuevo_df.index, y=nuevo_df['%K'], mode='lines', name='%K', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=nuevo_df.index, y=nuevo_df['%D'], mode='lines', name='%D', line=dict(color='orange')))

    # Agregar líneas horizontales en y=20 y y=80
    fig.add_shape(dict(type='line', x0=nuevo_df.index.min(), x1=nuevo_df.index.max(), y0=20, y1=20, line=dict(color='green')))
    fig.add_shape(dict(type='line', x0=nuevo_df.index.min(), x1=nuevo_df.index.max(), y0=80, y1=80, line=dict(color='green')))

    # Configurar visuales del gráfico
    fig.update_layout(
                    xaxis_title='Fecha',
                    yaxis_title='Values')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

    ##############################################################################################################   

main()
