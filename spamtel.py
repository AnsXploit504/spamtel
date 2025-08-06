import requests, os, time
from colorama import Fore, Back, Style, init

init(autoreset=True)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(Fore.RED + "╔" + "═"*56 + "╗")
    print(Fore.YELLOW + "║" + Fore.CYAN + "         ⚔️  SPAM TELEGRAM - ANSXPLOIT  ⚔️         " + Fore.YELLOW + "║")
    print(Fore.RED + "╠" + "═"*56 + "╣")
    print(Fore.YELLOW + "║" + Fore.MAGENTA + "   Tool spam elite, support 100.000.000 spam    " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.GREEN + "       Gunakan dengan bijak & respect rules     " + Fore.YELLOW + "║")
    print(Fore.RED + "╚" + "═"*56 + "╝")
    print(Fore.LIGHTBLUE_EX + "\nCTRL + C untuk hentikan kapan saja!\n")

def input_data():
    print(Fore.LIGHTCYAN_EX + "╔═══════════════════ INPUT DATA ═══════════════════╗")
    token   = input(Fore.LIGHTGREEN_EX + "║ BOT Token Telegram   : " + Fore.WHITE)
    chat_id = input(Fore.LIGHTGREEN_EX + "║ ID Target Telegram   : " + Fore.WHITE)
    pesan   = input(Fore.LIGHTGREEN_EX + "║ Pesan Spam           : " + Fore.WHITE)
    jumlah  = int(input(Fore.LIGHTGREEN_EX + "║ Jumlah Spam (max 100jt): " + Fore.WHITE))
    print(Fore.LIGHTCYAN_EX + "╚══════════════════════════════════════════════════╝\n")
    return token, chat_id, pesan, jumlah

def kirim_spam(token, chat_id, pesan, jumlah):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        for i in range(1, jumlah + 1):
            data = {"chat_id": chat_id, "text": f"{pesan} [{i}]"}
            res = requests.post(url, data=data)
            if res.status_code == 200:
                print(Fore.GREEN + f"[✓] SPAM {i}/{jumlah} terkirim ke {chat_id}")
            else:
                print(Fore.RED + f"[✗] Gagal kirim ke {chat_id} (status: {res.status_code})")
            time.sleep(0.25)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] SPAM dihentikan manual!")
        exit()

def main():
    clear()
    banner()
    token, chat_id, pesan, jumlah = input_data()
    if jumlah > 100000000:
        print(Fore.RED + "[!] Maksimal 100.000.000 spam bang!")
        exit()
    print(Fore.LIGHTYELLOW_EX + "[•] Mulai mengirim spam...\n")
    kirim_spam(token, chat_id, pesan, jumlah)

if __name__ == "__main__":
    main()