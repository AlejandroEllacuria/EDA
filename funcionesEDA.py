def estilo_tabla(tabla):
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
            {"selector": "th", "props": [("background-color", "#003366"),
                                         ("color", "white"),
                                         ("font-size", "12pt"),
                                         ("padding", "6px")]},
            {"selector": "td", "props": [("padding", "6px")]}
        ])
        .hide(axis="index")
    )

