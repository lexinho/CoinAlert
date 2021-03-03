# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import websocket
from playsound import playsound
import json
import winsound

try:
    import thread
except ImportError:
    import _thread as thread


frequency = 1000  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second


def on_message(ws, message):
    data = json.loads(message)
    print("BTCUSDT price is " + data['p'])
    price = int(float(data['p']))
    if price > 50890:
        playsound('t-rex-roar.mp3')
        # winsound.Beep(frequency, duration)



def on_error(ws, error):
    print(error)


def on_open(ws):
    def run(*args):
        print("Connecting to binance stream...")
    thread.start_new_thread(run, ())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@trade",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error)

    ws.run_forever()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
