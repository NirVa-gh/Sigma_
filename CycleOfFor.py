'''import time

for i in range(0,56,10):
    time.sleep(0.1)
    print(i)'''
'''list = [1,2,3,4]
for i in list:
    print(i+10)'''


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for i in sorted(favorite_languages.keys()):
    print(i)

favorite_languages.pop('phil')
print(favorite_languages)