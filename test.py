from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet
w = Wallet(JSONRPCWallet(port=28088))
print(w.address())



print(w.incoming())