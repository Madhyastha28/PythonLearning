name = input("Enter the name: ")
date = input("Enter the date: ")
template = '''
Dear <Name>'''
print(template.replace('<Name>', name))
