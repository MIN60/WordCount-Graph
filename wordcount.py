#wordcount.py
#1914201 김민정

#파일을 읽어 단어들의 등장 횟수를 세고 빈도수 상위 11개의 단어를 그래프로 표현하는 프로그램


try:  #try-except 예외처리
    from graphics import *   #히스토그램 표현을 위해서 graphics라는 모듈 전체를 불러와 사용함
except (ImportError, ModuleNotFoundError):  #graphics모듈을 찾지 못하면
    print('그래프 표현을 위해 임포트할 모듈 graphics를 찾지 못했습니다. 프로그램을 종료합니다.')  #사용자에게 찾지 못했다고 알려주고 
    exit() #프로그램 강제 종료


def wordprogram():#함수 wordprogram 선언
    passed = 0   #파일을 찾을 수 없을 때 다시 파일명을 받기 위해 passed를 만듦
    while (passed==0): #passed가 0일때
        #passed는 0으로 선언해 두었기 때문에 오류가 나지 않으면 passed는 1로 바뀌어 더이상 루프를 돌지 않고, 오류가 나면 루프로 인해 다시 파일명을 입력받음.
        try: #예외처리 try-except
            charFile = input('파일명을 .txt 형식으로 입력하십시오 [ex)text1.txt]: ')  #파일 이름을 charFile에 저장함
            fileOpen = open(charFile, 'r')  #읽기모드로 charFile에 저장된 파일이름을 가진 파일을 열고 파일의 객체를 돌려줌
            char = fileOpen.read()     #파일 전체의 내용을 하나의 문자열로 읽어와 char에 저장함
            passed=1  # 파일이 제대로 입력되면 passed를 1로 바꾸어 더이상 루프를 돌지 않도록 함
        except FileNotFoundError:  #예외처리, 파일명을 찾을 수 없어 오류가 나면 에러 대신 
            print('파일을 찾을 수 없습니다. 다시 입력하세요.')  #파일을 찾을 수 없다고 알려줌


    try:  #예외처리 try-except
        char1 = char.lower() #파일 전체 내용이 문자열로 저장된 char에 있는 대문자를 소문자 변환하여 char1에 저장
        oldchars = ',!?.\'\"\n;:' #단어에서 떼어내야 할 문자 . , ! ? ' " \n ; : 을 묶어서 oldchars에 저장하고
        new = '         ' #없애야 할 단어의 개수만큼 공백을 new에 저장해둠
        char2 = char1.translate({ord(x): y for (x,y) in zip(oldchars, new)}) #char1파일에 있는 문자 . , ! ? ' " \n ; :를 공백으로 치환하고 char2에 저장
        
        #translate는 여러개의 문자를 변환 해주는데, translate의 인자값은 dictionary가 들어갑니다.
        #이때 dictionary의 키에는 변환시킬 문자의 유니코드 값이 들어가야하기 때문에 ord()를 사용합니다.
        #zip은 동일한 개수의 요소 값을 갖는 반복 가능한 자료형을 묶는 역할을 합니다.


        #단어 구분, 빈도수 계산
        wordgroup = {}  #키와 값을 한쌍으로 가지는 딕셔너리 wordgroup를 생성함
        
        for word in char2.split():  #없애야 할 단어들이 공백으로 바뀐 파일 char2를 공백기준으로 단어를 나눔
            if word in wordgroup:  #만약 wordgroup에 해당 단어가 이미 존재하면
                wordgroup[word] += 1  #단어의 빈도수 +1
            else:  #단어가 wordgroup에 없는 새로운 단어이면 
                wordgroup[word] = 1  #단어 빈도수 1로 설정

        wordgroup_list = list(wordgroup.keys()) #wordgroup의 키값, 즉 단어들의 모음을 wordgroup_list에 저장
        countword = len(wordgroup_list) #총 단어의 개수를 countword에 저장함
        keylist = list() #keylist라는 키(단어)들을 모아둘 리스트 생성
        valuelist = list()  #valuelist라는 값(빈도수)들을 모아둘 리스트 생성
        
        for k,v in sorted(wordgroup.items(), key=lambda x:x[1], reverse=True):  #단어들을 빈도수 내림차순으로 정렬함
            #x는 wordgroup.items에서 얻은 목록에 들어있는 항목을 의미하며, 이는 (key,value) 튜플형식인데 x[1]은 value를 의미하며 정렬하는 key를 value로 하라는 것을 의미합니다.
            keylist.append(k)  #keylist에 단어 저장
            valuelist.append(v)  #valuelist에 빈도수 저장



        #빈도수 내림차순으로(빈도수 같을 경우 무작위) IDLE창에 단어와 빈도수 출력
        print('빈도수 내림차순으로 정렬한 모든 단어(빈도수 같으면 무작위)'.center(50,'=')) #사용자에게 빈도수가 큰 순으로 단어들을 나열한다고 알려줌
        for i in range(countword): #총 단어 수 만큼 반복해서
            print(keylist[i],valuelist[i]) #단어와 빈도수를 함께 IDLE창에 출력


        #파일에 존재하는 총 단어 수를 IDLE창에 출력
        print('총 단어 수'.center(35,'=')) #사용자에게 총 단어수를 출력한다고 알려줌
        print(countword)   #총 단어수 IDLE창에 출력


        #모든 단어를 빈도수 내림차순으로 정렬했을 때 상위 11개 단어를 IDLE창에 출력
        print('단어 빈도수 상위 11개의 단어'.center(35,'='))  #사용자에게 단어 빈도수 상위 11개 단어를 출력한다고 알려줌
        for i in range(11):  #11번 반복
            print(keylist[i],valuelist[i])  #단어와 빈도수 출력

    except (ValueError, IndexError, ZeroDivisionError, AttributeError,IndexError, KeyError): #예외처리
        #데이터의 값이 잘못되어 ValueError가 발생하거나, 존재하지 않는 인덱스로 인해 IndexError가 발생하거나, 0으로 나누는 경우가 생겨 ZeroDivisionError가 발생하거나
        #속성오류로 AttributeError가 발생하거나 IndexError, KeyError가 발생하여 에러가 났을 경우에 
        pass #에러를 내지 않고 넘어감

         

   


    #그래프 그리기
    win = GraphWin('Word Count Program', 1100, 800) #창크기가 1100*800인 Word Count Program 생성
    win.setCoords(-1.8, -8.0, 12.0, 50.0)  #왼쪽 하단 끝은(-1.8, -8.0)이고 오른쪽 상단 끝은(12.0, 50.0)으로 새 가상 좌표계 생성
    win.setBackground("white")  #창의 배경 색을 하얀색으로 변경 
    title = Text(Point(5.5, 47), ' Word Count Program')  #그래프의 제목(title)인 Word Count Program을 좌표(5.5, 47)에 표현하고자 함
    title.setFill('green')   #title의 색상을 초록색으로 설정 
    title.draw(win)  #창에 title을 출력함

    subtitle = Text(Point(5.5, 45), '가장 많이 등장한 상위 11개의 단어 (빈도수가 같을 경우 무작위 배열)')  #그래프에 표현된 단어 설명을 좌표(5.5, 45)에 표현하고자 함
    subtitle.setFill('navy')   #subtitle의 색상을 네이비로 설정 
    subtitle.draw(win)  #subtitle을 출력함

    wordtitle = Text(Point(5.5, 43.5), '5글자 이상의 단어는 분홍색으로 4글자까지 표현되며 IDLE창에서 확인가능') #5글자 이상의 단어 표현법을 좌표(5.5, 43.5)에 표현하고자 함
    wordtitle.setFill('deep pink')   #wordtitle의 색상을 deep pink로 설정 
    wordtitle.draw(win)  #창에 wordtitle을 출력함
    

    #표가 들어갈 사각형을 그림
    downxline = Line(Point(0,0), Point(11,0)) #아래쪽 x축선을 좌표(0,0)부터 (11,0)까지  
    downxline.draw(win)  #창에 출력함
    leftyline = Line(Point(0,0), Point(0,40)) #왼쪽 y축선을 좌표 (0,0)부터 (0,40)까지
    leftyline.draw(win)  #창에 출력함
    upxline = Line(Point(0,40), Point(11,40))  #위쪽 x축선을 좌표 (0,40)부터 (11,40) 까지
    upxline.draw(win)    # 창에 출력함
    rightyline = Line(Point(11,0), Point(11,40)) # 오른쪽 y축선을 좌표 (11,0)부터 (11,40)까지
    rightyline.draw(win)  #창에 출력함


    #히스토그램에 표현된 총 단어 수 출력
    Text(Point(10, 44), '총 단어 수: ').draw(win)  #'총 단어 수'를 알려주고자 좌표(10, 44)에 문자 출력
    Text(Point(10.8, 44), countword).draw(win) #파일에서 검색된 총 단어 수(countword)를 좌표(10.8, 44)에 출력
    

    #y축은 빈도수를 표현한다는 것을 알려주기 위한 ylabel 표현
    ylabel1 = Text(Point(-1.1, 25), '빈')  #좌표 (-1.1, 25)에 '빈'
    ylabel1.setFill('green')  #문자를 초록색으로 설정 
    ylabel1.draw(win)  #'학'문자 창에 출력
    ylabel2 = Text(Point(-1.1, 20), '도')  #좌표 (-1.1, 20)에 '도' 
    ylabel2.setFill('green')  #문자를 초록색으로 설정
    ylabel2.draw(win)  #'생'문자를 창에 출력
    ylabel3 = Text(Point(-1.1, 15), '수')  #좌표 (-1.1, 15)에 '수'
    ylabel3.setFill('green')  #문자를 초록색으로 설정
    ylabel3.draw(win)  #'수'문자를 창에 출력
    

    #x축은 단어를 표현한다는 것을 알려주기 위한 xlabel 표현
    xlabel1 = Text(Point(4.5, -4.0), '단')  #좌표 (4.5, -4.0)에 '단'
    xlabel1.setFill('green') #문자를 초록색으로 설정
    xlabel1.draw(win)  #'점'문자 창에 출력
    xlabel2 = Text(Point(6.5, -4.0), '어')  #좌표 (6.5, -4.0)에 '어'
    xlabel2.setFill('green') #문자를 초록색으로 설정
    xlabel2.draw(win)  #'점'문자 창에 출력

    #빈

    #도

    #수
    
    #      단  어
    

    
    y = 0 # y축에 표현될 빈도수 단위를 0부터 표현하기 위해 y를 0으로 설정   
    for i in range(9):  #0~40 까지 5간격으로 표현하기 위해서 총 9번 반복
        Text(Point(-0.5,y), y).draw(win)  #x좌표 -0.5 고정으로 y좌표를 변경해가면서 창에 빈도수 단위표현을 함 
        y = y+5  #표현되는 y좌표는 5 간격.
        #0, 5, 10, 15, 20, 25, 30, 35, 40 단위가 표현되게 됨

        
    print('5글자 이상의 단어'.center(35,'=')) #IDLE창에 5글자 이상의 단어를 알려주려고 출력

    try:
        for x in range(11):  # x축에 빈도수 상위 11개 단어를 표현하기 위해서 총 11번 반복
            #5글자이상 단어 4글자까지만 표현
            if (len(keylist[x]) > 4):  #만약 단어의 길이가 4글자 초과이면
               cutword = keylist[x]   #해당 단어를 cutword에 저장하고
               cut = Text(Point(x+0.5, -1), cutword[:4])  #y좌표 -1 고정으로 x좌표를 변경해가면서 창에 4글자까지 자른 단어를 표현
               cut.setFill('deep pink')  #글씨색을 deep pink로 설정
               cut.draw(win)  #창에 출력함
               print(cutword) #5글자 이상의 단어를 IDLE창에 표현함
            else:
                Text(Point(x+0.5, -1), keylist[x]).draw(win)  #y좌표 -1 고정으로 x좌표를 변경해가면서 창에 단어를 표현
                
            
            if valuelist[x] <= 40:   #만약 어떠한 단어 x의 빈도수가 40이하일 경우
                bar = Rectangle(Point(x, 0), Point(x+1,valuelist[x]))  #해당하는 단어의 x좌표부터 폭이 1, 높이가 빈도수인 막대 그래프 bar
                bar.setFill('green')  #막대를 초록색으로 설정
                bar.draw(win)  #막대를 창에 출력함
                txt = Text(Point(x+0.5, valuelist[x]+1), valuelist[x]).draw(win)  #해당하는 단어의 빈도수가 몇인지 막대그래프 위에 표현함  
            if valuelist[x] > 40:   #만약 어떠한 단어 x의 빈도수가 40 초과일 경우
                bar = Rectangle(Point(x, 0), Point(x+1,40))  #해당하는 단어의 x좌표부터 폭이 1, 높이가 40인 막대 그래프 bar. 표가 그려지는 사각형 범위를 넘지 않도록 함
                bar.setFill('green')  #막대를 초록색으로 설정
                bar.draw(win)  #막대를 창에 출력함
                txt = Text(Point(x+0.5, 40+1), valuelist[x]).draw(win)  #해당하는 단어의 빈도수가 몇인지 막대그래프 위에 표현함
            #y축의 빈도수는 최대 40까지 표현되므로 만약 어떠한 단어의 빈도수가 40을 넘는다면 막대 그래프를 40까지만 그려 막대그래프가 사각형을 넘어서지 않도록 함
                
    except (ValueError, IndexError, ZeroDivisionError, AttributeError,IndexError, KeyError): #예외처리
        #데이터의 값이 잘못되어 ValueError가 발생하거나, 존재하지 않는 인덱스로 인해 IndexError가 발생하거나, 0으로 나누는 경우가 생겨 ZeroDivisionError가 발생하거나
        #속성오류로 AttributeError가 발생하거나 IndexError, KeyError가 발생하여 에러가 났을 경우에 
        pass #에러를 일으키지 않고 지나감
         
    
    message = Text(Point(5.5, -6.5), '<종료하려면 아무 곳이나 클릭하세요>')  #그래프 하단 좌표 (5.5, -6.5)에 '<종료하려면 아무 곳이나 클릭하세요>' 문구
    message.setFill('red')  #문구를 빨간색으로 설정
    message.draw(win)  #문구를 창에 출력
    win.getMouse()  #클릭이 감지되면 (아무곳이나 클릭할 시)
    win.close()   #프로그램 닫기

    


