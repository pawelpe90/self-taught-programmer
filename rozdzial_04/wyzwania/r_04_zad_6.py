def squared(x):
    """ Pobiera liczę całkowitą i zwraca jej wartość pomnożoną przez 2.
    :param x: int.
    :return: x pomnożone przez 2.
    """
    return x ** 2


def print_string(string):
    """ Wyświetla przekazany łańcuch znaków.
    :param string: łańcuch.
    """
    print(string)

print_string("Testing: 1, 2, 3.")


def add_mult(a,b,c,x=100,z=1000):
    """ Zwraca sumę trzech parametrów, przy czym trzeci 
    jest mnożony przez dwa dodatkowe opcjonalne parametry.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return a + b + c * x * z


def convert(string):
    """ Konwertuje przekazany łańcuch na liczbę zmiennoprzecinkową.
    :param string: str.
    :return: liczba uzyskana w wyniku konwersji.
    """
    try:
        return float(string)
    except ValueError:
        print("Nie można skonwertować łańcucha na liczę zmiennoprzecinkową.")