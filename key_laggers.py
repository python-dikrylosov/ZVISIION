import pynput.keyboard
import pandas as pd
import time



def on_press(key):
    print("start"+ "" + format(key))
    try:
        # Здесь можно добавить код, который выполняется при каждом нажатии клавиши
        print('Key {} pressed.'.format(key.char))
        data = pd.read_csv('kl.csv', encoding='utf-8')
        print(data)
        data = pd.DataFrame({'Datetime': [time.strftime("%Y-%m-%d %H:%M:%S")],
                             'Timetime': [time.time()],
                             'press_key': [format(key)],
                             })
        data.to_csv('kl.csv', mode='a', header=False, index=False, encoding='utf-8')

    except AttributeError:
        # Данный блок выполнится, если нажата не символьная клавиша
        print('Key {} если нажата не символьная клавишаeeeg545'.format(key))

        data = pd.read_csv('ll.csv', encoding='utf-8')
        print(data)
        data = pd.DataFrame({'Datetime': [time.strftime("%Y-%m-%d %H:%M:%S")],
                             'Timetime': [time.time()],
                             'press_key': [format(key)],
                             })
        data.to_csv('ll.csv', mode='a', header=False, index=False, encoding='utf-8')


def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Прерываем выполнение программы при нажатии клавиши Esc
        return False

# Создаем объекты для мониторинга клавиатуры
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:

    listener.join()
