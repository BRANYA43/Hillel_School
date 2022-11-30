LENGTH_TRACK = 100
MAX_SPEED = 25
speed = 0
time = 0

message = ''


def get_distance(speed: int, time: int):
    distance = speed * time
    return distance


def get_position_on_track(distance: int, length_track: int):
    position = 0
    if distance > 0:
        if distance > length_track:
            position = distance - (distance // length_track * length_track)
        elif distance < length_track:
            position = distance

    elif distance < 0:
        if abs(distance) > length_track:
            position = distance - (distance // length_track * length_track)
        elif abs(distance) < length_track:
            position = length_track + distance

    return position


def get_input_number(message: str):
    ret = ''
    while not ret.isdigit():
        ret = input(message)

        try:
            if int(ret) < 0:
                break
        except ValueError:
            pass

    return int(ret)


speed = get_input_number('Введіть швидкість (км/год): ')
time = get_input_number('Введіть час (год): ')
distance = get_distance(speed, time)
position = get_position_on_track(distance, LENGTH_TRACK)

print('*' * 20)

if time == 0:
    print('Васілій за 0 год проїде рівно 0 км.')
elif time < 0:
    print("Не буває від'ємного часу.\n")

elif time > 0:
    if abs(speed) > MAX_SPEED:
        message += 'Васілій або приймає допінг, або його батьком був Флеш.\n'
        message += f'Його швидкість перевищує {MAX_SPEED}(км), нормальну швидкість людей на велосипеді.\n'

    if speed == 0:
        print(f'Васілій вирішив постояти {time} год.')
    elif speed > 0:
        message += 'Васілій їхав за годинниковою стрілкою.\n'
    elif speed < 0:
        message += 'Васілій їхав проти годинникової стрілки.\n'

    if message != '':
        message += f'Він проїхав {abs(distance)}(км) та зупинився на позначці {position}(км).'
        print(message)
