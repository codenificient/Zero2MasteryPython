# Short Circuiting
is_friend = True
is_User = False
if is_friend and is_User:
    print("Best Friends Forever")

if is_friend or is_User:
    print("Is friend and not care if is user!")

print(1 < 2 > 3 < 5)