from flask import Flask, render_tempalte, request
import requests
import matplotlib.pyplot as plt
import datetime
import os

app = Flask(__name__, static_folder="currency_chart/static")

API_KEY = 'fca_live_xa0BIncYUXOowI2zzWTs7xjCvAEB7QGdlUi7Of2o'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
