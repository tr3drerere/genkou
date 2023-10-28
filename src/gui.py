
import cla_genkou
import os
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
    i_dir = entry1.get()
    i_ext = ext.get()
    i_nob = nob.get()
    i_size = size.get()
    i_addm = addm.get()
    i_cmode = cmode.get()
    i_samp = samp.get()

    main_proc = cla_genkou.inputData(i_dir, i_ext, i_nob, i_size, i_addm, i_cmode, i_samp)
    res = main_proc.convert()
    if not res == 0 :
        messagebox.showerror("ERROR", res)
    else:
        now = main_proc.getNow()
        dir_name = r"convert_" + str(now)
        dir_path = str(os.path.dirname(__file__)) + "\\" + dir_name
        messagebox.showinfo("処理完了", "処理が完了しました。\r\nfolder:" + dir_name)
        os.system('explorer.exe "%s"' % dir_path)

# 参照ボタンのアクション
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
main_win.geometry("800x370")

font = tkinter.font.Font(main_win, size=12)
main_win.option_add("*Radiobutton.Font", font)
main_win.option_add("*font", font)
main_win.option_add("*Botton.Font", font)


# 初期化
ext = tk.StringVar()
nob = tk.IntVar()
size = tk.StringVar()
addm = tk.IntVar()
cmode = tk.StringVar()
samp = tk.BooleanVar()
ext.set("tiff")
nob.set(1)
size.set("A5")
addm.set(3)
cmode.set("gray")
samp.set(False)


# フレーム配置
fr_ext = tk.Frame(main_win, width=160, height=100, relief="flat")
fr_nob = tk.Frame(main_win, width=160, height=100, relief="flat")
fr_samp = tk.Frame(main_win, width=300, height=100, relief="flat")
fr_size = tk.Frame(main_win, width=140, height=80, relief="flat")
fr_addm = tk.Frame(main_win, width=140, height=80, relief="flat")
fr_cmode = tk.Frame(main_win, width=160, height=80, relief="flat")
fr_cmt = tk.Frame(main_win, width=300, height=80, relief="flat")

fr_ext.place(x=40, y=140)
fr_nob.place(x=200, y=140)
fr_samp.place(x=570, y=140)
fr_size.place(x=40, y=270)
fr_addm.place(x=200, y=270)
fr_cmode.place(x=340, y=270)
fr_cmt.place(x=570, y=270)

# 変換元フォルダ
entry1 = tk.StringVar()
direty = tk.Entry(main_win, textvariable=entry1)
filebtn = tk.Button(main_win, text="参照", command=dirdialog_clicked)

# 変換元フォルダ_ラベル
lbl_dir = ttk.Label(main_win, text="◆変換元フォルダ", padding=(5, 2))
# 注意書き_ラベル
lbl_atnd1 = ttk.Label(main_win, text="対応拡張子：bmp, png, tiff　解像度：600dpiのみ", padding=(5, 2), font=("normal", 10))
lbl_atnd2 = ttk.Label(main_win, text="※変換後はツールの場所にconvert_日付フォルダが作成されます。", padding=(5, 2), font=("normal", 10))

# 変換元フォルダ_レイアウト
lbl_dir.place(x=40, y=25)
filebtn.place(x=65, y=55, width=100, height=30)
direty.place(x=170, y=55, width=600, height=30)
lbl_atnd1.place(x=170, y=85)
lbl_atnd2.place(x=170, y=105)


# 変換後拡張子
ext1 = tk.Radiobutton(fr_ext, value="tiff", variable=ext, text="TIFF")
ext2 = tk.Radiobutton(fr_ext, value="png", variable=ext, text="PNG")

# 変換後拡張子_ラベル
lbl_ext = ttk.Label(fr_ext, text="◆変換後拡張子", padding=(5, 2))

# 変換後拡張子_レイアウト
lbl_ext.pack(side = tk.TOP, anchor = tk.W)
ext1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
ext2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# ノンブル始まり
nob1 = tk.Radiobutton(fr_nob, value=1, variable=nob, text="1")
nob2 = tk.Radiobutton(fr_nob, value=3, variable=nob, text="3")
nob3 = tk.Radiobutton(fr_nob, value=99, variable=nob, text="ノンブルなし")

# ノンブル始まり
lbl_nob = ttk.Label(fr_nob, text="◆ノンブル始まり", padding=(5, 2))

# ノンブル始まり_レイアウト
lbl_nob.pack(side = tk.TOP, anchor = tk.W)
nob1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
nob2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
nob3.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# 仕上がりサイズ
size1 = tk.Radiobutton(fr_size, value="A5", variable=size, text="A5")
size2 = tk.Radiobutton(fr_size, value="B5", variable=size, text="B5")

# 仕上がりサイズ_ラベル
lbl_size = ttk.Label(fr_size, text="◆仕上がりサイズ", padding=(5, 2))

# 仕上がりサイズ_レイアウト
lbl_size.pack(side = tk.TOP, anchor = tk.W)
size1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
size2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))

# 塗り足し
add1 = tk.Radiobutton(fr_addm, value=3, variable=addm, text="3mm")
add2 = tk.Radiobutton(fr_addm, value=5, variable=addm, text="5mm")

# 塗り足し_ラベル
lbl_add = ttk.Label(fr_addm, text="◆塗り足し", padding=(5, 2))

# 塗り足し_レイアウト
lbl_add.pack(side = tk.TOP, anchor = tk.W)
add1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
add2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))


# カラーモード
cmode1 = tk.Radiobutton(fr_cmode, value="gray", variable=cmode, text="グレースケール")
cmode2 = tk.Radiobutton(fr_cmode, value="mono", variable=cmode, text="モノクロ")

# カラーモード_ラベル
lbl_cmode = ttk.Label(fr_cmode, text="◆カラーモード", padding=(5, 2))

# カラーモード_レイアウト
lbl_cmode.pack(side = tk.TOP, anchor = tk.W)
cmode1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
cmode2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))

# サンプルモード
samp1 = tk.Radiobutton(fr_samp, value=True, variable=samp, text="オン")
samp2 = tk.Radiobutton(fr_samp, value=False, variable=samp, text="オフ")

# サンプルモード_ラベル
lbl_samp = ttk.Label(fr_samp, text="◆サンプルモード", padding=(5, 2))
lbl_samp_at = ttk.Label(fr_samp, text=" ※WEB掲載に20%縮小JPGに変換します。", padding=(5, 2), font=("normal", 8))

# サンプルモード_レイアウト
lbl_samp.pack(side = tk.TOP, anchor = tk.W)
samp1.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
samp2.pack(side = tk.TOP, anchor = tk.W, padx=(20,0))
lbl_samp_at.pack(side = tk.TOP, anchor = tk.W)

# 実行ボタン
cmtbtn = tk.Button(fr_cmt, text="実行", command=commit)

# 実行ボタン_レイアウト
cmtbtn.place(x=0, y=35, width=200, height=40)



main_win.mainloop() 
