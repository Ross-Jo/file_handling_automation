import os
import glob
import csv

def makeLabel(dirname, category):
    # 안의 모든 파일에 대하여 카테고리를 붙인 라벨 파일을 만들기
    full_path = os.getcwd() + "\\" + str(dirname)
    f = open(sub_directory+".csv", 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)

    for filename in glob.glob(full_path +"\\"+ "*.jpg"):
        short_name = os.path.split(filename)[-1]
        wr.writerow([short_name+" "+category])
        # []를 하지 않으면 한글자 한글자마다 콤마가 찍힘
        # 참고 : https://stackoverflow.com/questions/1816880/why-does-csvwriter-writerow-put-a-comma-after-each-character

    f.close()
    print("레이블 생성 완료")

sub_directory = input("레이블을 만들기 원하는 파일 디렉터리를 입력하시오: ")
category = input("결과값을 지정할 카테고리 번호를 입력하세요: ")
makeLabel(sub_directory, category)
