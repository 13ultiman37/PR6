import pandas as pd
import scipy.stats as st

pd.options.display.max_columns = 10

throws = pd.DataFrame({'N': [1, 2, 3, 4, 5, 6], 'Observed': [97, 98, 109, 95, 97, 104]})
throws['Expected'] = 100

k = len(throws.N)

diff = throws.Observed - throws.Expected
throws['Difference'] = diff
throws['SquareDiff'] = throws['Difference'] ** 2
throws['SquareDiff/Expected'] = throws['SquareDiff'] / throws.Expected
print(throws)

stats = throws['SquareDiff/Expected'].sum()
print('\nСтатистика: ', stats)

pval = 1 - st.chi2.cdf(stats, k)
print('Вероятность получить похожее значение или выше, исходя из полученной статистики: ', pval)

print('\n', st.chisquare(throws['Observed'], throws['Expected']))
