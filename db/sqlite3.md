# 설치

sqlite 홈페이지에 다운로드에서 파일 2개 받음

![image-20210325102713189](sqlite3.assets/image-20210325102713189.png)



C:\sqlite 폴더 생성 후 저장

![image-20210325102738870](sqlite3.assets/image-20210325102738870.png)



안의 파일 끄집어내기

![image-20210325102814299](sqlite3.assets/image-20210325102814299.png)



![image-20210325102930574](sqlite3.assets/image-20210325102930574.png)

환경변수에 시스템변수에 path 더블클릭 후 경로 추가

![image-20210325103801631](sqlite3.assets/image-20210325103801631.png)



## 사용하기

사용가능~✨

![image-20210325103719229](sqlite3.assets/image-20210325103719229.png)

종료는 ctrl + z 엔터



![image-20210325104233673](sqlite3.assets/image-20210325104233673.png)

;로 데이터베이스 생성

![image-20210325104426150](sqlite3.assets/image-20210325104426150.png)

csv사용 가능하게 모드 변경

![image-20210325104640507](sqlite3.assets/image-20210325104640507.png)

파일을 테이블에 넣기 (example이 테이블 이름)

![image-20210325104801690](sqlite3.assets/image-20210325104801690.png)



테이블 삭제 (그냥 DROP TABLE도 가능)

![image-20210325105522566](sqlite3.assets/image-20210325105522566.png)



테이블 내의 모든 값 가져오기

![image-20210325105311653](sqlite3.assets/image-20210325105311653.png)

테이블 생성

![image-20210325110655643](sqlite3.assets/image-20210325110655643.png)

sqlite자체에선 명령어의 수정이 귀찮으니 파일 하나 만들고 읽어오는 식으로 진행

![image-20210325111225940](sqlite3.assets/image-20210325111225940.png)





dbshell 구문을 이용해 django에서 db만지는 것 가능

![image-20210325152326069](sqlite3.assets/image-20210325152326069.png)



shell_plus에서 코드 작성시 sql문을 보여줌

- python manage.py shell_plus --print-sql