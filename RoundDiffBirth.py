import datetime
import math
from datetime import date

print("Heute ist der:")
today = date.today()
print(today)



print("Willkommen bei ROundDiffBirth")
print("Dieses Programm berechnet den altersunterschied zweier Menschen in anbetracht des aktuellen Datums.")
print("Es nimmt einem die Frage ab, ob die Person bereits geburstag hatte im Jahr und berechnet den Altersunterschied beider Menschen")

jungere_jahr = int(input("In welchem Jahr wurde die jüngere Person geboren?"))
jungere_monat = int(input("In welchem Monat wurde die jüngere geboren?"))
jungere_tag = int(input("An welchem Tag wurde die jüngere geboren?"))

altere_jahr =int(input("In welchem Jahr wurde die ältere geboren?"))
altere_monat=int(input("In welchem Monat wurde die ältere geboren?"))
altere_tag  =int(input("An welchem Tag wurde der ältere geboren"))


#TODO: Modulo irgendwas
def convertSecondsToYeahrs(seconds):
    SEKUNDEN_PRO_JAHR = 3.1709
    year = 0.0
    year = seconds / SEKUNDEN_PRO_JAHR
    return year



def getDate(year, month, day):
    return datetime.date(year,month,day)


h = getDate(2023,9,23)

x2 = getDate(jungere_jahr,jungere_monat,jungere_tag)
x1 = getDate(altere_jahr,altere_monat,altere_tag)


#TODO: Konvertiere delta in eine jahr,tag
def substractTwoBirthdays(earlierDate, laterDate):
    delta = laterDate - earlierDate
    #momentane ausgabe: -655 days, 0:00:00
    #gewünschte ausgabe: 6.55
    delta = delta.total_seconds()
    delta = convertSecondsToYeahrs(delta)
    print(delta)
    return delta
def roundUp(number):
    return math.ceil(number)
def convertDaysToYears(days):
    days = 1658
    years = days/365
    return years
def showResult():
    print("Der Altersunterschied beträgt {}", result)


result = roundUp(convertDaysToYears(substractTwoBirthdays(x2, x1))) 
print("Der Altersunterschied beträgt, "+ str(result) + "Jahre")


###############################UNIT TEST###############################

