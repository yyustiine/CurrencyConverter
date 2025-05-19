from flask import Flask, render_template, request
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import os

app = Flask(__name__, static_folder="currency_chart/static")

API_KEY = 'fca_live_xa0BIncYUXOowI2zzWTs7xjCvAEB7QGdlUi7Of2o'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
HISTORICAL_URL = "https://api.freecurrencyapi.com/v1/historical"
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP", "CHF", "JPY", "HKD", "SGD"]

def draw_chart(currency_code, rates, dates):
    chart_dir = 'currency_chart_fixed/static'
    chart_path = os.path.join(chart_dir, 'chart.png')

    os.makedirs(chart_dir, exist_ok=True)
    if os.path.exists(chart_path):
        os.remove(chart_path)
        
    plt.style.use('dark_background')
    plt.figure(figsize=(8, 4))
    plt.plot(dates, rates, marker='o', linestyle='-', color='#00ff99')
    plt.title(f'{currency_code} to USD - Last year')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path

@app.route("/", methods=["GET", "POST"])
def index():
    top10_output = ""
    converted_output = ""
    chart_url = None
    
    if request.method == "POST":
        action = request.form.get("action")

        if action == "top10":
            base_currency = request.form.get("base_currency", "").upper()
            if base_currency in CURRENCIES:
                other_currencies = [cur for cur in CURRENCIES if cur != base_currency]
                url = f"{BASE_URL}&base={base_currency}&currencies={','.join(other_currencies)}"
                
                try:
                    response = requests.get(url)
                    data = response.json()["dataa"]
