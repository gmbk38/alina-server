import update

update.update('badWords', 'Запрещённые слова', 1, 2)

while True:
    a = input()
    if a:
        print(update.badWords)