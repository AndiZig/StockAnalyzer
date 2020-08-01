import yfinance as yf
import matplotlib.pyplot as plt

BitcoinEUR = yf.Ticker("AAPL")
btc = BitcoinEUR.history(period='1y', interval='1d')

plt.plot(btc['Open'])
plt.plot(btc['Open'].rolling(window=22).mean())
plt.show()



for i_ma in range(200):
    ma50 = btc.iloc[:, 1].rolling(window=i_ma).mean()
    kurs_steigt = True
    status = "Long"
    start_preis = 0
    gewinn = 0
    for i in range(len(btc['Open'])):
        if ma50[i] < btc['Open'][i]:
            if kurs_steigt:
                if start_preis != 0:
                    gewinn += (start_preis - btc['Open'][i])
                print("Long bei", btc['Open'][i])
                status = "Long"
                start_preis = btc['Open'][i]
            kurs_steigt = False
        else:
            if not kurs_steigt:
                if start_preis != 0:
                    gewinn += (btc['Open'][i] - start_preis)
                print("Short bei", btc['Open'][i])
                status = "Short"
                start_preis = btc['Open'][i]
            kurs_steigt = True
    print("Gewinn bei", i_ma, ":", (gewinn / btc['Open'][0] - 1) * 100, "%")





#mp.plot(btc['Open'])
#for i_ma in range(2):
#    mp.plot(btc.iloc[:, 1].rolling(window=i_ma*50).mean())
#mp.show()




