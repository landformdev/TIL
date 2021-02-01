# 210201  HTML 시작

## tags

html은 기본적으로 에러가 없다!

```<h1>Hello SSAFY</h1>```

그냥 이렇게 써도 브라우저에서 보이긴 함, 브라우져가 알아서 잡아줌 but  다 쓰자



마크업을 작성할땐 내용에 신경쓰자!

만드는 도중 화면 볼 필요 없다! 꾸미는건 나중일!



### block 요소   ( display : block; )

!+tab을 통해 vscode에선 최소한의 틀을 잡아줌 (emmet)

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

</body>
</html>
```



Contro+Enter : 어느곳에서든 밑에 줄로 엔터

Ctrl+Shift+Enter : 어느곳에서든 윗줄로 엔터

Alt + 방향키 : 코드를 가지고 줄이동 가능

ul>li*3  + Tab: ul태그 안에 li태그 3개 들어감

```
<body>

  <h1>This is Heading 1</h1>
  <h2>2</h2>
  <h3>3</h3>
  <h4>4</h4>
  <h5>5</h5>
  <h6>6</h6>
  
  <p>본문(paragraph)</p>
  
  <ol>
    <li>순서가 있는 리스트</li>
    <li>Ordered List</li>
    <li>md: 1.</li>
  </ol>

  <ul>
    <li>Unordered List</li>
    <li>순서가 없는 List</li>
    <li>md: -</li>
  </ul>
```

태그들 사이에 엔터 실제론 반영 안됨



폼

```
  <form action="">
    <input type="text">
    <input type="submit">
  </form>

</body>
```



구역 묶고 나누기용

```
  <div></div>
  <section></section>
  <header></header>
  <article></article>
  <aside></aside>
  <footer></footer>
  <nav></nav>
```



### inline 요소

인라인 요소는 형광펜 먹이듯이 쓴다.

인라인요소는 블럭요소를 자식응로 가지지 못함 ( 반대는 가능 )



target="_blank"는 새창에서 열어줌

<b> 와 <i>는 필요가 없다! 의미 부여하지 않고 굳이 변형하는 것 이므로!

```
  <a href="http://google.com">google</a>은 짱짱한 검색엔진이다.
  <br>
  시험 성적 확인은 <a href="http://edu.ssafy.com" target="_blank">이곳</a>에서 새창으로 열어주자

  <br>

  <span></span>

  내<b>용</b>은   
  HTML 문서에서 가장<strong>중요한</strong> 내용은 이것이다.

  기<i>울</i>여
  이 내용은<em>기울어진다</em>아아아

  <button>눌러</button>이게 버튼이다.
```











