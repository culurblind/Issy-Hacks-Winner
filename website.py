# website.py creates combines out front end and back end code together and
# outputs a website as a visual while also running all the individual games 
# in a VS Code terminal

from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

balance = 1000

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def return_home():
    return render_template('home.html')

@app.route('/roulette')
def roulette():
    return render_template('roulette.html', result=balance)

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html', result=balance)

@app.route('/craps')
def craps():
    return render_template('craps.html', result=balance)

@app.route('/execute_blackjack', methods=['GET'])
def execute_blackjack():
    # Execute the bj.blackjack() method
    global balance
    balance = bj.blackJack(balance)
    return jsonify({'balance': balance})

@app.route('/execute_roulette', methods=['GET'])
def execute_roulette():
    # Execute the rl.roulette() method
    global balance
    balance = rl.roulette(balance)
    return jsonify({'balance': balance})

@app.route('/execute_craps', methods=['GET'])
def execute_craps():
    # Execute the cr.craps() method
    global balance
    balance = cr.craps(balance)
    return jsonify({'balance': balance})

@app.route('/get_balance', methods=['GET'])
def get_balance():
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)