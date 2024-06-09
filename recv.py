# import subprocess as sp
# import os
# os.add_dll_directory('C:/gstreamer/1.0/msvc_x86_64/bin')
# import cv2

# sp.Popen("ffplay -rtsp_flags listen rtsp://127.0.0.1:5000/test")

import cv2
import numpy as np
import socket

# UDPソケットの作成
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# バインドするIPアドレスとポート番号を指定
host = '127.0.0.1'
port = 5000
udp_socket.bind((host, port))

# 受信して表示
while True:
    # UDPパケットの受信
    data, _ = udp_socket.recvfrom(65507)

    # 受信したデータをNumpy配列に変換
    nparr = np.frombuffer(data, np.uint8)

    # フレームをデコード
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # デコードされた画像のサイズを取得
    if frame is not None:
        height, width, _ = frame.shape
        print("Received frame size: {}x{}".format(width, height))

        # ビデオフレームを表示
        cv2.imshow('Received Video', frame)

    else:
        print("Failed to decode frame")

    # キー入力の待機
    key = cv2.waitKey(1) & 0xFF

    # 'q'キーが押されたらループを抜ける
    if key == ord('q'):
        break

# ウィンドウを閉じる
cv2.destroyAllWindows()

# UDPソケットを閉じる
udp_socket.close()