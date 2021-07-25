import csv

# bid = buying
def init(fileName, stocks, bid, n):
    header = ['stockName', 'bid', 'current', 'benefit', 'benefit ratio']
    f = open(fileName+'.csv', 'w', encoding='utf-8')
    wr = csv.writer(f)
    wr.writerow(header)
    for i in range(n):
        wr.writerow([stocks[i], bid[i], 100, 100-bid[i], 0])

    f.close()

stocks = ['kakao', 'disney']
bid = [40, 50]
init('example-MyPortfolio', stocks, bid, 2)
