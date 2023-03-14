import json
from Crypto.Cipher import AES

# Read the encrypted cookie data from file
with open('/home/llydo1/projects/samsidu/Taobao-Scrapping-app/Backend/Data/encrypted_cookie.json', 'r') as f:
    encrypted_data = json.load(f)

# Decrypt the encrypted data using the decryption key
decryption_key = b'Llydo1' # replace with your own key
cipher = AES.new(decryption_key, AES.MODE_CBC, IV=encrypted_data['iv'])
cookie_data = json.loads(cipher.decrypt(encrypted_data['value']).decode('utf-8'))

# Save the decrypted cookie data to a new file
with open('/home/llydo1/projects/samsidu/Taobao-Scrapping-app/Backend/Data/decrypted_cookie.json', 'w') as f:
    json.dump(cookie_data, f)
