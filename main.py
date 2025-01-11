import package

# !program Utama
if __name__ == "__main__":
    package.Jendela_utama()


# user_option = input("Masukkan kota yang ingin di lihat : ")
# city_name = user_option.capitalize()
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=c64440556d3e8632d606a5ec0a226a6f"
# respons = requests.get(url)

# data_cuaca = respons.json() # * Mengambil json untuk kota
# suhu = data_cuaca["main"]["temp"] - 273.15

# if respons.status_code == 200:


#     print(f"Cuaca di {city_name}: {data_cuaca['weather'][0]['description']}")
#     print(f"Suhu: {round(suhu,2)}°C")

# else :
#     print("Error", respons.status_code)