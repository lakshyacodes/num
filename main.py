import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
message='''
	This program is only for educational purpose!
	created by @lakshya_codes.
	'''
print(message)
n1=input("Enter country code (without +):")
n2=input("Enter target mobile number:")
blank=''''''
number="+"+n1+n2
ch_number=phonenumbers.parse(number, "CH")
country=geocoder.country_name_for_number(ch_number,"en")
service_provider=carrier.name_for_number(ch_number,"en")
print(blank)
print("Service_provider:",service_provider)
print("Country:",country)