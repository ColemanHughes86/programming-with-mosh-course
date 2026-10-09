car_started = False
game_active = True

while game_active:
    command = input('>')
    if command.lower() == 'help':
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif command.lower() == 'start' and not car_started:
        car_started = True
        print('Car started...Ready to go!')
    elif command.lower() == 'start' and car_started:
        print('Car has already been started.')
    elif command.lower() == 'stop' and car_started:
        car_started = False
        print('Car stopped.')
    elif command.lower() == 'stop' and not car_started:
        print('Car is already stopped.')
    elif command.lower() == 'quit':
        game_active = False
    else:
        print('I dont understand that.')