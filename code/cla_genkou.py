import cv2
import numpy as np
import os, glob
from PIL import Image
import datetime


class inputData:
    def __init__(self, b_folder, ext, nob, size, addm, cmode, samp):
        self.__b_folder = b_folder
        self.__ext = ext
        self.__nob = nob
        self.__size = size
        self.__addm = addm
        self.__cmode = cmode
        self.__samp = samp
        self.__now = datetime.datetime.now().strftime("%Y%m%d")
        self.__width = 0
        self.__height = 0

    def getNow(self):
        now = self.__now
        return now

    def getFiles(self):
        #　変換元フォルダに指定したパスからリストを作成する
        path=self.__b_folder
        files = os.listdir(path)
        filelist = [f for f in files if os.path.isfile(os.path.join(path, f))]
        return filelist
    
    
    def getTrimSize(self):    
        #　塗り足しのピクセル変換
        if self.__addm == 3:
            self.__addm = 71
        elif self.__addm == 5:
            self.__addm = 118

        #　トリミングサイズを設定する
        if self.__size == "A5":
            self.__width = 3496 + int(self.__addm)
            self.__height = 4961 + int(self.__addm)

        elif self.__size == "B5":
            self.__width = 4299 + int(self.__addm)
            self.__height = 6071 + int(self.__addm)            

        return self.__width, self.__height


    def trim_center(self, img):
        #　指定サイズ取得
        width, height = self.getTrimSize()

        #　中央寄せのトリミング
        h, w = img.shape[:2]
        top = int((h / 2) - (height / 2))
        bottom = top + height
        left = int((w / 2) - (width / 2))
        right = left + width
        dst = img[top:bottom, left:right]

        return dst
    
    def getNobPos(self,pageNo):
        #　ノンブルの位置を設定する
        if self.__size == "A5":
            posW = self.__addm + 118
            posH = self.__height - 710
        elif self.__size == "B5":
            posW = self.__addm + 118
            posH = self.__height - 874

        #  ファイルのページ番号が奇数か偶数かで位置を変更
        if pageNo % 2 == 0:
                posW = self.__width - posW

        return posW, posH



    def convert(self):
        try:
            # ファイルリスト取得
            filelist = self.getFiles()
            # error_check
            if len(filelist) == 0:
                raise TypeError("指定フォルダにファイルがありません")
            
            # ファイル一覧の順にファイルを開き、処理を行う
            for i in range( 0, len(filelist)) :


                # Pillowで画像ファイルを開く
                path = self.__b_folder
                pil_img = Image.open(path + "\\" + filelist[i])
                # PillowからNumPyへ変換
                img = np.array(pil_img)
                
                # トリミング処理
                dst = self.trim_center(img)

                #　カラーモード変換
                gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
                
                #　モノクロ変換の場合
                if self.__cmode == "mono":
                    ret,th_img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
                    gray = th_img
                
                ###ノンブル入力
                # ノンブル位置取得
                if not self.__nob == 99:
                    posW,posH = self.getNobPos(i)

                    #  座標の色によって、文字の色を変更し入力
                    pil_image = Image.fromarray(gray)
                    color = pil_image.getpixel((posW, posH))
                    if color > 125:
                        cv2.putText(gray, str(i + self.__nob), (posW, posH), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 0), 1, cv2.LINE_AA)
                    else:
                        cv2.putText(gray, str(i + self.__nob), (posW, posH), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 1, cv2.LINE_AA)    

                #  変換後のフォルダ名成形
                dirname = "convert_" + self.__now
                if not os.path.exists(dirname):
                    os.makedirs(dirname)

                #  ファイル保存
                #  サンプルモードの場合
                if self.__samp == True:
                    filename = filelist[i].split(".")[0] + ".jpg"
                    dst = cv2.resize(gray, None, None, 0.2, 0.2)
                    cv2.imwrite(dirname + "\\" + filename, dst)

                #  通常モードの場合
                else:
                    #選択した拡張子で保存                    
                    filename = filelist[i].split(".")[0] + "." + self.__ext
                    cv2.imwrite(dirname + "\\" + filename, gray)
            return 0
                        
        except Image.UnidentifiedImageError:
            msg = "画像ファイル以外のファイルが含まれています。"
            return msg
        
        except IndexError:
            msg = "画像サイズが不正です。"
            return msg
        
        except FileNotFoundError as e:
            return e
        