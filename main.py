from pydoc import render_doc
from flask import Flask
from flask import render_template, jsonify, request
from flask_cors import CORS, cross_origin
import ciphers
import os 

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin(origins='*')
def hello_world():
    return render_template("index.html")

@app.route("/columnar_transposition_cipher", methods=["POST"])
@cross_origin(origins='*')
def columnar_cipher():
    # get class 
    print("IN COLUMNAR")
    request_data = request.get_json()
    cipher = ciphers.Columnar_Transposition(request_data["key"])
    if (request_data["encryptFlag"] == "encrypt"):
        response = {"text": cipher.encrypt(request_data["userInput"]) }
    else: 
        response = {"text": cipher.decrypt(request_data["userInput"]) }

    return jsonify(response)

@app.route("/vigenere_cipher", methods=["POST"])
@cross_origin(origins='*')
def vigenere_cipher():
    # get class 
    print("IN VIGEENRE")
    request_data = request.get_json()
    cipher = ciphers.Vigenere(request_data["key"])
    if (request_data["encryptFlag"] == "encrypt"):
        response = {"text": cipher.encrypt(request_data["userInput"]) }
        print("this is the response", response)
    else: 
        response = {"text": cipher.decrypt(request_data["userInput"]) }

    return jsonify(response)

@app.route("/ceasar_cipher", methods=["POST"])
@cross_origin(origins='*')
def ceasar_cipher():
    # get class 
    #print("IN CEASAR CIPHER")
    request_data = request.get_json()
    cipher = ciphers.Ceaser_Cipher(int( request_data["key"] ))
    if (request_data["encryptFlag"] == "encrypt"):
        response = {"text": cipher.encrypt(request_data["userInput"]) }
    else: 
        response = {"text": cipher.decrypt(request_data["userInput"]) }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
