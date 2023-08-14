import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

if __name__ == "__main__":
    style.use('ggplot')

    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()

    df = web.DataReader("TSLA", "morningstar", start, end)
    print(df.head())

    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)

    print(df.head())

    df.to_csv('tsla.csv')
    df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

    df.plot()
    plt.show()

    df['Adj Close'].plot()
    plt.show()

    df[['High', 'Low']]

    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

    print(df.head())

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])

    plt.show()