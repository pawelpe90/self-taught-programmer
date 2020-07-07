import re

text = """Żyrafy od samego momentu odkrycia 
    stanowią __RZECZOWNIK_LPOJ__ świata zwierząt.
    Są one najwyższymi ze wszystkich żyjących
    na świecie __RZECZOWNIK_LMNOGA__, jednak
    naukowcy nie są w stanie wyjaśnić, w jaki
    sposób ich __CZESC_CIAŁA__ stała się tak 
    długa. Żyrafy zawdzięczają swoją niesamowitą
    wysokość, która może dochodzić do 
    __LICZBA__ __RZECZOWNIK_LMNOGA__, swoim 
    nogom i __CZESC_CIAŁA__.
    """

def mad_libs(mls):
    """
    :param mls: Łańcuch znaków, 
    zawierający części otoczone podwójmymi 
    znakmi podkreślenia, które użytkownik
    powinien zastąpić samodzielnie wybranymi
    słowami. W sugestiach nie można 
    umieszczać znaków podkreślenia; np:
    nie __to_sugestia__, tylko 
    __sugestia__.
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Wpisz {}:"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Nieprawidłowy parametr mls")

mad_libs(text)
