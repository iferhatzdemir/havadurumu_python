#vericekmeye yardımcı olan kütüphane
import requests
#tarih zaman Kütüphanesi
import datetime
#anahtar değer şeklinde gelen veriyi bölmemize sağlar
import json
#openweathermap.org kayıt olarak aldığımız anahtar
apiKey = '10d816fd2ad802ecc70b04f152c75208'
#hangi şehirin havadurumunu istediğimizi tanımlıyoruz
#sehirİsmi='Isparta'
sehirİsmi=input("Şehir İsmi Giriniz")
#istek atacağımız url
orgin_url=(f'http://api.openweathermap.org/data/2.5/weather?q={sehirİsmi}&appid={apiKey}')
#response değeri tanımlayarak istek yapıyoruz
response = requests.get(orgin_url)
#veriyi jsonlaştırıyoruz
jsonResponse=json.loads(response.text)
#Hava Durumunun nasıl olduğunu çekiyoruz
skyDescription = jsonResponse['weather'][0]['description']
#hava durumunun ingilizceden türkçeye ceviriyoruz
skyTypes = ['clear sky', 'few clouds', 'overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain',
            'thunderstorm', 'snow', 'mist','light rain']
skyTypesTR = ['Güneşli', 'Az Bulutlu', 'Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu',
              'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Sisli','Hafif Yağmurlu']
for i in range(len(skyTypes)):
    if skyDescription == skyTypes[i]:
        skyDescription = skyTypesTR[i]

# For temp: Kelvin to Celcius:
# Sıcaklık bilgisini Kelvin den Celcius a çevirir ve aşağıdaki değişkenlerin içine atar.
temp = round((jsonResponse['main']['temp'] - 273.15), 2)  # Genel sıcaklık
feels_temp = round((jsonResponse['main']['feels_like'] - 273.15), 2)  # hissedilen
temp_min = round((jsonResponse['main']['temp_min'] - 273.15), 2)  # Minimum
temp_max = round((jsonResponse['main']['temp_max'] - 273.15), 2)  # Maksimum
cloud_rate=jsonResponse['clouds']['all'] #bulutluluk oranı
humidity=jsonResponse['main']['humidity'] #nem oranı
sunset_unix=jsonResponse["sys"]["sunset"] #gün batımı
sunrise_unix=jsonResponse["sys"]["sunrise"] #gün doğusu
datatime = jsonResponse["dt"] # veriyi aldığımız saati alıyoruz

#unix saati GTC tarzına çeviriyoruz
sunset=datetime.datetime.fromtimestamp(sunset_unix).strftime(' %H:%M:%S')
sunrise=datetime.datetime.fromtimestamp(sunrise_unix).strftime(' %H:%M:%S')
datatime_real=datetime.datetime.fromtimestamp(datatime).strftime('%d-%m-%y %H:%M:%S')

#çektiğimiz verileri ekranaa yazdırıyoruz
print("Sehir: "+ jsonResponse["name"])
print("Verinin Alındığı Tarih-Saat:"+datatime_real)
print("Gökyüzü:"+skyDescription)
print("Hava Sıcaklığı: "+str(temp)+" C")
print("Hissedilen Hava Sıcaklığı: "+str(feels_temp)+" C")
print("Minumum Sıcaklık: "+str(temp_min)+" C")
print("Maksimum Sıcaklık "+str(temp_max)+" C")
print("Nem Oranı : %"+str(humidity))
print("Bulutluluk Oranı:%"+str(cloud_rate))
print("Gün Batımı: "+sunset)
print("Gün Doğumu:"+sunrise)
