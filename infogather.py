import socket
import whois
import dns.resolver
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style

init(autoreset=True)

# Daftar port dan layanan umum
common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"
}

# ─── Tampilan Intro ────────────────────────
def print_intro():
    print(Fore.WHITE + r"""
        ________
       /      /|
      /______/ |         """ + Fore.GREEN + "INFO GATHERING TOOL" + Fore.WHITE + """
     |      |  |         """ + Fore.GREEN + "by kotaksuusu" + Fore.WHITE + """
     | MILK |  |      
     | BOX  |  |         
     |      |  |         
     |      | /          
     |______|/     
""" + Style.RESET_ALL)

    print(Fore.YELLOW + "👤 GitHub: " + Fore.GREEN + "Hanif_Albana" + Fore.WHITE + " | " + Fore.MAGENTA + "kotaksuusu\n" + Style.RESET_ALL)

# ─── Fungsi Info Gathering ─────────────────
def resolve_ip(domain):
    print(Fore.BLUE + "\n📡 [Resolving IP Address]")
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"✅ IP Address: {ip}")
    except Exception as e:
        print(Fore.RED + f"❌ Gagal resolve IP: {e}")

def whois_lookup(domain):
    print(Fore.BLUE + "\n📄 [WHOIS Lookup]")
    try:
        w = whois.whois(domain)
        for key, value in w.items():
            print(f"{Fore.YELLOW}    {key}: {Fore.WHITE}{value}")
    except Exception as e:
        print(Fore.RED + f"❌ Gagal WHOIS lookup: {e}")

def dns_lookup(domain):
    print(Fore.BLUE + "\n🌐 [DNS Records]")
    for rtype in ["A", "MX", "NS"]:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            for rdata in answers:
                print(f"{Fore.GREEN}    {rtype}: {Fore.WHITE}{rdata}")
        except:
            print(f"{Fore.RED}    {rtype}: Tidak ditemukan.")

def get_http_headers(domain):
    print(Fore.BLUE + "\n📥 [HTTP Headers]")
    try:
        url = f"http://{domain}"
        headers = requests.get(url, timeout=5).headers
        for key, value in headers.items():
            print(f"{Fore.YELLOW}    {key}: {Fore.WHITE}{value}")
    except Exception as e:
        print(Fore.RED + f"❌ Gagal mengambil headers: {e}")

# ─── Port Scanning (Hanya Open) ────────────
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                service = common_ports.get(port, "Unknown")
                return (port, "Open", service)
    except:
        pass
    return None

def scan_ports(domain):
    print(Fore.BLUE + "\n🚀 [Port Scanning - Menampilkan yang terbuka saja]")
    try:
        ip = socket.gethostbyname(domain)
    except Exception as e:
        print(Fore.RED + f"❌ Gagal resolve IP untuk port scanning: {e}")
        return

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(1, 1025)]
        for f in as_completed(futures):
            result = f.result()
            if result:
                port, status, service = result
                print(f"{Fore.GREEN}    Port {port:5d} | {status:6s} | {service}")

# ─── Main Program ─────────────────────────
def main():
    print_intro()
    domain = input(Fore.CYAN + "🔎 Masukkan domain (contoh: example.com): ").strip()
    print(Fore.LIGHTBLACK_EX + "=" * 60)

    resolve_ip(domain)
    whois_lookup(domain)
    dns_lookup(domain)
    get_http_headers(domain)
    scan_ports(domain)

if __name__ == "__main__":
    main()
