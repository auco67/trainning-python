print('continueとpassの違い')
print('continueの場合')
for i in range(3):
    print(i)
    if i == 1:
        continue
        print('continue')
        
print('')
print('passの場合')
for i in range(3):
    print(i)
    if i == 1:
        pass
        print('pass')
