"""Funciones para el análisis exploratorio de datos"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_top_companies(df, n=10):
    """Obtiene las top n empresas por número de viajes"""
    return df.nlargest(n, 'trips_amount')

def get_top_neighborhoods(df, n=10):
    """Obtiene los top n barrios por promedio de viajes"""
    return df.nlargest(n, 'average_trips')

def plot_top_companies(df, n=10, save_path='../outputs/grafico_empresas.png'):
    """Crea gráfico de las top n empresas"""
    top = get_top_companies(df, n)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top, x='trips_amount', y='company_name', palette='viridis')
    plt.title(f'Top {n} Empresas de Taxis por Número de Viajes')
    plt.xlabel('Cantidad de Viajes')
    plt.ylabel('Empresa')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    return top

def plot_top_neighborhoods(df, n=10, save_path='../outputs/grafico_barrios.png'):
    """Crea gráfico de los top n barrios"""
    top = get_top_neighborhoods(df, n)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top, x='average_trips', y='dropoff_location_name', palette='viridis')
    plt.title(f'Top {n} Barrios por Promedio de Viajes')
    plt.xlabel('Promedio de Viajes')
    plt.ylabel('Barrio')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    return top