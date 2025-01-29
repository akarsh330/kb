user_name=input('enter user name: ')
plan=input('enter plan ex: normal,prime: ')
id=int(input('enter your id: '))
lst=[111,222,444]
if plan=='prime' and id in lst:
    print('ur a prime member')
else:
    print('invalid prime user')