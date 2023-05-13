
import cv2
import numpy as np
import os, glob
from PIL import Image
import datetime

def trim_center(img, width, height):
    h, w = img.shape[:2]
    
    top = int((h / 2) - (height / 2))
    bottom = top+height
    left = int((w / 2) - (width / 2))
    right = left+width
    
    return img[top:bottom, left:right]

if __name__ == '__main__':

    # setting
    path = r'C:\Users\reona takeda\Python\03_開発\03_原稿支援\manga'
    width = 3638
    height = 5102
    now = datetime.datetime.now().strftime('%Y%m%d')

    # ディレクトリからファイル一覧を取得
    files = os.listdir(path)
    filelist = [f for f in files if os.path.isfile(os.path.join(path, f))]
    dig = len(filelist[0])

    # ファイル一覧の順にファイルを開き、処理を行う
    for i in range( 0, len(filelist)) :
        # Pillowで画像ファイルを開く
        pil_img = Image.open(path + '\\' + filelist[i])
        # PillowからNumPyへ変換
        img = np.array(pil_img)

        #　指定サイズへトリミング
        dst = trim_center(img, width, height)
        #　カラーモード変換
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        #　ノンブル入力
        posW = 120
        posH = height - 470

        #  ファイルのページ番号が奇数か偶数かで位置を変更
        if i % 2 == 0:
            posW = width - 120
        cv2.putText(gray, str(i+1), (posW, posH), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        #  ファイル名成形
        dirname = 'convert_' + now
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = filelist[i].split(".")[0] + '.tiff'

        #tiffで保存
        cv2.imwrite(dirname + '\\' + filename, gray)
