unconfirmed_users = ['alice, brian, candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('verifying user:' + current_user.title())
    confirmed_users.append(current_user)
    print('\n the folowing users have been confirmed')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())