from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requestDTO import DACRequest
from service import getPredict
app = FastAPI()

origins = ["*"]

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
def read_item(request : DACRequest):
    print("zz")
    for i in request.table1:
        print(*i)
    print()
    print()
    for i in request.table2:
        print(*i)
    print()
    print()
    for i in request.table3:
        print(*i)
    print()
    print()
    getPredict(request.table1, request.table2, request.table3)
    return {"hello" : "world"}
