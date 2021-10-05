f = open('/Users/mac/Documents/work/python/python-ds-ai/py/data.csv', 'r')
elements_list = []
for line in f:
   line
   elements = line.split(';')
   elements.pop()
   elements_list.append(elements)
elements_list.pop()
print(elements_list)
print(elements_list)
for element in elements:
    element = element.replace(' ','')
    element = element.replace(',','.')
    print(float(element))


import plotly.graph_objects as go
some_list = [2, 4, 4, 3]

f = go.FigureWidget()
f.add_scatter(y=some_list);
f.add_bar(y=[1, 4, 3, 2]);
f.layout.title = 'Hello FigureWidget'
f.show()