def bottles_of_beer(bob):
    """ Wyświetla słowa piosenki 
        99 butelek piwa na ścianie.
        :param bob: Musi być liczbą
        dodatnią.
    """
    if bob < 1:
        print("""Nie ma już butelek
                 piwa na ścianie. 
                 Nie ma już butelek piwa.""")
        return
    tmp = bob
    bob -= 1
    print("""{} butelek piwa na ścianie. 
             {} butelek piwa. Jedną weź
             i przekaż w koło, {} butelek
             piwa na ścianie.
          """.format(tmp, 
                     tmp, 
                     bob))
    bottles_of_beer(bob)


bottles_of_beer(99)