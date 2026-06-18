import colorama


banner = (r"""
      
'||  ||`             '||                    __   _____   '||                                     
 ||  ||   ''          ||                    \ \ / / __|   ||                                     
 ||''||   ||  .|''|,  ||''|, .|''|, '||''|   \ V /\__ \   ||     .|''|, '\\    //` .|''|, '||''| 
 ||  ||   ||  ||  ||  ||  || ||..||  ||       \_/ |___/   ||     ||  ||   \\/\//   ||..||  ||    
.||  ||. .||. `|..|| .||  || `|...  .||.                 .||...| `|..|'    \/\/    `|...  .||.
                  ||                                                                  
               `..|'                                                                  
      """)
vs_tag = (r"""
   __   _____ 
   \ \ / / __| 
    \ V /\__ \  
     \_/ |___/ (O)
                        
""")
def rainbow_print(logo):
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
    GRADIENT = 7

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
