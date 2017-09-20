import os
import glob

def changeName(dirname):
    os.chdir(full_path)
    number = 1
    for filename in glob.glob("*.jpg"):
        changedName = "sushi_{0:0>3}.jpg".format(number)
        number += 1
        os.rename(filename, changedName)
    print("변경완료")

sub_directory = input("하위파일의 이름 변경을 원하는 파일 디렉터리를 입력하시오: ")
full_path = "C:\\Users\\350U2A\\Desktop\\소프트웨어 종합설계\\자료사진\\" + str(sub_directory)
changeName(full_path)