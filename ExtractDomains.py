import os,sys,time,re


TLD = ["ABB","ABBOTT","ABOGADO","AC","ACADEMY","ACCOUNTANT","ACCOUNTANTS","ACTIVE","ACTOR","AD","ADS","ADULT","AE","AERO","AF","AFL","AG","AGENCY","AI","AIG","AIRFORCE","AL","ALLFINANZ","ALSACE","AM","AMSTERDAM","AN","ANDROID","AO","APARTMENTS","AQ","AQUARELLE","AR","ARCHI","ARMY","ARPA","AS","ASIA","ASSOCIATES","AT","ATTORNEY","AU","AUCTION","AUDIO","AUTO","AUTOS","AW","AX","AXA","AZ","BA","BAND","BANK","BAR","BARCLAYCARD","BARCLAYS","BARGAINS","BAUHAUS","BAYERN","BB","BBC","BD","BE","BEER","BERLIN","BEST","BF","BG","BH","BI","BID","BIKE","BINGO","BIO","BIZ","BJ","BLACK","BLACKFRIDAY","BLOOMBERG","BLUE","BM","BMW","BN","BNPPARIBAS","BO","BOATS","BOND","BOO","BOUTIQUE","BR","BRIDGESTONE","BROKER","BRUSSELS","BS","BT","BUDAPEST","BUILD","BUILDERS","BUSINESS","BUZZ","BV","BW","BY","BZ","BZH","CA","CAB","CAFE","CAL","CAMERA","CAMP","CANCERRESEARCH","CANON","CAPETOWN","CAPITAL","CARAVAN","CARDS","CARE","CAREER","CAREERS","CARS","CARTIER","CASA","CASH","CASINO","CAT","CATERING","CBN","CC","CD","CENTER","CEO","CERN","CF","CFA","CFD","CG","CH","CHANNEL","CHAT","CHEAP","CHLOE","CHRISTMAS","CHROME","CHURCH","CI","CITIC","CITY","CK","CL","CLAIMS","CLEANING","CLICK","CLINIC","CLOTHING","CLUB","CM","CN","CO","COACH","CODES","COFFEE","COLLEGE","COLOGNE","COM","COMMUNITY","COMPANY","COMPUTER","CONDOS","CONSTRUCTION","CONSULTING","CONTRACTORS","COOKING","COOL","COOP","COUNTRY","COURSES","CR","CREDIT","CREDITCARD","CRICKET","CRS","CRUISES","CU","CUISINELLA","CV","CW","CX","CY","CYMRU","CYOU","CZ","DABUR","DAD","DANCE","DATE","DATING","DATSUN","DAY","DCLK","DE","DEALS","DEGREE","DELIVERY","DEMOCRAT","DENTAL","DENTIST","DESI","DESIGN","DEV","DIAMONDS","DIET","DIGITAL","DIRECT","DIRECTORY","DISCOUNT","DJ","DK","DM","DNP","DO","DOCS","DOG","DOHA","DOMAINS","DOOSAN","DOWNLOAD","DURBAN","DVAG","DZ","EAT","EC","EDU","EDUCATION","EE","EG","EMAIL","EMERCK","ENERGY","ENGINEER","ENGINEERING","ENTERPRISES","EPSON","EQUIPMENT","ER","ERNI","ES","ESQ","ESTATE","ET","EU","EUROVISION","EUS","EVENTS","EVERBANK","EXCHANGE","EXPERT","EXPOSED","EXPRESS","FAIL","FAITH","FAN","FANS","FARM","FASHION","FEEDBACK","FI","FILM","FINANCE","FINANCIAL","FIRMDALE","FISH","FISHING","FIT","FITNESS","FJ","FK","FLIGHTS","FLORIST","FLOWERS","FLSMIDTH","FLY","FM","FO","FOO","FOOTBALL","FOREX","FORSALE","FOUNDATION","FR","FRL","FROGANS","FUND","FURNITURE","FUTBOL","GA","GAL","GALLERY","GARDEN","GB","GBIZ","GD","GDN","GE","GENT","GF","GG","GGEE","GH","GI","GIFT","GIFTS","GIVES","GL","GLASS","GLE","GLOBAL","GLOBO","GM","GMAIL","GMO","GMX","GN","GOLD","GOLDPOINT","GOLF","GOO","GOOG","GOOGLE","GOP","GOV","GP","GQ","GR","GRAPHICS","GRATIS","GREEN","GRIPE","GS","GT","GU","GUGE","GUIDE","GUITARS","GURU","GW","GY","HAMBURG","HANGOUT","HAUS","HEALTHCARE","HELP","HERE","HERMES","HIPHOP","HITACHI","HIV","HK","HM","HN","HOLDINGS","HOLIDAY","HOMES","HONDA","HORSE","HOST","HOSTING","HOUSE","HOW","HR","HT","HU","IBM","ICU","ID","IE","IFM","IL","IM","IMMO","IMMOBILIEN","IN","INDUSTRIES","INFINITI","INFO","ING","INK","INSTITUTE","INSURE","INT","INTERNATIONAL","INVESTMENTS","IO","IQ","IR","IRISH","IS","IT","IWC","JAVA","JCB","JE","JETZT","JEWELRY","JM","JO","JOBS","JOBURG","JP","JUEGOS","KAUFEN","KDDI","KE","KG","KH","KI","KIM","KITCHEN","KIWI","KM","KN","KOELN","KOMATSU","KP","KR","KRD","KRED","KW","KY","KYOTO","KZ","LA","LACAIXA","LAND","LAT","LATROBE","LAWYER","LB","LC","LDS","LEASE","LECLERC","LEGAL","LGBT","LI","LIAISON","LIDL","LIFE","LIGHTING","LIMITED","LIMO","LINK","LK","LOAN","LOANS","LOL","LONDON","LOTTE","LOTTO","LOVE","LR","LS","LT","LTDA","LU","LUXE","LUXURY","LV","LY","MA","MADRID","MAIF","MAISON","MANAGEMENT","MANGO","MARKET","MARKETING","MARKETS","MARRIOTT","MC","MD","ME","MEDIA","MEET","MELBOURNE","MEME","MEMORIAL","MENU","MG","MH","MIAMI","MIL","MINI","MK","ML","MM","MMA","MN","MO","MOBI","MODA","MOE","MONASH","MONEY","MORMON","MORTGAGE","MOSCOW","MOTORCYCLES","MOV","MOVIE","MP","MQ","MR","MS","MT","MTN","MTPC","MU","MUSEUM","MV","MW","MX","MY","MZ","NA","NADEX","NAGOYA","NAME","NAVY","NC","NE","NET","NETWORK","NEUSTAR","NEW","NEWS","NEXUS","NF","NG","NGO","NHK","NI","NICO","NINJA","NISSAN","NL","NO","NP","NR","NRA","NRW","NTT","NU","NYC","NZ","OKINAWA","OM","ONE","ONG","ONL","ONLINE","OOO","ORACLE","ORG","ORGANIC","OSAKA","OTSUKA","OVH","PA","PAGE","PANERAI","PARIS","PARTNERS","PARTS","PARTY","PE","PF","PG","PH","PHARMACY","PHOTO","PHOTOGRAPHY","PHOTOS","PHYSIO","PIAGET","PICS","PICTET","PICTURES","PINK","PIZZA","PK","PL","PLACE","PLUMBING","PLUS","PM","PN","POHL","POKER","PORN","POST","PR","PRAXI","PRESS","PRO","PROD","PRODUCTIONS","PROF","PROPERTIES","PROPERTY","PS","PT","PUB","PW","PY","QA","QPON","QUEBEC","RACING","RE","REALTOR","RECIPES","RED","REDSTONE","REHAB","REISE","REISEN","REIT","REN","RENT","RENTALS","REPAIR","REPORT","REPUBLICAN","REST","RESTAURANT","REVIEW","REVIEWS","RICH","RIO","RIP","RO","ROCKS","RODEO","RS","RSVP","RU","RUHR","RW","RYUKYU","SA","SAARLAND","SALE","SAMSUNG","SAP","SARL","SAXO","SB","SC","SCA","SCB","SCHMIDT","SCHOLARSHIPS","SCHOOL","SCHULE","SCHWARZ","SCIENCE","SCOT","SD","SE","SEAT","SENER","SERVICES","SEW","SEX","SEXY","SG","SH","SHIKSHA","SHOES","SHOW","SHRIRAM","SI","SINGLES","SITE","SJ","SK","SKY","SL","SM","SN","SO","SOCIAL","SOFTWARE","SOHU","SOLAR","SOLUTIONS","SONY","SOY","SPACE","SPIEGEL","SPREADBETTING","SR","ST","STUDY","STYLE","SU","SUCKS","SUPPLIES","SUPPLY","SUPPORT","SURF","SURGERY","SUZUKI","SV","SWISS","SX","SY","SYDNEY","SYSTEMS","SZ","TAIPEI","TATAR","TATTOO","TAX","TC","TD","TEAM","TECH","TECHNOLOGY","TEL","TEMASEK","TENNIS","TF","TG","TH","TICKETS","TIENDA","TIPS","TIRES","TIROL","TJ","TK","TL","TM","TN","TO","TODAY","TOKYO","TOOLS","TOP","TORAY","TOSHIBA","TOURS","TOWN","TOYS","TR","TRADE","TRADING","TRAINING","TRAVEL","TRUST","TT","TUI","TV","TW","TZ","UA","UG","UK","UNIVERSITY","UNO","UOL","US","UY","UZ","VA","VACATIONS","VC","VE","VEGAS","VENTURES","VERSICHERUNG","VET","VG","VI","VIAJES","VIDEO","VILLAS","VISION","VLAANDEREN","VN","VODKA","VOTE","VOTING","VOTO","VOYAGE","VU","WALES","WANG","WATCH","WEBCAM","WEBSITE","WED","WEDDING","WEIR","WF","WHOSWHO","WIEN","WIKI","WILLIAMHILL","WIN","WME","WORK","WORKS","WORLD","WS","WTC","WTF","XEROX","XIN","XN--1QQW23A","XN--30RR7Y","XN--3BST00M","XN--3DS443G","XN--3E0B707E","XN--45BRJ9C","XN--45Q11C","XN--4GBRIM","XN--55QW42G","XN--55QX5D","XN--6FRZ82G","XN--6QQ986B3XL","XN--80ADXHKS","XN--80AO21A","XN--80ASEHDB","XN--80ASWG","XN--90A3AC","XN--90AIS","XN--9ET52U","XN--B4W605FERD","XN--C1AVG","XN--CG4BKI","XN--CLCHC0EA0B2G2A9GCD","XN--CZR694B","XN--CZRS0T","XN--CZRU2D","XN--D1ACJ3B","XN--D1ALF","XN--FIQ228C5HS","XN--FIQ64B","XN--FIQS8S","XN--FIQZ9S","XN--FLW351E","XN--FPCRJ9C3D","XN--FZC2C9E2C","XN--GECRJ9C","XN--H2BRJ9C","XN--HXT814E","XN--I1B6B1A6A2E","XN--IO0A7I","XN--J1AMH","XN--J6W193G","XN--KCRX77D1X4A","XN--KPRW13D","XN--KPRY57D","XN--KPUT3I","XN--L1ACC","XN--LGBBAT1AD8J","XN--MGB9AWBF","XN--MGBA3A4F16A","XN--MGBAAM7A8H","XN--MGBAB2BD","XN--MGBAYH7GPA","XN--MGBBH1A71E","XN--MGBC0A9AZCG","XN--MGBERP4A5D4AR","XN--MGBX4CD0AB","XN--MXTQ1M","XN--NGBC5AZD","XN--NODE","XN--NQV7F","XN--NQV7FS00EMA","XN--NYQY26A","XN--O3CW4H","XN--OGBPF8FL","XN--P1ACF","XN--P1AI","XN--PGBS0DH","XN--Q9JYB4C","XN--QCKA1PMC","XN--RHQV96G","XN--S9BRJ9C","XN--SES554G","XN--UNUP4Y","XN--VERMGENSBERATER-CTB","XN--VERMGENSBERATUNG-PWB","XN--VHQUV","XN--VUQ861B","XN--WGBH1C","XN--WGBL6A","XN--XHQ521B","XN--XKC2AL3HYE2A","XN--XKC2DL3A5EE0H","XN--YFRO4I67O","XN--YGBI2AMMX","XN--ZFR164B","XXX","XYZ","YACHTS","YANDEX","YE","YODOBASHI","YOGA","YOKOHAMA","YOUTUBE","YT","ZA","ZIP","ZM","ZONE","ZUERICH","ZW"]

def Extract(iFile):
    if os.path.exists(iFile)==False:
        print "File does not exist\r\n"
        return -1
    else:
        Length = os.path.getsize(iFile)
        if Length == 0:
            print "File of zero length\r\n"
            return -1
        else:
            fOut = open("Domains.txt","w")
            iFileX = open(iFile,"r")
            for f in iFileX:
                LineLength = len(f)
                for i in TLD:
                    s_TLD = "." + i
                    XInd = f.upper().find(s_TLD)
                    if XInd != -1:
                        XInd_x = XInd + len(s_TLD)
                        #if f[XInd_x].isalnum()==False or XInd_x == LineLength :
                        if f[XInd_x].isspace()==True or XInd_x == LineLength :
			    if XInd > 0 and f[XInd-1].isalnum() == True:
                                print "TLD: " + i
                                fOut.write("TLD: " + i + "\r\n")
                                print "Domain Found: " + f
                                fOut.write("Domain Found: " + f + "\r\n")
            iFileX.close()
            fOut.close()
            return 0

if len(sys.argv) != 2:
    print "Usage: ExtractDomains.py input_file\r\n"
    sys.exit(-1)
else:
    ret = Extract(sys.argv[1])
    sys.exit(ret)