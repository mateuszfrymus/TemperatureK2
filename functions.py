def FindDateFromApi(content, list1, dt_txt):
    ListDate = [value[dt_txt] for value in content[list1]]
    return ListDate


def FindTempFromApi(content, list1, main, temp_max):
    number = 0
    ListTemp = []
    for value in content['list']:
        KelvinTemp = content['list'][number]['main']['temp_max']
        CelsTemp = KelvinTemp - 273.15
        ListTemp.append(CelsTemp)
        number += 1
    return ListTemp


def RoundNumber(list1):
    TempList = [round(list1[i], 2) for i, v in enumerate(list1)]
    list1.clear()
    return TempList


def DateForMaxTemp(list1, MaximumTemp, ListDate):
    for i, v in enumerate(list1):
        if v == MaximumTemp:
            return ("Maksymalna temperatura to:",
                    MaximumTemp, "°C. Będzie dnia:", ListDate[i])
