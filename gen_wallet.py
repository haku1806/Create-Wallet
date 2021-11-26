#
# Quick creation of BSC/ETH wallet by python
# By: Haku1806
#

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from alive_progress import alive_bar
import csv, datetime

def gen_wallet_eth():
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    wallet_address = '0x' + addr.hex()
    return wallet_address, private_key.hex()


amount = int(input("Enter number of wallet ETH/BSC to create: "))

date_format = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = "wallet_{}_{}.csv".format(amount, date_format)

print('\nRunning...')
with alive_bar(amount) as bar:
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        
        # write the header
        header = ['STT', 'Address', 'PrivateKey']
        writer.writerow(header)

        # write the data
        for i in range(amount):
            wallet, priv = gen_wallet_eth()
            data = [i+1, wallet, priv]
            
            writer.writerow(data)
            bar()
        
print("\nSuccessfully created, please check the file \'{}\'".format(file_name))
