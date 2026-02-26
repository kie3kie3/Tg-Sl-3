import threading
import handler
import loop


def main():
    thHandler = threading.Thread(target=handler.main)
    thLoop = threading.Thread(target=loop.main)
    thHandler.start()
    thLoop.start()
    print('Запуск')


main()