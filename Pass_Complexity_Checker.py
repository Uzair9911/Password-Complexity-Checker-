import string
password = "i_am_!@{uzair9911}BOLT4264"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password ])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password ])
special = any([1 if c in string.punctuation else 0 for c in password ])
digits = any([1 if c in string.digits else 0 for c in password ])



characters = [upper_case,lower_case,special,digits]

length = len(password)

score = 0

with open('10-million-password-list-top-10000.txt','r') as f:
    common = f.read().splitlines()

    if password in common:
        print("Password was found in a common list, Score: 0/7")
        exit()

if length > 8:
    score += 1
    if length > 12:
        score += 1
        if length > 17:
            score += 1
            if length > 20:
                score += 1
print(f"Password lenght is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1
    if sum(characters) > 2:
        score += 1
        if sum(characters) > 3:
            score += 1
print(f"Password has {str(sum(characters))} diffrent characters types!, adding {str(sum(characters)-1)} points!")


if score < 4:
    print(f"The password is quite weak! score: {str(score)} / 7")
elif score == 4:
    print(f"The password is ok! score: {str(score)} / 7")
elif score > 4 and score < 6:
    print(f"The password is pretty! good score: {str(score)} / 7")
elif score > 6:
    print(f"The password is string! score: {str(score)} / 7")
