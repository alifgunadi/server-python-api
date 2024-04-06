import utils.logger_setup as logger_setup

# condition method
condition = 5 > 20
if condition:
    print(False)
elif 10 > 50:
    print(False)
else:
    print(True)

# # input method
# name = input("my name is ")
# print("call me", name)


# function python
def myAge(x):
    logger_setup.logger.info(f"my age {int(20) + x}")
    print("I'm", int(20) + x)


myAge(6)

# while loops
i = 1
while i < 10:
    print(i)
    i += 1

print("--------------")

# for loops
identity = [
    {"id": 1, "user": "alif"},
    {"id": 2, "user": "zaqi"},
]

for el in identity:
    get_id = el["id"]
    get_user = el["user"]
    logger_setup.logger.info(f"get id {get_id}")
    logger_setup.logger.info(f"get user {get_user}")
    print("get id", get_id)
    print("get user", get_user)


for el in range(2, 9):
    print(el)


print("--------------")

for el in range(6):
    print(el)

for index, x in enumerate([10, 11, 12]):
    if index == 0:
        print(x)
        break
