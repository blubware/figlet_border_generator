import pyfiglet, sys
from clear_screen import clear

def figlet_border_generator():
    try:
        clear()
        font = str(input('Font: '))
        text = str(input('Text: '))

        def border(string):
            try:
                ascii_text = pyfiglet.figlet_format(string, font=font)
            except:
                print('Invalid font')
                return None

            lines = ascii_text.split("\n")
            max_len = max(len(line) for line in lines)
            border = "╔" + "═" * (max_len + 2) + "╗\n"
            
            for line in lines:
                border += "║ " + line.ljust(max_len) + " ║\n"

            border += "╚" + "═" * (max_len + 2) + "╝"
            return border
            

        print(border(text))

        input('Press enter to return to main menu')
        figlet_border_generator()
    
    except KeyboardInterrupt:
        clear()
        sys.exit()

if __name__ == '__main__':
    figlet_border_generator()