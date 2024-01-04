import streamlit as st
import pandas as pd
import requests 



# Calcular el estocastico
def oscilador_estocastico(df, periodo=14, k=3, d=3):
    # Calcular el rango más alto (HH) y el rango más bajo (LL) para el período dado
    df['HH'] = df['high'].rolling(window=periodo).max()
    df['LL'] = df['low'].rolling(window=periodo).min()

    # Calcular %K
    denominator = df['HH'] - df['LL']
    
    # Revisa que el denominador no sea igual a cero
    mask = denominator != 0
    
    # Calcula % K y establece Nonce si el denominador es cero
    df['%K'] = 100 * (df['close'] - df['LL']) / denominator
    df['%K'] = df['%K'].where(mask)
    
    # Calcular %D (media móvil de %K)
    df['%D'] = df['%K'].rolling(window=d).mean()

    df.drop(["HH", "LL"], axis=1, inplace=True)
    
    return df
