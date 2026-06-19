import colorama

banner = r"""
      ______________________
     |  __________________  |
     | |                  | |
     | |   COFFEE  v7.7   | |                                             
     | |__________________| |                               /')    /')        
     |                      |          ____     ____      /' /'  /' /' ____   
     |   [ Espresso  ]  >o  |        /'    )--/'    )---/'--' -/'--' /'    )  
     |   [ Cappuccino]  >o  |       /'       /'    /'  /'     /'    /(___,/' 
     |   [ Latte     ]  >o  |      (___,/   (___,/'  /(_____/(_____(________  
     |                      |                     /'     /' 
     |      .--------.      |                   /'     /' 
     |      |  ____  |      |                 /'     /' 
     |      | |____| |      |        /'                                    /'  _/     /
     |      |        |      |       /'                                    /' _/~     /
     |______|________|______|      /'__      ____     ____     ____     ,/'_/~      /
       /___/ ::  ~^~  \___\       /'    )   )'    )--/'    )  /'    )   /\/~       /
             :: ~^^~             /'    /'  /'       /(___,/' /'    /'  /'  \      /
             ::_|||__           (___,/(__/'        (________(___,/(__/'     \    o
            \        /
             |  @@  |
             |______|
                 
"""

espresso = r"""
          ) (
         ( ) )
        .-----.
        | @@@ |]
        '-----'  ESPRESSO..
"""

latte = r"""
          .-.
       .-(   )-.
     _(___.__)__)_
     \ ^---^---^ /
      (~~~~~~~~~)
      |XXXXXXXXX|
      (~~~~~~~~~)
       \_______/        LATTE..
"""

cappuccino = r"""
            )  (
           (   ) )
            ) ( (
       __________)_
    .-'------------|
   ( C|/\/\/\/\/\/\|
    '-./\/\/\/\/\/\|
      '____________'
       '----------'     CAPPUCCINO..
"""
money_back = r"""
                                   __-----__
      .._______               ..;;;--'~~~`--;;;..
       \_______\            /;-~IN GOD WE TRUST~-.\
        \_______\_         //      ,;;;;;;;;      \\
 ________\________\      .//      ;;;;;    \       \\
>  -----  vv \___\ \     ||       ;;;;(   /.|       ||
>- DOLLARS vv \   \ \    ||       ;;;;;;;   _\      ||
>^^ BACK!! ^^^/___/ /    ||       ';;  ;;;;=        ||
>________^^^_/___/ /     ||LIBERTY | ''\;;;;;;      ||
          /_______/       \\     ,| '\  '|><| 1993 //
         /______/          \\   |     |      \  A //
        /______/            `;.,|.    |      '\.-'/
                              ~~;;;,._|___.,-;;;~'
                                  ''=------=''    
"""

def rainbow_print(logo,gradient=21):
    colorama.init()

    RAINBOW = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
    ]

    RESET = "\033[0m"
    GRADIENT = gradient

    for i, line in enumerate(logo.splitlines()):
        for j, char in enumerate(line):
            color = RAINBOW[(i + j // GRADIENT) % len(RAINBOW)]
            print(color + char, end="")
        print()

    print(RESET)
    
def print_green_text(text):
    colorama.init()
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(GREEN + text + RESET)
    
def print_red_text(text):
    colorama.init()
    RED = "\033[91m"
    RESET = "\033[0m"
    print(RED + text + RESET)
    
def print_blue_text(text):
    colorama.init()
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print(BLUE + text + RESET)