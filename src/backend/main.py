from fastapi import FastAPI

app = FastAPI()

@app.post('/model')
async def predict():
   print("Hello world")

import uvicorn
uvicorn.run(app)