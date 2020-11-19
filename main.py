a = 70
b = 70 > b > 40
while True:
    print("Temperature" + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > a:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) < b:
        light.set_pixel_color(5, light.rgb(0, 255, 0)
    else:
        light.set_pixel_color(5, light.rgb(0, 0, 255)