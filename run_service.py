from datetime import date
from typing import Optional
from db import connection
from db.model.yahoo import get_historical_data, get_news_data
from fastapi import FastAPI, Query


app = FastAPI(title='Yahoo service')

@app.on_event("startup")
async def startup():
    await connection.get_db().connect()


@app.on_event("shutdown")
async def shutdown():
    await connection.get_db().disconnect()

@app.get("/")
async def root():
    return {"message": "API for providing historical stocks and news data. You can find the API description on:  http://host:port/docs or http://host:port/redoc"}

@app.get('/historical/{company}')
async def historical(company:str, start_date: Optional[date] = Query(None), end_date: Optional[date] = Query(None)):
    print(company, start_date, end_date)
    query = get_historical_data(company, start_date, end_date)
    print(query)
    return await connection.get_db().fetch_all(query)

@app.get('/news/{company}')
async def news(company:str, start_date: Optional[date] = Query(None), end_date: Optional[date] = Query(None)):
    query = get_news_data(company, start_date, end_date)
    return await connection.get_db().fetch_all(query)

