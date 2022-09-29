import ctypes
from pystyle import *
import random
import string
char = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
number = 0
Result = ''
ctypes.windll.kernel32.SetConsoleTitleW('BNITROGEN | Made by https://github.com/TheCuteOwl Code Generated : 0')
print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter(
    '''
██████╗ ███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗
██╔══██╗████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
██████╔╝██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
██╔══██╗██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║
╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝''')))

print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter('You will need checker to check the code')))
gen = input(Colorate.Horizontal(Colors.blue_to_green, 'How many code do you want to gen ? : '))
with open('result.txt', 'w') as f:
    for i in range(int(gen)):
        Result += f'https://discord.gift/{"".join(random.choices(char, k=16))}\n'
        number += 1
        ctypes.windll.kernel32.SetConsoleTitleW('BNITROGEN | '
                                                'Made by https://github.com/TheCuteOwl Code Generated : ' + str(number))
        print(Colorate.Horizontal(Colors.blue_to_green, "[Gen] | " + Result))
        f.write(f'{Result}')
        Result = ''
print(5 * '\n')
input(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter('Succesfully Generated, Saved into result.txt file,'
                                                             ' Press enter to close')))
