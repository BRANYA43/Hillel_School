"""У додатку є json файл. Написати програму, яка прочитає його та порахує загальну тривалість всіх треків в альбомі.
  Базовий кейс - поверне кількість секунд.
  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39"""
import json
import time

with open('acdc.json', 'r') as f:
    file = json.load(f)
    sum_duration = sum(int(track['duration']) for track in file['album']['tracks']['track'])
    print(time.strftime('%H:%M:%S', time.gmtime(sum_duration)))
