# Weather for Loxone Miniserver EN
## General information
This program allows you to send weather data downloaded from OpenWeatherMap to a mini server via UDP. In your code, you need to set variables:<br>
`udp_ip` as the minserver ip address<br>
`api_key` as the key you will get after registration on [OpenWeatherMap](https://openweathermap.org)<br>
`city_name` as the name of the city you want download the weather

In the "Loxone Config" application, click "Virtual Inputs" and then "Virtual UDP input". In the "Sender address" settings enter the IP address of the device on which you will run the script, and in "UDP receive port" enter the same port as in the `udp_port`.

Then you need to click on "Virtual UDP input command" and in the "Command recognition" section, enter the variable from the table below, e.g. `w_tt=\v`

## Table with variables
Variable   | Description
:----------:|:------------------------:|
w_tt | Current temperature in °C
w_pr | Pressure in hPa
w_fl | Current temperature feels like in °C
w_ws | Wind speed in m/s 
w_hmd | Current humidity 

## Author information
The creator of the script is Dominik Krzywański.<br>
Creator's website: [WolfRor](http://WolfRor.iwhy.me)

<hr>

# Pogoda dla Loxone Miniserwer PL
## Informacje ogólne
Ten program umożliwia wysyłanie danych pogodowych pobranych z OpenWeatherMap do mini serwera za pomocą UDP. W kodzie musisz ustawić zmienne:<br>
`udp_ip` jako adres ip miniserwera<br>
`api_key` jako klucz który dostaniesz po rejestracji na [OpenWeatherMap](https://openweathermap.org)<br> 
`city_name` jako nazwa miasta którego chesz pobrać pogodę

W aplikacji "Loxone Config" należy kliknąć "Wejścia wirtualne", a następnie "Wirtualne wejścia UDP". W ustawieniach w "Adres nadawcy" wpisz adres ip urządzenia na którym uruchomisz skrypt, a w "Port odbiorczy UDP" wpisz ten sam port co w zmiennej `udp_port`

Następnie musisz kliknąć na "Wirtualne wejścia UDP rozkaz" i w sekcji "Rozpoznawanie poleceń" należy wpisać zmienną z tabeli poniżej np. `w_tt=\v`

## Tabela ze zmiennymi
Zmienna   | Opis
:----------:|:------------------------:|
w_tt | Obecna temperatura w °C
w_pr | Ciśnienie w hPa
w_fl | Obecna odczuwalna temperatura w °C
w_ws | Prędkość wiatru w m/s 
w_hmd | Obecna wilgotność powietrza 

## Informacje o autorze
Twórcą skryptu jest Dominik Krzywański. <br>
Witryna twórcy: [WolfRor](http://WolfRor.iwhy.me)
