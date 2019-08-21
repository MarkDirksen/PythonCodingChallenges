import numpy as np

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

profit = []
profitAfterTax = []
profitMargin = []
goodMonths = []
badMonths = []
bestMonth = []
worstMonth = []

for i in range(12):
    r = revenue[i]
    e = expenses[i]
    
    p = r - e
    pat = p * 0.7
    pm = pat / r
    
    profit.append(p)
    profitAfterTax.append(pat)
    profitMargin.append(pm)

meanProfitAfterTax = np.mean(profitAfterTax)

for i in range(12):
    m = months[i]
    if profitAfterTax[i] < meanProfitAfterTax:
        badMonths.append(m)
    if profitAfterTax[i] > meanProfitAfterTax:
        goodMonths.append(m)

wM = months[np.argmin(profitAfterTax)]
bM = months[np.argmax(profitAfterTax)]

bestMonth.append(bM)
worstMonth.append(wM)

rounded_profit = [ round(i / 1000, 0) for i in profit ]
formatted_profit = [ "{:.0f}".format(i) for i in rounded_profit ]

rounded_profitAfterTax= [ round(i / 1000, 0) for i in profitAfterTax ]
formatted_profitAfterTax = [ "{:.0f}".format(i) for i in rounded_profitAfterTax ]

rounded_profitMargin= [ round(i * 100, 0) for i in profitMargin ]
formatted_profitMargin = [ "{:.0f}".format(i) for i in rounded_profitMargin ]

print("Profit ($1000) per month:")
print(formatted_profit)
print("profit after tax ($1000) per month:")
print(formatted_profitAfterTax)
print("Profit margin (%) per month:")
print(formatted_profitMargin)
print("Good months:")
print(goodMonths)
print("Bad months:")
print(badMonths)
print("Best month:")
print(bestMonth)
print("Worst month:")
print(worstMonth)