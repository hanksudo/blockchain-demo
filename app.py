from flask import Flask, request
node = Flask(__name__)


# Store the transactions this node has in a list.
node_transactions = []

@node.route("/txion", methods=["POST"])
def transaction():
    # Extract transaction data
    new_txion = request.get_json()
    # Add transaction to list
    node_transactions.append(new_txion)

    # Log
    print("New transaction")
    print("FROM: {}".format(new_txion["from"]))
    print("TO: {}".format(new_txion["to"]))
    print("AMOUNT: {}\n".format(new_txion["amount"]))

    return "Transaction submission successful\n"