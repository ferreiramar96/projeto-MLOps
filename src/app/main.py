from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pandas as pd
from textblob import TextBlob
from deep_translator import GoogleTranslator
from sklearn.linear_model import LinearRegression
import pickle
import os
from dotenv import load_dotenv

project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
load_dotenv(dotenv_path)

colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('../../models/modelo_previsao_valor_casa.sav', 'rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route("/")
def home():
    return "Minha primeira API."

@app.route("/sentimento/<frase>")
@basic_auth.required
def sentimento(frase):
    translated = GoogleTranslator(source="auto", target="en").translate(frase)
    tb = TextBlob(translated)
    polaridade = tb.sentiment.polarity
    return f"polaridade: {polaridade}" 

@app.route("/cotacao/", methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True, host='0.0.0.0', port=5001)