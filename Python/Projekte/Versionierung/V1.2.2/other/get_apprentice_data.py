import datetime

class Get_Apprentice_Data:
    
    def calc_lehrjahr(self,  eintrittsdatum):
        eintritt_jahr = str(eintrittsdatum)[:4]
        eintritt_monat = str(eintrittsdatum)[5:7]
        eintritt_tag = str(eintrittsdatum)[8:10]
        dt_now = str(datetime.datetime.now())
        dt_jahr = dt_now[:4]
        dt_monat = dt_now[5:7]
        dt_tag = dt_now[8:10]
        LJ = int(dt_jahr) - int(eintritt_jahr)
        if int(eintritt_monat) < int(dt_monat):
            LJ += 1
        elif int(eintritt_monat) == int(dt_monat) and int(eintritt_tag) <= int(dt_tag):
            LJ += 1
        return LJ
