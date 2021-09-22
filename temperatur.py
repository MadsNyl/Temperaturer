class CsvEditor:

    def lagOrdbok(self, filnavn):
        ordbok = {}
        fil = open(filnavn, 'r')
        for linje in fil:
            måned, temp = linje.strip('\n').split(',')
            ordbok[måned] = float(temp)
        return ordbok
    
    def sjekkVarmeRekord(self, ordbok, filnavn):
        fil = open(filnavn, 'r')
        for linje in fil:
            måned, dag, temp = linje.strip('\n').split(',')
            for ordbok_måned in ordbok:
                if ordbok_måned == måned:
                    if ordbok[ordbok_måned] < float(temp):
                        print(ordbok[ordbok_måned])
                        ordbok[ordbok_måned] = float(temp)
                        print(ordbok[ordbok_måned])
        return ordbok
    
    def lagNyFil(self, ordbok, filnavn):
        fil = open(filnavn, 'w')
        for nøkkel in ordbok:
            fil.write(f'{nøkkel},{ordbok[nøkkel]}\n')
    
    def sjekkVarmebølge(self, filnavn):
        fil = open(filnavn, 'r')
        varmebølge_dager = []
        varmebølger = []
        for linje in fil:
            måned, dag, temp = linje.strip('\n').split(',')
            if float(temp) > 25:
                varmebølge_dager.append(f'{dag}.{måned}')
            else:
                varmebølger.append(varmebølge_dager)
                varmebølge_dager = []
        for liste in varmebølger:
            if len(liste) >= 5:
                print(f'Varmebølge! Start: {liste[0]}. Slutt: {liste[len(liste) - 1]}')
            




max_per_month_fil = 'Temperaturer/max_temperatures_per_month.csv'
max_daily_2018_fil = 'Temperaturer/max_daily_temperature_2018.csv' 

csv = CsvEditor()
min_ordbok = csv.lagOrdbok(max_per_month_fil)
print(min_ordbok)
varmerekord = csv.sjekkVarmeRekord(min_ordbok, max_daily_2018_fil)
print(varmerekord)
csv.lagNyFil(varmerekord, 'Temperaturer/nyVarmeRekord.csv')
csv.sjekkVarmebølge(max_daily_2018_fil)
