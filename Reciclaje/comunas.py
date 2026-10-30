import json
from pathlib import Path
RUTA_GEO = Path(__file__).resolve().parent / 'data' / 'geo.json'

def obtener_comunas():
    with open(RUTA_GEO, 'r', encoding='utf-8') as f:
        data = json.load(f)
    nombres = {
        p['commune']['name'].strip()
        for p in data
        if p.get('commune') and p['commune'].get('name')
    }
    return sorted(nombres)
            