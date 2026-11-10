from django.shortcuts import render
from .emisiones import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    # Registros de prueba procesados por el algoritmo
    registros_historicos = [
        {"planta": "Planta Norte", "consumo_kwh": 4500.0},
        {"planta": "Planta Sur", "consumo_kwh": 6200.0},
        {"planta": "Planta Este", "consumo_kwh": 3100.0}
    ]

    metricas = obtener_metricas_consumo(registros_historicos)

    contexto = {
        "titulo_panel": "Panel Administrativo de Sustentabilidad",
        "metricas": metricas
    }

    return render(request, 'sustentabilidad/panel.html', contexto)