# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def estilo_tabla(tabla):
    """Aplica estilo visual a tablas para Jupyter."""
    return (
        tabla.style
        .background_gradient(cmap="Blues", subset=["suicidios_totales"])
        .format({
            "suicidios_totales": "{:,.0f}",
            "suicidios_prom_100k": "{:,.2f}",
            "poblacion_promedio": "{:,.0f}",
            "pib_anual_prom_usd": "{:,.0f}",
            "idh_promedio": "{:.3f}",
        })
        .set_properties(**{
            "text-align": "center",
            "font-size": "12pt",
            "border": "1px solid #333"
        })
        .set_table_styles([
            {"selector": "th",
             "props": [("background-color", "#003366"),
                       ("color", "white"),
                       ("font-size", "12pt"),
                       ("padding", "6px")]},
            {"selector": "td",
             "props": [("padding", "6px")]}
        ])
        .hide(axis="index")
    )


def enriquecer_csv_sin_wbgapi(ruta_csv_original, ruta_indicadores, ruta_salida=None):
    """
    Enriquecer el CSV principal con un segundo CSV de indicadores externos.

    Ambos deben contener:
        - iso_alpha3 (clave principal)
        - iso_alpha2 y flag_emoji opcionales

    Parámetros:
    -----------
    ruta_csv_original : str -> CSV principal
    ruta_indicadores  : str -> CSV con indicadores externos
    ruta_salida       : str|None -> Si se especifica, guarda el resultado

    Retorna:
    --------
    DataFrame final enriquecido.
    """
    df = pd.read_csv(ruta_csv_original)
    df_ind = pd.read_csv(ruta_indicadores)

    if "iso_alpha3" not in df.columns:
        raise ValueError("El CSV original debe incluir la columna 'iso_alpha3'.")
    if "iso_alpha3" not in df_ind.columns:
        raise ValueError("El CSV de indicadores debe incluir la columna 'iso_alpha3'.")

    df_final = df.merge(df_ind, on="iso_alpha3", how="left")

    if ruta_salida:
        df_final.to_csv(ruta_salida, index=False)

    return df_final

def winsorize(series, lower=0.01, upper=0.99):
    ql = series.quantile(lower)
    qh = series.quantile(upper)
    return series.clip(lower=ql, upper=qh)

def get_flag(country_name):
    try:
        c = pycountry.countries.lookup(country_name)
        code = c.alpha_2.upper()
        return chr(127397 + ord(code[0])) + chr(127397 + ord(code[1]))
    except:
        return None

# ============================================
# 1) Distribución de registros por país
# ============================================
'''
plt.figure(figsize=(14, 6))
kills["pais"].value_counts().plot(kind="bar")
plt.title("Registros por país en la muestra")
plt.xlabel("País")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()
'''
# ============================================
# 2) Distribución de registros por año
# ============================================
'''
plt.figure(figsize=(12, 4))
kills["anio"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribución de registros por año")
plt.xlabel("Año")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()
'''
# ============================================
# 3) Distribución por sexo
# ============================================
'''
plt.figure(figsize=(6, 4))
kills["sexo"].value_counts().plot(kind="bar")
plt.title("Distribución por sexo")
plt.xlabel("Sexo")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()
'''
# ============================================
# 4) Distribución por grupo de edad
# ============================================
'''
plt.figure(figsize=(8, 4))
kills["edad"].value_counts().plot(kind="bar")
plt.title("Distribución por grupo de edad")
plt.xlabel("Grupo de edad")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()
'''
# ============================================
# 5) Distribución por generación
# ============================================
'''
plt.figure(figsize=(10, 4))
kills["generacion"].value_counts().plot(kind="bar")
plt.title("Distribución por generación")
plt.xlabel("Generación")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()
'''


# ============================================
# Resumen de valores faltantes
# ============================================
""" print("--- Revisión de Valores Faltantes ---")
resumen_faltantes = pd.DataFrame({
    'Total Faltantes': kills.isnull().sum(),
    'Porcentaje (%)': (kills.isnull().sum() / len(kills) * 100).round(2)
})
print(resumen_faltantes[resumen_faltantes['Total Faltantes'] > 0])
print("-" * 40) """


# --------------------------------------------------------------
#  Gráfico simple: temperatura vs suicidios
# --------------------------------------------------------------
'''
if "temperature_celsius" in df.columns and tasa_col in df.columns:
    df_temp = df[["temperature_celsius", tasa_col]].dropna()

    plt.figure(figsize=(8,5))
    sns.scatterplot(
        data=df_temp,
        x="temperature_celsius",
        y=tasa_col,
        alpha=0.5,
        color=reds[3]
    )
    sns.regplot(
        data=df_temp,
        x="temperature_celsius",
        y=tasa_col,
        scatter=False,
        color="black",
        line_kws={"linewidth":2}
    )
    plt.title("Relación entre temperatura y tasa de suicidios")
    plt.xlabel("Temperatura media (°C)")
    plt.ylabel("Suicidios por 100k habitantes")
    plt.tight_layout()
    plt.show()

'''