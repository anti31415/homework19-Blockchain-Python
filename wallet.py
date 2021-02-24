import subprocess
import json

command = 'php derive -g --mnemonic="index plug jaguar gesture vibrant scatter laugh above dragon alone memory vapor tree robust deer" --cols=path,address,privkey,pubkey --format=json --coin=ETH'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
