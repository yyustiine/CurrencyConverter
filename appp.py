from flask import Flask, render_tempalte, request
import requests
import matplotlib.pyplot as plt
import datetime
import os

app = Flask(__name__, static_folder="currency_chart/static")

API_KEY = 'fca_live_xa0BIncYUXOowI2zzWTs7xjCvAEB7QGdlUi7Of2o'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
HIST_URL = "https://api.freecurrencyapi.com/v1/historic" 
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP", "CHF", "JPY", "HKD", "SGD"]

def draw_chart(currency, rates, time_labels):
    if os.path.exists("currency_chart/static/chart.png"):
        os.remove("currency_chart/static/chart.png")
        
    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, rates, color="green")
    plt.title(f'{currency} to USD')
    plt.xlabel("Time")
    plt.ylabel("Rate")
    plt.tight_layout()
