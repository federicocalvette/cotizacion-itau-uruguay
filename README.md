# cotizacion-itau-uruguay

#### Flujo:
Se realiza una request a la URL de Itaú, donde se obtiene una respuesta XML con información acerca de la cotización. Se controla el status_code, si es un 200 se prosigue a parsear esa información a un diccionario. 
<br>

#### Ejemplo:
```json
{
    "cotizacion": {
        "USD": {
            "nombre": "Dolar",
            "iso": "USD",
            "compra": "37,55",
            "venta": "39,75"
        },
        "ARG": {
            "nombre": "Peso Argentino",
            "iso": "ARG",
            "compra": "0,05",
            "venta": "0,35"
        },
        "BRL": {
            "nombre": "Real",
            "iso": "BRL",
            "compra": "7,45",
            "venta": "9,25"
        },
        "EUR": {
            "nombre": "Euro",
            "iso": "EUR",
            "compra": "40,00",
            "venta": "44,90"
        },
        "UYI": {
            "nombre": "Unidad Indexada",
            "iso": "UYI",
            "compra": "5,71",
            "venta": "5,71"
        }
    },
    "informacion": {
        "mensaje": "Estas cotizaciones son en pesos uruguayos y solo a titulo informativo",
        "fecha_actualizacion": "2023-03-31 23:57:50.007520"
    }
}
```
<br>

### Primeros pasos
Correr:
```bash
    python3 -m venv env
```

```bash
    source env/bin/activate 
```

```bash
    pip install -r requirements.txt
```

```bash
    python3 main.py
```

