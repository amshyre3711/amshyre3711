import streamlit as stl
import time 

stl.title("Hello World!🇰🇷")
stl.text("이 것은 테스트 페이지입니다.")
ltm = time.strftime("%Z(%z)기준 %Y년 %m월 %d일 %p %I시 %M분 %S초")
y= stl.button("이건 세계 제일이라는 문장을 출력하는 버튼이야")
if y: stl.write("세계 제일!!!")
x = stl.text_input("",value="하고싶은 말을 입력해")
s = stl.button("입력한 걸 출력해주는 버튼이야.")
if s:stl.write(x)
cd ='stl.title("Hello World🇰🇷")\nstl.text("이 것은 테스트 페이지입니다.")\ny= stl.button("이건 세계 제일이라는 문장을 출력하는 버튼이야")\nif y: stl.write("세계 제일!!!")\nx = stl.text_input("",value="하고싶은 말을 입력해")\ns = stl.button("입력한 걸 출력해주는 버튼이야.")\nif s:stl.write(x)'
tt = stl.text("현재 페이지 소스코드")
stl.code(cd , language= "python")
tdup = stl.text("현재 시각 : {}".format(ltm))
tbu = stl.button("시간 갱신")
if tbu:tbup=tdup
with open("test.txt", "rb") as file:
    btn = stl.download_button(
            label="다운로드",
            data=file,
            file_name="test.txt"
          )
 