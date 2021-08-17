from fastapi import FastAPI

app=FastAPI()#인스턴스 설정

#3번째 줄에서 app을 인스턴스로먄 설정하고 호출을 하지 않으면 에러가 난다.

@app.get('/')#@가 decorate 역할을 한다.

def index():
    return {"data":"not inserted"}
#함수의 리턴 값은 문자열, 딕셔너리가 보통
