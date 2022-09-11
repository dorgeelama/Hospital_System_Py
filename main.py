#keep iterating until the given input is valid
def input_valid_int(msg, start =0, end = None):
    while True:
        inp  = input(msg)
        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
            else:
                return int(inp)
        else:
            return int(inp)

class FrontendManager:
    def __init__(self):
        pass
    
    def print_menu(self):
        print('\nProgram Options: ')
        messages = [
            '1) Add new patient',
            '2) Print all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}):'
        return input_valid_int(msg, 1, len(messages))


if __name__ == '__main__':
    app = FrontendManager()
    app.print_menu()
