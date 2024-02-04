import yfinance 
#GOOG
import yfinance

hist = yfinance.Ticker("GOOG").history(
            period ="4d",
            interval = "1h",
            start = "2023-01-05",
            end = "2023-01-09",
            prepost = True
)

print(hist.info())
