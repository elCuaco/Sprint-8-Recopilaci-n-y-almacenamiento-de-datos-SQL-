# Análisis de Datos para Zuber - Chicago

## 🚀 Sobre el Proyecto
Análisis de datos para Zuber, una nueva empresa de viajes compartidos en Chicago.
El objetivo es identificar patrones de viajes y el impacto del clima en la duración de los mismos.

## 📊 Datos Utilizados
- **Empresas de Taxis**: Viajes realizados el 15-16 de noviembre 2017
- **Barrios de Chicago**: Promedio de viajes que terminan en cada barrio (nov 2017)
- **Viajes Loop → O'Hare**: Duración según condiciones climáticas

## 🔍 Resultados Clave

### 1. Empresas Dominantes
- **Flash Cab**: 19,558 viajes
- **Taxi Affiliation Services**: 11,422 viajes
- Estas dos empresas dominan el mercado

### 2. Barrios con Mayor Demanda
1. Loop (10,727 viajes)
2. River North (9,524 viajes)
3. Streeterville (6,665 viajes)

### 3. Impacto del Clima
- **Clima bueno**: 33.3 minutos de viaje
- **Clima malo**: 40.5 minutos de viaje
- **Diferencia**: +7.1 minutos en días lluviosos
- **Conclusión**: El clima afecta significativamente la duración

## 🛠️ Cómo Ejecutar

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Abrir el notebook
jupyter notebook notebooks/zuber_analysis.ipynb