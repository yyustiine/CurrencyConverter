from flask import Flask, render_template, request
import requests
import matplotlib.pyplot as plt
import datetime
import os

app = Flask(__name__, static_folder="currency_chart/static")
API_KEY = 'fca_live_xa0BIncYUXOowI2zzWTs7xjCvAEB7QGdlUi7Of2o'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
HISTORICAL_URL = "https://api.freecurrencyapi.com/v1/historical"
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP", "CHF", "JPY", "HKD", "SGD"]

def draw_chart(currency_code, rates, dates):
   if os.path.exists('currency_chart_fixed/static/chart.png'):
        os.remove('currency_chart_fixed/static/chart.png')
    plt.style.use('dark_background')
    plt.figure(figsize=(8, 4))
    plt.plot(dates, rates, marker='o', linestyle='-', color='#00ff99')
    plt.title(f'{currency_code} to USD - Last year')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    chart_path = os.path.join('currency_chart_fixed/static', 'chart.png')
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
            base = request.form.get("base_currency", "").upper()
            if base and base in CURRENCIES:
                filtered = [c for c in CURRENCIES if c != base]
                url = f"{BASE_URL}&base_currency={base}&currencies={','.join(filtered)}"
                try:
                    res = requests.get(url)
                    data = res.json().get("data", {})
                    if data:
                        top10_output = f"Base: {base}\n\n" + "\n".join(f"{k}: {v}" for k, v in data.items())
                except:
                    top10_output = "Error fetching data."
                   
                today = datetime.date.today()
                dates, rates = [], []
                for i in range(11, -1, -1):
                    date_obj = today - datetime.timedelta(days=i*30)
                    date_str = date_obj.strftime('%Y-%m-%d')
                    url = f"{HISTORICAL_URL}?apikey={API_KEY}&base_currency={base}&currencies=USD&date={date_str}"
                    try:
                        res = requests.get(url)
                        data = res.json().get('data', {}).get(date_str, {})
                        rate = data.get("USD")
                        if rate:
                            dates.append(date_obj.strftime('%Y-%m'))
                            rates.append(rate)
                    except:
                        continue
                if rates:
                    draw_chart(base, rates, dates)
                    chart_url = f"/static/chart.png?ts={int(datetime.datetime.now().timestamp())}"

                   
         elif action == "convert":
            try:
                amount = float(request.form.get("amount"))
                from_cur = request.form.get("from_currency", "").upper()
                to_cur = request.form.get("to_currency", "").upper()
                dropdown = request.form.get("dropdownCurrancy")
                if dropdown:
                    to_cur = dropdown
                if from_cur and to_cur and amount >= 0:
                    url = f"{BASE_URL}&base_currency={from_cur}&currencies={to_cur}"
                    res = requests.get(url)
                    rate = res.json().get("data", {}).get(to_cur)
                    if rate:
                        converted = amount * rate
                        converted_output = f"{amount} {from_cur} = {converted:.2f} {to_cur}"
                    else:
                        converted_output = "Invalid conversion."
            except:
                converted_output = "Conversion error."

   return render_template("index.html", top10=top10_output, amount_result=converted_output, chart_url=chart_url)

if __name__ == "__main__":
    os.makedirs("currency_chart_fixed/static", exist_ok=True)
    app.run(debug=True)
