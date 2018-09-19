n=int(input('enter number:'))
temp=n
rev=0
while(n>0):
n=n//10
if(temp==rev):
  print('the number is palindrome')
  else:
    print('the number is a not palindrome')
