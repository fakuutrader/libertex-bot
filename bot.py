import os, time, requests
from flask import Flask

app = Flask(__name__)

EMAIL = os.getenv("LIBERTEX_EMAIL", "")
PASSWORD = os.getenv("LIBERTEX_PASSWORD", "")
SYMBOL = os.getenv("SYMBOL", "EUR/USD")
AMOUNT = float(os.getenv("AMOUNT", "10"))
TAKE_PROFIT = float(os.getenv("TAKE_PROFIT", "20"))
STOP_LOSS = float(os.getenv("STOP_LOSS", "10"))

@app.route("/")
def home():
    return "Bot Libertex corriendo! - fakuutrader"

@app.route("/status")
def status():
    return {"status": "running", "symbol": SYMBOL, "amount": AMOUNT}

def bot_loop():
    print(f"Bot iniciado para {SYMBOL} - Monto: {AMOUNT}")
    print("Esperando configuracion de Libertex...")
    while True:
        # Aca va la logica de trading
        # Por ahora el bot queda en espera / modo demo
        print("Bot activo, revisando mercado...")
        time.sleep(60)

if __name__ == "__main__":
    import threading
    t = threading.Thread(target=bot_loop, daemon=True)
    t.start()
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
