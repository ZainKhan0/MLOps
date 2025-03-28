import yfinance as yf # type: ignore
import pandas as pd #type: ignore


ticker = input("Enter the ticker: ")
start_date = input("Enter the start date format yyyy-mm-dd: ")
end_date = input("Enter the end date format yyyy-mm-dd: ")

def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start = start_date, end = end_date)

    data.to_csv("data.csv")
    print("Data downloaded successfully and saved to data.csv")

download_data(ticker, start_date, end_date)


