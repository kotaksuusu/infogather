# infogather
Information  Gathering by Kotaksuusu


### 🧠 **InfoGather CLI Tool**

Tools ini adalah **alat informasi pengintaian (information gathering)** berbasis **Command Line Interface (CLI)** yang dibuat menggunakan Python, bertujuan untuk mengumpulkan informasi dasar dari suatu target (domain/website). Tools ini sangat cocok digunakan untuk **fase awal pengujian penetrasi (reconnaissance)**.

---

### 🎯 **Fitur Utama:**

1. **IP Resolver**
   Mengubah nama domain menjadi alamat IP.
   Contoh: `example.com → 93.184.216.34`

2. **WHOIS Lookup**
   Mengambil informasi pendaftaran domain seperti:

   * Pemilik domain
   * Registrar
   * Tanggal pendaftaran dan kadaluwarsa

3. **DNS Records**
   Menampilkan record DNS penting:

   * A (alamat IP)
   * MX (mail server)
   * NS (nameserver)

4. **HTTP Headers**
   Mengambil dan menampilkan header dari server HTTP target.
   Berguna untuk mengetahui:

   * Jenis server
   * Teknologi yang digunakan (Apache, Nginx, dll)

5. **Port Scanning (Only Open Ports)**
   Melakukan pemindaian port (1–1024) terhadap IP target dan hanya menampilkan port **yang terbuka** beserta layanan umum yang berjalan.
   Contoh output:

   ```
   Port    80 | Open   | HTTP
   Port   443 | Open   | HTTPS
   ```

---

### 🧃 **Identitas Tool:**

* Nama: **InfoGather CLI Tool**
* Developer: **kotaksuusu (GitHub: Hanif\_Albana)**
* Ciri khas: ASCII art berbentuk **milk box** 🥛
* Bahasa: **Python 3**
* Tampilan: **Berwarna** dengan bantuan `colorama`

---

### 🔧 Tujuan Penggunaan:

* Pemula belajar teknik reconnaissance
* Tahap awal pentesting
* Memetakan permukaan serangan (attack surface)
* Menjadi dasar untuk modul lanjutan seperti subdomain enumeration, vulnerability scanner, dll.

---

Mohon digunakan dengan bijak
