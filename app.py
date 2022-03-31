######### MODULES
from web3 import Web3,HTTPProvider
from web3.middleware import geth_poa, geth_poa_middleware
import json
from flask import Flask,request

######### SETTING OBJECTS
w3 = Web3(Web3.HTTPProvider("https://mainnet-rpc.thundercore.com"))
app = Flask(__name__)
private_key = "87c420a33aed96949ca87c1c6604a412fc60efe7444818f62838ed0abe1d8c7b"
mainAddress = "0x984AAa257F7a143bbc57e834F8b2C40CfBE2DF15"
nonce = w3.eth.getTransactionCount(mainAddress)

######## SETTING UP FUNCTION
def sendThunderToken(to, value):
  nonce = w3.eth.getTransactionCount(mainAddress)
  tx = {
  'nonce' : nonce,
  'to' : to,
  'value' : w3.toWei(value , 'ether'),
  'gas' : 39002,
  'gasPrice' : w3.toWei('50', 'gwei')
  }
  sign_tx = w3.eth.account.signTransaction(tx, private_key)
  tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
  txn = w3.toHex(tran_hash)
  return txn

####### CREATEING API
@app.route('/test')
def setuphandler():
	nonce = w3.eth.getTransactionCount(mainAddress)
	return str(nonce)

@app.route('/sendThunderToken', methods = ['POST'])
def sendZilHandler():
	index = request.json
	address = index["address"]
	amount = index["amount"]
	tx = sendThunderToken(address, amount)
	return tx
