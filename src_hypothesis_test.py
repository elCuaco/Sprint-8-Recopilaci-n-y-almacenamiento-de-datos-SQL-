"""Funciones para la prueba de hipótesis"""

from scipy import stats

def test_weather_impact(df, alpha=0.05):
    """
    Prueba si el clima afecta la duración de los viajes
    
    Args:
        df: DataFrame con columnas 'weather_conditions' y 'duration_seconds'
        alpha: Nivel de significancia
    
    Returns:
        dict: Resultados de la prueba
    """
    # Separar grupos
    good = df[df['weather_conditions'] == 'Good']['duration_seconds']
    bad = df[df['weather_conditions'] == 'Bad']['duration_seconds']
    
    # Estadísticas descriptivas
    stats_dict = {
        'good_mean': good.mean(),
        'bad_mean': bad.mean(),
        'good_std': good.std(),
        'bad_std': bad.std(),
        'good_n': len(good),
        'bad_n': len(bad),
        'difference': bad.mean() - good.mean()
    }
    
    # Prueba de Levene para varianzas iguales
    _, p_levene = stats.levene(good, bad)
    
    # Prueba t
    t_stat, p_value = stats.ttest_ind(good, bad, equal_var=(p_levene > alpha))
    
    # Resultados
    results = {
        **stats_dict,
        't_statistic': t_stat,
        'p_value': p_value,
        'equal_var_assumed': p_levene > alpha,
        'reject_null': p_value < alpha,
        'levene_p': p_levene
    }
    
    return results

def print_test_results(results):
    """Imprime los resultados de la prueba de forma legible"""
    print("\n" + "="*60)
    print("PRUEBA DE HIPÓTESIS: IMPACTO DEL CLIMA")
    print("="*60)
    
    print("\n📊 ESTADÍSTICAS DESCRIPTIVAS:")
    print(f"Clima Bueno (n={results['good_n']}):")
    print(f"  Media: {results['good_mean']:.2f} seg ({results['good_mean']/60:.2f} min)")
    print(f"  Desv: {results['good_std']:.2f} seg")
    print(f"\nClima Malo (n={results['bad_n']}):")
    print(f"  Media: {results['bad_mean']:.2f} seg ({results['bad_mean']/60:.2f} min)")
    print(f"  Desv: {results['bad_std']:.2f} seg")
    print(f"\nDiferencia: {results['difference']:.2f} seg ({results['difference']/60:.2f} min)")
    
    print("\n📈 RESULTADOS ESTADÍSTICOS:")
    print(f"Prueba de Levene (varianzas): p-value = {results['levene_p']:.4f}")
    print(f"Prueba t: estadístico = {results['t_statistic']:.4f}")
    print(f"Prueba t: p-value = {results['p_value']:.2e}")
    
    print("\n🎯 DECISIÓN:")
    alpha = 0.05
    if results['reject_null']:
        print(f"✅ RECHAZAMOS la hipótesis nula (p-value = {results['p_value']:.2e} < {alpha})")
        print(f"   → El clima AFECTA significativamente la duración de los viajes")
    else:
        print(f"❌ NO rechazamos la hipótesis nula (p-value = {results['p_value']:.4f} >= {alpha})")
        print(f"   → No hay evidencia de que el clima afecte la duración")