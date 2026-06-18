import random


names = [
    "JoHaN",
    "MiKeL",
    "AlExI",
    "DaMiEn",
    "LuCaS",
    "RaFaEl",
    "NiKoL",
    "ViNcE",
    "MaRcO",
    "ZeNoN",
    "XaNtE",
    "KyRoN",
    "AeRoN",
    "VaLeN",
    "ZePhYr",
    "OrIoN",
    "DrAkE",
    "CaSpEr",
    "LySaNdEr",
    "NoVaK"
]

def rand_name():
    return random.choice(names)

def format (f_name, l_name):
    """
    Take a first and last names and tittlelize it...\n
    and then concatenate them ..
    """
    if f_name == '' or l_name == '':
        return "U didn't provide one or more names..."
    f_name = str(f_name).title()
    l_name = str(l_name).title()
    return f_name + ' ' + l_name

print(format("MIkE","SilVA"))

print(format(rand_name(),rand_name()))

print(format(input("what's ur first Name?? "),input("what's ur last Name?? ")))