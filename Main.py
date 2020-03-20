import requests
import json
import webbrowser
from graph import *
from sqlite import *
from functions import *

params = {
    "appid": "570a250f89779fc9b0a36edc18a938d4",
    "lat": "35.88",
    "lon": "76.51"
}

r = requests.get('http://api.openweathermap.org/data/2.5/forecast?', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    ListDate = FindDateFromApi(content, 'list', 'dt_txt')
    ListTemp = FindTempFromApi(content, 'list', 'main', 'temp_max')
    TempList = RoundNumber(ListTemp)
    MaximumTemp = max(TempList)
    print(DateForMaxTemp(TempList, MaximumTemp, ListDate))

    conn = sqlite3.connect('temperature.db')
    c = conn.cursor()
    DeleteFromDB(c, conn)
    UpdateData(c, conn, ListDate, TempList)
    # ShowData(c)
    conn.close

    ShowGraph(ListDate, TempList, "Wykres temperatury",
              'Temperature at K2 in the next 5 days', 'Date and hour [yyyy-mm-dd hh:mm:ss]', '[°C]')
