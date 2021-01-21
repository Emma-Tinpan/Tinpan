import tkinter as tk

# ウィンドウの作成
window = tk.Tk()

#　描画のキャンパス作成
#　キャンバスは図形を描画するために必要
cv = tk.Canvas(window, width = 400, height = 300)
#　ウィンドウにキャンパスを配置する
cv.pack()

#　グリット表示
for i in range(20):
    # 横線用の変数
    x = i * 20
    # 縦線
    y = i * 20

    # create_line(x1, y1, x2, y2, ....)
    # x1, y1からx2, y2まで線を引く
    cv.create_line(x, 0, x ,400, fill="black", width=2)
    cv.create_line(0, y, 400 ,y, fill="black", width=2)

# 縁を描く
cv.create_oval(
    100, 100, 200, 200, fill="blue", outline = "green", width = 5
    )

# メインループを実行
window.mainloop()