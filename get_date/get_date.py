import datetime
import calendar


class Irasas():
    def __init__(self, diena, pavadinimas):
        self.diena = diena
        self.pavadinimas = pavadinimas
        self.dienu_sarasas = []
        self.atr_dienu_sarasas = []
        self.paskutine_diena = []

    def get_diena(self, diena):
        kuri_diena = self.diena
        self.diena = diena
        self.dienu_sarasas.append(kuri_diena)  # sutvarkyti formatavyma

    def get_pavadinimas(self, pavadinimas):
        kokia_diena = self.pavadinimas
        self.pavadinimas = pavadinimas

    def get_sekmadienis(self, diena):
        kuri_diena = self.diena
        dienos_pavadinimas = datetime.date.weekday(diena)
        self.diena = diena
        kokia_diena = self.pavadinimas

        if len(self.dienu_sarasas) > 0:
            if calendar.day_name[dienos_pavadinimas] == kokia_diena:
                self.atr_dienu_sarasas.append(
                    (f'{kokia_diena} - {kuri_diena}'))

        else:
            print('Dienu sarasas tuscias')

    def get_parodyti_atsakyma(self):
        if len(self.dienu_sarasas) > 0:
            print(
                f'\n====Dienu Sarasas ====\n{self.dienu_sarasas}\n========\n')

        else:
            print(f'\n==== Sarasas tuscias ====\n')

        if len(self.atr_dienu_sarasas) > 0:
            print(
                f'\n==== {self.pavadinimas} list ====\n{self.atr_dienu_sarasas}\n========\n')
        else:
            print(f'\n==== Atrinktu dienu sarasas tuscias ====\n')

        if len(dienos_ivestis) == 0:
            print(f'\n==== Nepasirinkta diena ====\n')
        else:
            (f'\n==== Pasirinkta diena ====\n{dienos_ivestis}\n========\n')

    def get_trinti(self):
        if len(self.dienu_sarasas) < 1:
            print(f'\n==== Dienu sarasas tuscias ====\n')
        else:
            while len(self.dienu_sarasas) > 0:
                self.dienu_sarasas.pop()
        if len(self.atr_dienu_sarasas) < 1:
            print(f'\n==== Dienu sarasas tuscias ====\n')
        else:
            while len(self.atr_dienu_sarasas) > 0:
                self.atr_dienu_sarasas.pop()
        if len(dienos_ivestis) > 0:
            dienos_ivestis = ''
        else:
            print(f'\n==== Nepasirinkta diena ====\n')
        print('\n===========\nRezultatas istrintas\n===========\n')

    def get_paskutine_diena(self):
        if len(dienos_ivestis) > 0:
            if len(self.atr_dienu_sarasas) > 0:
                self.paskutine_diena.append(self.atr_dienu_sarasas[0])
                print(
                    f'\n===========\n Paskutinis {dienos_ivestis} buvo {self.paskutine_diena}\n===========\n')
            else:
                print('\n===========\nAtrinktu dienu sarasas tuscias\n===========\n')
        else:
            print('\n===========\nNepasirinkta diena\n===========\n')

    def __str__(self):
        return f'{self.diena,self.pavadinimas}'

    def __repr__(self):
        return f'{self.diena}, {self.pavadinimas}'


ivestis = datetime.date.today()
data_dabar = datetime.date.today()
skirtumas = (datetime.date.today() - ivestis)
dienu_tikrinimas = [
    'monday', 'Monday', 'tuesday', 'Tuesday', 'wednesday', 'Wednesday', 'thursday',
    'Thursday', 'friday', 'Friday', 'saturday', 'Saturday', 'sunday', 'Sunday']  # Ideti lietuviskas dienas
dienos_ivestis = ''
splitas = [' ', '/', '-', '.', '_']  # sutvarkyti splita

kalendorius = Irasas(datetime.date.today, calendar.day_name)
while True:
    try:

        pasirinkimas = int(input(   # ideti kalbos parinkti (lt, en)
            f'''
        ========================== 
        1. Iveskite Data:
        2. Pasirinkti diena: 
        3. Surasti pasirinkta diena: 
        4. Rasti paskutine ivestos dienos data:
        5. Rezultatai:
        6. Trinti rezultatus:
        0. Iseiti is programos
        ==========================
        '''))

        if pasirinkimas == 0:
            break

        elif pasirinkimas == 1:
            try:
                ivestis = input('Praejusia data YYYY MM DD formatu: ')
                year, month, day = map(int, ivestis.split(' '))
                ivestis = datetime.date(year, month, day)
                skirtumas = (datetime.date.today() - ivestis)
                if ivestis > datetime.date.today():
                    print('Iveskite praejusia diena')
                else:
                    for x in range(skirtumas.days):
                        diena = data_dabar - datetime.timedelta(days=x)
                        kalendorius.get_diena(diena)
                print('\n===========\nDatos suvestos i rezultatus\n===========\n')
            except ValueError:
                print('\n===========\nNeteisingai ivesta data!\n===========\n')

        elif pasirinkimas == 2:
            try:
                dienos_ivestis = str(
                    input('Iveskite diena kuria norite rasti pvz(monday): '))
                if any(diena in dienos_ivestis for diena in dienu_tikrinimas):
                    kalendorius.get_pavadinimas(dienos_ivestis.capitalize())
                    print('\n===========\nDiena pasirinkta\n===========\n')
                else:
                    print('\n===========\nNeteisingai ivesta diena\n===========\n')

            except ValueError:
                print('\n===========\nNeteisinga Ivestis\n===========\n')

        elif pasirinkimas == 3:
            try:
                if ivestis == datetime.date.today():
                    print('\n===========\nNepakeista Data\n===========\n')
                else:
                    for x in range(skirtumas.days):
                        diena = data_dabar - datetime.timedelta(days=x)
                        kalendorius.get_sekmadienis(diena)
                    print('\n===========\nDienos suvestos i rezultatus!\n===========\n')

            except ValueError:
                print('\n===========\nNeivesta data!\n===========\n')

        elif pasirinkimas == 4:
            kalendorius.get_paskutine_diena()

        elif pasirinkimas == 5:
            try:
                kalendorius.get_parodyti_atsakyma()
            except ValueError:
                print('\n===========\nKlaida\n===========\n')

        elif pasirinkimas == 6:
            kalendorius.get_trinti()

        else:
            print('\n===========\nNeteisinga Ivestis!\n===========\n')
    except ValueError:
        print('\n===========\nNeteisinga Ivestis!\n===========\n')
