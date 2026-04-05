import requests
import time

TOKEN = "8283636993:AAEGIltY7YtZdt7EghHuNajSiT-CRy6uQIA"
CHAT_ID = "5618520877"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": texto})
    print(r.text)

def obtener_precio(simbolo):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={simbolo}"
    try:
        data = requests.get(url).json()
        return data['quoteResponse']['result'][0]['regularMarketPrice']
    except:
        return None

# 🔥 ACTIVOS (TIENEN QUE IR ACÁ)
activos = {
    "BYMA.BA": {"compra": 318, "ruptura": 333},
    "PAMP.BA": {"compra": 5170, "ruptura": 5258},
    "SUPV.BA": {"compra": 2635, "ruptura": 2847},
    "GGAL.BA": {"compra": 6495, "ruptura": 7209},
    "TXAR.BA": {"compra": 680, "ruptura": 714},
    "LOMA.BA": {"compra": 1400, "ruptura": 1500},

    "AAPL": {"compra": 170, "ruptura": 190},
    "TSLA": {"compra": 180, "ruptura": 250},
    "NVDA": {"compra": 800, "ruptura": 950},
    "MSFT": {"compra": 300, "ruptura": 350},
    "GOOGL": {"compra": 130, "ruptura": 150},
    "MELI": {"compra": 1200, "ruptura": 1400},
    "XOM": {"compra": 95, "ruptura": 110},
    "KO": {"compra": 55, "ruptura": 65},
    "ITUB": {"compra": 6, "ruptura": 7},
    "VIST": {"compra": 30, "ruptura": 38},
    "URA": {"compra": 14.7, "ruptura": 16.2}
}

alertados = {}

enviar_mensaje("🚀 BOT ACTIVO ANI")

while True:
    for activo, niveles in activos.items():
        precio = obtener_precio(activo)

        if precio is None:
            continue

        if activo not in alertados:
            alertados[activo] = {"compra": False, "ruptura": False}

        if precio <= niveles["compra"] and not alertados[activo]["compra"]:
            enviar_mensaje(f"🟢 {activo} compra: {precio}")
            alertados[activo]["compra"] = True

        if precio > niveles["compra"]:
            alertados[activo]["compra"] = False

        if precio >= niveles["ruptura"] and not alertados[activo]["ruptura"]:
            enviar_mensaje(f"🚀 {activo} rompe: {precio}")
            alertados[activo]["ruptura"] = True

        if precio < niveles["ruptura"]:
            alertados[activo]["ruptura"] = False

    time.sleep(15)