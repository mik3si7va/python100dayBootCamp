letters = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

print(r"""

  ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗
 ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
 ██║     ███████║█████╗  ███████╗███████║██████╔╝
 ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
 ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

           ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
          ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
          ██║     ██║██████╔╝███████║█████╗  ██████╔╝
          ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
          ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
           ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                        "Veni. Vidi. Encrypti.."

""")

def encrypt(text, shift, upper):
    text = str(text).upper()
    result = ''
    for letter in text:
        if letter not in letters:
            result += letter
            continue
        index = letters.index(letter)
        index += shift
        while index >= len(letter):
            index = index - len(letters)
        result += letters[index]
        
    if not bool(upper):
        result = result.lower()
    
    return result

def decrypt(text, shift, upper):
    text = str(text).upper()
    result = ''
    for letter in text:
        if letter not in letters:
            result += letter
            continue
        index = letters.index(letter)
        index -= shift
        while index < -len(letters):
            index = index + len(letters)
        result += letters[index]
        
    if not bool(upper):
        result = result.lower()
    
    return result

while True:
    direction = input("type 'encode' for encrypt and 'decode' for decrypt ... ('esc' to exit):\n>>> ")

    if "encode" in direction.lower():
        text = input("what would u like to encode??\n>>> ")
        shift = int(input("Enter the shift number ..\n>>> "))
        upper = input("Would you like that in UPPERCASE?? (Y/N): ").upper()
        print(f"This is your encoded message:\n\n     {encrypt(text,shift,upper.upper() == 'Y' and True or False)}\n")
    elif  "decode" in direction.lower():
        text = input("what would u like to decode??\n>>> ")
        shift = int(input("Enter the shift number ..\n>>> "))
        upper = input("Would you like that in UPPERCASE?? (Y/N): ")
        print(f"This is your decoded message:\n\n     {decrypt(text,shift,upper.upper() == 'Y' and True or False)}\n")
    elif direction.lower() == 'esc':
        print("Be seeing U... 🫡")
        break
    else:
        print("wrong choice ... ceasar's coming to get YOU .. hihihi!")
