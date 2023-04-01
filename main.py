import json
from datetime import datetime

import requests
import xmltodict

FECHA = str(datetime.now())

MONEDA_ISO = {
    'US.D': ('USD', 'Dolar'),
    'ARGP': ('ARG', 'Peso Argentino'),
    'CRUZ': ('BRL', 'Real'),
    'EUR': ('EUR', 'Euro'),
    'URGI': ('UYI', 'Unidad Indexada'),
}

COTIZACION = {
    'cotizacion':{},
    'informacion':{
        'mensaje': 'Estas cotizaciones son en pesos uruguayos y solo a titulo informativo',
        'fecha_actualizacion': FECHA
    }
}

respuesta = requests.get('https://www.itau.com.uy/inst/aci/cotiz.xml')

respuesta_diccionario = xmltodict.parse(respuesta.content)

lista_cotizaciones = respuesta_diccionario['root']['cotizacion']

for cotizacion in lista_cotizaciones:

    if cotizacion['moneda'] in MONEDA_ISO:

        COTIZACION['cotizacion'][MONEDA_ISO[cotizacion['moneda']][0]] = {
            'nombre': MONEDA_ISO[cotizacion['moneda']][1],
            'iso': MONEDA_ISO[cotizacion['moneda']][0],
            'compra': cotizacion['compra'],
            'venta': cotizacion['venta']
        }

print(json.dumps(COTIZACION, sort_keys=False, indent=4))    