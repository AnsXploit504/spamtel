import os, time, requests, random

# Warna
W = '\033[0m'
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'

pesan_acak = [
    "🔥 Hacked by AnsXploit",
    "💣 SPAM MODE: VVIP",
    "🚀 Powered by Telegram API",
    "👁️‍🗨️ Watching you...",
    "💥 BOOM!",
    "⚠️ Warning from AnsXploit",
    "💀 Welcome to dark mode"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def box_input():
    clear()
    print(C + "┌" + "─" * 50 + "┐")
    print(C + "│" + Y + "         TELEGRAM SPAMMER VVIP FINAL        " + C + "│")
    print(C + "│" + G + "           by Developer AnsXploit            " + C + "│")
    print(C + "├" + "─" * 50 + "┤" + W)

    token  = input(C + "│" + W + " [>] Token Bot Telegram             : " + W)
    target = input(C + "│" + W + " [>] ID Target (User/Group)         : " + W)
    pesan  = input(C + "│" + W + " [>] Isi Pesan (kosong = random)    : " + W)
    print(C + "│" + Y + " [!] SPAM TANPA BATAS. Tekan CTRL+C untuk stop " + C + "│")
    print(C + "└" + "─" * 50 + "┘" + W)
    return token, target, pesan

def tampilkan_box_status(log_lines):
    clear()
    print(C + "┌" + "─" * 50 + "┐")
    print(C + "│" + Y + "         🚀 SEDANG MENGIRIM PESAN...         " + C + "│")
    print(C + "├" + "─" * 50 + "┤" + W)
    for line in log_lines[-10:]:
        print(C + "│ " + W + f"{line:<48}" + C + "│")
    print(C + "└" + "─" * 50 + "┘" + W)

# Mulai
token, target, pesan = box_input()
pakai_random = (pesan.strip() == "")
log_lines = []
i = 1

try:
    while True:
        teks = pesan if not pakai_random else random.choice(pesan_acak)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": target, "text": teks}
        r = requests.post(url, data=data)

        if r.status_code == 200:
            log_lines.append(f"[✔] {i} terkirim")
        else:
            log_lines.append(f"[✖] Gagal di pesan ke-{i}")
            break

        tampilkan_box_status(log_lines)
        i += 1
        # Spam tanpa delay (secepat koneksi & server)
        # time.sleep(0.01)  # optional jika koneksi terbatas
except KeyboardInterrupt:
    print(R + "\n[!] SPAM Dihentikan oleh pengguna.\n" + W)

print(G + f"\n[✓] Total pesan terkirim: {i - 1}\n" + W)