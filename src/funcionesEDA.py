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
