from sqlalchemy.sql import select
from db import metadata
from sqlalchemy import func, text, UniqueConstraint
from sqlalchemy import Table, Column, String, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT, DATE, DECIMAL, TEXT, VARCHAR

yahoo_historical = Table('yahoo_historical', metadata,
                Column('id', BIGINT(20), primary_key=True, autoincrement=True),
                Column('Date', DATE(),nullable=False, index=True),
                Column('Symbol', String(32), nullable=False, index=True),
                Column('Open', DECIMAL(20, 8), nullable=False),
                Column('High', DECIMAL(20, 8), nullable=False),
                Column('Low', DECIMAL(20, 8), nullable=False),
                Column('Close', DECIMAL(20, 8), nullable=False),
                Column('Adj Close', DECIMAL(20, 8), nullable=False, key='adj_close'),
                Column('Volume', DECIMAL(20, 8), nullable=False),
                Column('3day_before_change', DECIMAL(12, 4), nullable=False, key='_3day_before_change'),
                Column('created_at', TIMESTAMP, nullable=False, server_default=func.now()),
                Column('updated_at', TIMESTAMP, nullable=False,
                       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), index=True),
                UniqueConstraint('Symbol', 'Date', name='symbol_date_uniq')
          )

yahoo_news = Table('yahoo_news', metadata,
                Column('id', BIGINT(20), primary_key=True, autoincrement=True),
                Column('Symbol', String(32), nullable=False, index=True),
                Column('Link', VARCHAR(1024),nullable=False),
                Column('Title', TEXT(), nullable=False),
                Column('created_at', TIMESTAMP, nullable=False, server_default=func.now()),
                Column('updated_at', TIMESTAMP, nullable=False,
                       server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), index=True),
                UniqueConstraint('Link', name='link_uniq')
          )

def get_historical_data(company, start_date, end_date):
    where_clause = f"`Symbol` = '{company}'"
    start_date_clause = ''
    end_date_clause = ''
    bool_and = ''
    if start_date or end_date:
        where_clause += " and "
        if start_date and end_date:
            bool_and = 'and '
        if start_date:
            start_date_clause = f"`Date` > '{start_date}'"
        if end_date:
            end_date_clause = f"`Date` < '{end_date}'"
        where_clause += f' {start_date_clause} {bool_and} {end_date_clause}'
    query = select([yahoo_historical.c.Date,
                               yahoo_historical.c.Symbol,
                               yahoo_historical.c.Open,
                               yahoo_historical.c.High,
                               yahoo_historical.c.Low,
                               yahoo_historical.c.Close,
                               yahoo_historical.c.adj_close,
                               yahoo_historical.c._3day_before_change]
                              ).where(text(where_clause))
    return query

def get_news_data(company, start_date, end_date):
    where_clause = f"`Symbol` = '{company} '"
    start_date_clause = ''
    end_date_clause = ''
    bool_and = ''
    if start_date or end_date:
        where_clause += " and "
        if start_date and end_date:
            bool_and = 'and '
        if start_date:
            start_date_clause = f"`created_at` > '{start_date}'"
        if end_date:
            end_date_clause = f"`created_at` < '{end_date}'"
        where_clause += f' {start_date_clause} {bool_and} {end_date_clause}'
    query = select([yahoo_news.c.Symbol,
                               yahoo_news.c.Title,
                               yahoo_news.c.Link,
                               yahoo_news.c.created_at]
                              ).where(text(where_clause))
    return query

