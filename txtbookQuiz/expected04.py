url = 'https://docs.python.org/3/tutorial'
index = url.find(':')
print(url[:index])
index = url.find('//') + 2
print(url[index: index + len('docs.python.org')])

index = url.rfind('/') + 1
print(url[index:])
print(url.find('d'))
print(url.rfind('d'))