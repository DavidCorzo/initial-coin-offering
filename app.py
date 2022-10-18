from flask import Flask, render_template, request
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/95ef02cced1249e18967d4b77f003341'))
app = Flask(__name__)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        from_addr = request.form['address']
        private_key = request.form['private_key']
        amount = request.form['amount']
        print(from_addr, private_key, amount)
        address_contract = web3.toChecksumAddress('0x2d089c7450177b7d5b013304d5d5a3a5bec55852') 
        nonce = web3.eth.getTransactionCount(from_addr)
        amount = request.form['amount']
        tx = {
            'nonce': nonce, 'to' : address_contract, 'value': web3.toWei(str(amount),'ether'), 'gas': 86000, 'gasPrice': web3.toWei(40,'gwei')

        }

        signed_transaction = web3.eth.account.sign_transaction(tx,private_key)
        tx_transaction = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        print(tx_transaction)
    return render_template('login.html')

# @app.route('/', methods=['POST', 'GET'])
# def home():
#     print(request.form['sendTo'])
#     return render_template('template.html')

# address: 0x05De64AdC505918A77EAe3D82d112e534EB710F7
# private key: 782359de410c9d3762bac46b05f249a3910f60625e75da82b517ac06a718642c


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)