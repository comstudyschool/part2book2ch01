# 실습 : 
# 1. join-us.html 파일을 만든다.
# 2. 신상 정보 입력 받을수 있도록 form 구현
# 3. 신상 정보는 성명, 주소, 전화번호, email, 나이, 성별 등.
# 4. main.py에서 데이터를 전송 받아서 터미널에 출력 or 파일 저장.

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime
import csv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def show_form(request: Request) :
    return templates.TemplateResponse(
        "join-us.html", {"request": request}
    )


@app.post("/join")
def submit_form(
    request: Request,
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: str = Form(...),
    gender: str = Form(...)
) :
    print(">>>> [POST - /join]", name, address, phone, email, age, gender)
    
    return {
        "name": name, 
        "address": address, 
        "phone": phone,  
        "email": email, 
        "age": age, 
        "gender": gender
    }
    