from metno_locationforecast import Place, Forecast

place = Place("tromsø", 69.69, 19, 30)

my_forecast = Forecast(place, "metno-locationforecast/1.0 https://github.com/Rory-Sullivan/metno-locationforecast")

my_forecast.update()
print(my_forecast)