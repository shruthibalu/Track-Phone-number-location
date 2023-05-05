import phonenumbers
from phonenumbers import geocoder,carrier,timezone
phone=input("enter number with country code:")
phonenumber =phonenumbers.parse(phone)
country_name=geocoder.description_for_number(phonenumber,'en')
service_provider=carrier.name_for_number(phonenumber,'en')
timezone=timezone.time_zones_for_number(phonenumber)
print("country name: ",country_name)
print("service provider name:" ,service_provider)
print("timezone: ",timezone)
