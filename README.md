# AirQuality_bot

Skrypt napisany na potrzeby laboratorium z Ochrony Środowiska. <br />
Autor:  Kacper Kaczmarek  <br />
 <br />

Konfiguracja: <br />
1.  Plik “config” <br />
    Format danych: <stacja_IMGW>\t<stacja_GIOŚ>\t…\t<stacja_GIOŚ>\t-1 <br />
    Przykład: 12330	944	943	-1 <br />
    Podczas pierwszego uruchomienia skryptu automatycznie pobierze punkty pomiarowe i zapisze je do pliku “config” <br />

2.  Katalog danych<br />
    W pliku “main.py” w linijce 4 w cudzysłowiu należy podać lokalizację pliku “config”, która będzie także lokalizacją zapisu danych. <br />

3.  Automatyczne uruchamianie skryptu<br />
    Pod linuxem można wykorzystać do tego celu crontab <br />
    https://crontab.guru/ <br />
    sudo apt-get install cron <br />

