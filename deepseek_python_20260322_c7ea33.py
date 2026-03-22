# %% [markdown]
# # Análisis de Datos para Zuber
# 
# ## Introducción
# Este análisis identifica patrones en viajes compartidos en Chicago y evalúa el impacto del clima.

# %% [markdown]
# ### 1. Importar Librerías

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("✅ Librerías cargadas correctamente")

# %% [markdown]
# ### 2. Cargar Datos

# %%
# Rutas de archivos
path_companies = '../data/moved_project_sql_result_01.csv'
path_neighborhoods = '../data/moved_project_sql_result_04.csv'
path_hypothesis = '../data/moved_project_sql_result_07.csv'

# Cargar datos
df_companies = pd.read_csv(path_companies)
df_neighborhoods = pd.read_csv(path_neighborhoods)
df_hypothesis = pd.read_csv(path_hypothesis, parse_dates=['start_ts'])

print("✅ Datos cargados correctamente")
print(f"Empresas: {df_companies.shape}")
print(f"Barrios: {df_neighborhoods.shape}")
print(f"Viajes: {df_hypothesis.shape}")

# %% [markdown]
# ### 3. Exploración Inicial

# %%
print("=== INFO EMPRESAS ===")
print(df_companies.info())
print("\n=== INFO BARRIOS ===")
print(df_neighborhoods.info())
print("\n=== INFO VIAJES ===")
print(df_hypothesis.info())

# %% [markdown]
# ### 4. Top 10 Barrios

# %%
top_barrios = df_neighborhoods.nlargest(10, 'average_trips')
print("\n=== TOP 10 BARRIOS ===")
print(top_barrios.to_string(index=False))

# %% [markdown]
# ### 5. Visualización: Empresas de Taxis

# %%
# Top 10 empresas
top_empresas = df_companies.nlargest(10, 'trips_amount')

# Gráfico
plt.figure()
sns.barplot(data=top_empresas, x='trips_amount', y='company_name', palette='viridis')
plt.title('Top 10 Empresas de Taxis por Número de Viajes')
plt.xlabel('Cantidad de Viajes')
plt.ylabel('Empresa')
plt.tight_layout()
plt.savefig('../outputs/grafico_empresas.png', dpi=300)
plt.show()

print("✅ Gráfico de empresas guardado")

# %% [markdown]
# ### 6. Visualización: Barrios

# %%
plt.figure()
sns.barplot(data=top_barrios, x='average_trips', y='dropoff_location_name', palette='viridis')
plt.title('Top 10 Barrios por Promedio de Viajes')
plt.xlabel('Promedio de Viajes')
plt.ylabel('Barrio')
plt.tight_layout()
plt.savefig('../outputs/grafico_barrios.png', dpi=300)
plt.show()

print("✅ Gráfico de barrios guardado")

# %% [markdown]
# ### 7. Prueba de Hipótesis: Impacto del Clima

# %%
# Separar datos por clima
good = df_hypothesis[df_hypothesis['weather_conditions'] == 'Good']['duration_seconds']
bad = df_hypothesis[df_hypothesis['weather_conditions'] == 'Bad']['duration_seconds']

# Estadísticas
print("\n=== ESTADÍSTICAS ===")
print(f"Clima Bueno - Media: {good.mean():.2f} segundos ({good.mean()/60:.2f} minutos)")
print(f"Clima Malo - Media: {bad.mean():.2f} segundos ({bad.mean()/60:.2f} minutos)")
print(f"Diferencia: {bad.mean() - good.mean():.2f} segundos ({(bad.mean() - good.mean())/60:.2f} minutos)")

# Prueba de Levene (igualdad de varianzas)
_, p_levene = stats.levene(good, bad)
print(f"\nPrueba de Levene p-value: {p_levene:.4f}")

# Prueba t de Student
t_stat, p_value = stats.ttest_ind(good, bad, equal_var=(p_levene > 0.05))

print(f"\n=== RESULTADOS PRUEBA T ===")
print(f"Estadístico t: {t_stat:.4f}")
print(f"P-value: {p_value:.2e}")

# Conclusión
alpha = 0.05
if p_value < alpha:
    print(f"\n✅ RECHAZAMOS la hipótesis nula")
    print(f"El clima SÍ afecta significativamente la duración del viaje")
    print(f"Diferencia: {bad.mean() - good.mean():.2f} segundos más en clima malo")
else:
    print(f"\n❌ NO rechazamos la hipótesis nula")
    print(f"No hay evidencia de que el clima afecte la duración")

# %% [markdown]
# ### 8. Conclusiones

# %%
print("\n" + "="*60)
print("CONCLUSIONES PRINCIPALES")
print("="*60)

print("""
1. MERCADO:
   - Flash Cab y Taxi Affiliation Services dominan el mercado
   - Zuber necesita una estrategia diferenciada

2. DEMANDA GEOGRÁFICA:
   - Loop, River North y Streeterville son los barrios con mayor demanda
   - O'Hare también es un punto importante de finalización de viajes

3. IMPACTO DEL CLIMA:
   - El clima afecta significativamente la duración de los viajes
   - Los viajes en clima malo duran 7.1 minutos más en promedio
   - Zuber debe considerar esto para:
     * Precios dinámicos
     * Estimaciones de tiempo de llegada
     * Gestión de flota en días lluviosos
""")