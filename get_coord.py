from pynput.mouse import Listener

# クリックイベントを取得する関数
def on_click(x, y, button, pressed):
    if pressed:
        print(f"クリックされた座標: ({x}, {y})")

# リスナーを開始
with Listener(on_click=on_click) as listener:
    listener.join()