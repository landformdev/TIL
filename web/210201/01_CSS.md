# 210201 CSS 시작



html과 CSS는 각각의 언어를 가진 별개의 언어이다. but CSS는 html없인 사용 불가

![image-20210201140756117](01_CSS.assets/image-20210201140756117.png)



정의방법

1. 인라인 : 해당 태그에 style 속성을 이용
2. 내부참조 : <head>내에 <style>에 지정
3. 외부참조 - 분리된 CSS파일 : 외부 CSS파일을 <head>내에 <link>를 통해 연결

![image-20210201141843391](01_CSS.assets/image-20210201141843391.png)

 lorem  +Tab : 아무문장 생성



class 선택자





![image-20210201144453560](01_CSS.assets/image-20210201144453560.png)

!important 는 정말 특수한 경우가 아니면 사용하지 않음

class선택자 위주로 작성하는 것이 편하다.

소스 순서는 늦게 작성된게 덮어 씌운다.



![image-20210201150957500](01_CSS.assets/image-20210201150957500.png)





![image-20210201151807735](01_CSS.assets/image-20210201151807735.png)

html기본 사이즈는 16px

em은 계속 상속받아 예상외의 크기가 되기도함

rem이 편하다. but 이것만 쓰는건 아님



![image-20210201152533017](01_CSS.assets/image-20210201152533017.png)



## BOX model

![image-20210201152841582](01_CSS.assets/image-20210201152841582.png)



Margin : 상하좌우

![image-20210201153353039](01_CSS.assets/image-20210201153353039.png)

margin: 0 auto;  :  /* 가운데 정렬 */



Border : 상하좌우

![image-20210201153451317](01_CSS.assets/image-20210201153451317.png)



Padding : 상하좌우



![image-20210201154644745](01_CSS.assets/image-20210201154644745.png)

border와 padding까지 고려해서 width를 정해야함

![image-20210201154834421](01_CSS.assets/image-20210201154834421.png)

일반적으로 시작시  border-box를 선언하고 시작하는 경우가 많음

```
    * {
      box-sizing: border-box;
    }
```



마진상쇄

블럭요소의 top bottom에서 발생







![image-20210201155733689](01_CSS.assets/image-20210201155733689.png)

![image-20210201155826823](01_CSS.assets/image-20210201155826823.png)

block은 기본 너비의 100%

inline은 컨텐츠 영역만큼 만



![image-20210201155936081](01_CSS.assets/image-20210201155936081.png)

![image-20210201155959622](01_CSS.assets/image-20210201155959622.png)

none을 쓰면 공간이 사라져 밑에 것이 위로 올라가서 망칠수 있다.





## ===================================================================



