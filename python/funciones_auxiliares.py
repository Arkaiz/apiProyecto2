import decimal
import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)
    
        
def calculariva(importe):
    return importe*0.21