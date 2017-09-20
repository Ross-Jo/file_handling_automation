import os
import shutil

def changeName(dirname):
    os.chdir(dirname)

    check_dirname = input("생성을 원하는 디렉터리 이름을 입력하시오: ")

    if not os.path.isdir(check_dirname):
        os.mkdir(check_dirname)

    number = 1
    for path, dir, files in os.walk(dirname):
        if((not path==dirname+"\\"+check_dirname) and (files)): #새로 생성한 디렉터리가 아니어야 하며, files가 비어있지 않아야 한다.
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.jpg': # jpg 파일만 변경토록 한다.
                    changedName = "sushi_{0:0>3}.jpg".format(number)
                    number += 1
                    os.rename(os.path.join(path, filename), changedName) # 여기 함수 사용에 특히 유의할 것. 바꾸려는 것이 무엇인지 명시해줘야 한다.
                    shutil.move(changedName, dirname+"\\"+check_dirname)
    print("변경완료")

full_path = "C:\\Users\\350U2A\\Downloads\\스테이지"
changeName(full_path)
