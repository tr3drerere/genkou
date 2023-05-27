
import cv2
import numpy as np
import os, glob
from PIL import Image
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font

#----------------------------------------------------------------
# 関数設計
#----------------------------------------------------------------

# 実行処理
def commit():
    print("test")


# フォルダ選択
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

#----------------------------------------------------------------
# GUI設計
#----------------------------------------------------------------

#画面全体
main_win = tk.Tk()
main_win.title("原稿変換ツール")
main_win.geometry("800x340")

font = tkinter.font.Font(main_win, size=12)
main_win.option_add("*Radiobutton.Font", font)
main_win.option_add("*font", font)
main_win.option_add("*Botton.Font", font)


# 初期化
ext = tk.BooleanVar()
nob = tk.BooleanVar()
size = tk.BooleanVar()
addm = tk.BooleanVar()
cmode = tk.BooleanVar()
ext.set(False)
nob.set(False)
size.set(False)
addm.set(False)
cmode.set(False)

# フレーム配置
fr_ext = tk.Frame(main_win, width=160, height=80, relief="flat")
fr_nob = tk.Frame(main_win, width=160, height=80, relief="flat")
fr_size = tk.Frame(main_win, width=140, height=80, relief="flat")
fr_addm = tk.Frame(main_win, width=140, height=80, relief="flat")
fr_cmode = tk.Frame(main_win, width=160, height=80, relief="flat")
fr_cmt = tk.Frame(main_win, width=330, height=80, relief="flat")

fr_ext.place(x=40, y=140)
fr_nob.place(x=200, y=140)
fr_size.place(x=40, y=230)
fr_addm.place(x=200, y=230)
fr_cmode.place(x=340, y=230)
fr_cmt.place(x=500, y=230)

# 変換元フォルダ
entry1 = tk.StringVar()
direty = tk.Entry(main_win, textvariable=entry1)
filebtn = tk.Button(main_win, text="参照", command=dirdialog_clicked)

# 変換元フォルダ_ラベル
lbl_dir = ttk.Label(main_win, text="◆変換元フォルダ", padding=(5, 2))
# 注意書き_ラベル
lbl_atnd1 = ttk.Label(main_win, text="対応拡張子：bmp, png, tiff", padding=(5, 2), font=("normal", 10))
lbl_atnd2 = ttk.Label(main_win, text="※変換後はツールの場所にconvert_日付フォルダが作成されます。", padding=(5, 2), font=("normal", 10))

# 変換元フォルダ_レイアウト
lbl_dir.place(x=40, y=25)
filebtn.place(x=65, y=55, width=100, height=30)
direty.place(x=170, y=55, width=600, height=30)
lbl_atnd1.place(x=170, y=85)
lbl_atnd2.place(x=170, y=105)


# 変換後拡張子
ext1 = tk.Radiobutton(fr_ext, value=0, variable=ext, text='TIFF')
ext2 = tk.Radiobutton(fr_ext, value=1, variable=ext, text='PNG')

# 変換後拡張子_ラベル
lbl_ext = ttk.Label(fr_ext, text="◆変換後拡張子", padding=(5, 2))

# 変換後拡張子_レイアウト
lbl_ext.pack(side = tk.TOP, anchor = tk.W)
ext1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
ext2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# ノンブル始まり
nob1 = tk.Radiobutton(fr_nob, value=0, variable=nob, text='1')
nob2 = tk.Radiobutton(fr_nob, value=1, variable=nob, text='3')

# ノンブル始まり
lbl_nob = ttk.Label(fr_nob, text="◆ノンブル始まり", padding=(5, 2))

# ノンブル始まり_レイアウト
lbl_nob.pack(side = tk.TOP, anchor = tk.W)
nob1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
nob2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# 仕上がりサイズ
size1 = tk.Radiobutton(fr_size, value=0, variable=size, text='A5')
size2 = tk.Radiobutton(fr_size, value=1, variable=size, text='B5')

# 仕上がりサイズ_ラベル
lbl_size = ttk.Label(fr_size, text="◆仕上がりサイズ", padding=(5, 2))

# 仕上がりサイズ_レイアウト
lbl_size.pack(side = tk.TOP, anchor = tk.W)
size1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
size2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))

# 塗り足し
add1 = tk.Radiobutton(fr_addm, value=0, variable=addm, text='3mm')
add2 = tk.Radiobutton(fr_addm, value=1, variable=addm, text='5mm')

# 塗り足し_ラベル
lbl_add = ttk.Label(fr_addm, text="◆塗り足し", padding=(5, 2))

# 塗り足し_レイアウト
lbl_add.pack(side = tk.TOP, anchor = tk.W)
add1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
add2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# カラーモード
cmode1 = tk.Radiobutton(fr_cmode, value=0, variable=cmode, text='グレースケール')
cmode2 = tk.Radiobutton(fr_cmode, value=1, variable=cmode, text='モノクロ')

# カラーモード_ラベル
lbl_cmode = ttk.Label(fr_cmode, text="◆カラーモード", padding=(5, 2))

# カラーモード_レイアウト
lbl_cmode.pack(side = tk.TOP, anchor = tk.W)
cmode1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
cmode2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# 実行ボタン
cmtbtn = tk.Button(fr_cmt, text="実行", command=commit)

# 実行ボタン_レイアウト
cmtbtn.place(x=70, y=35, width=200, height=40)



main_win.mainloop() 

"""
#フレーム
frame1 = ttk.Frame(main_win)
frame1.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

#入力元
in_path_label = ttk.Label(frame1, text="PDF置き場")
in_path_box = ttk.Entry(frame1)
in_path_box.insert(tk.END, "")

#

#実行ボタン
app_btn = ttk.Button(frame1, text="実行", width=12, command=pdf_word)

# ウィジェットの配置
in_path_label.grid(column=0, row=0, pady=10)
in_path_box.grid(column=1, row=0, sticky=tk.EW, padx=5)
out_path_label.grid(column=0, row=1, pady=10)
out_path_box.grid(column=1, row=1, sticky=tk.EW, padx=5)
app_btn.grid(column=1, row=3, padx=10)

# 伸縮設定
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)

main_win.mainloop() 

"""

