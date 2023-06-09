a = 'radar'
b = 'birthday'
print(type(a),type(b))
# check - palindrome
if a==a[::-1]:
    print(a+ ' is a palindrome')
else:
    print(a+ ' is not a palindrome')
if b==b[::-1]:
    print(b+ ' is a palindrome')
else:
    print(b+ ' is not a palindrome')