def main():  #main함수 정의
    print('이 프로그램은 파일을 읽어 단어들의 등장 횟수를 세고 빈도수 상위 11개의 단어를 그래프로 표현하는 프로그램입니다.\n')  #뭐하는 프로그램인지 설명
    print('꽉찬 그래프를 위해 단어가 적어도 11개 이상 있는 파일을 사용하는 것을 권장합니다.')   #권장사항을 알려줌
    print('<. , ! ? \" \' : 줄바꿈 세미콜론> 은 공백으로 바뀌어 단어에서 제거되며, 이후 공백 기준으로 단어를 분리합니다.')  #단어 분리 원리 설명
    print('그래프가 표현될 때 x축에 표현될 단어가 5글자 이상이면 그래프에는 4글자까지만 표현됩니다. 나머지는 IDLE창에서 확인하십시오. ')  #5글자이상의 단어가 어떻게 표현되는지 설명
    print('그래프창을 종료하려면 아무곳이나 클릭하면 됩니다.') #그래프창 종료 방법 설명
    print('\'전체 단어 정렬, 총 단어 수, 상위 11개 단어, 5글자 이상의 단어\'를 IDLE창에 출력한 뒤 그래프창이 뜹니다.\n') #프로그램의 출력 순서를 설명
    wordprogram()  #함수 wordprogram 실행


main()#main함수 실행



