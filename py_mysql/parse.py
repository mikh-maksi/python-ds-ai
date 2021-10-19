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


