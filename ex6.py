# Given the following dictionary, that stores users data, calculating the average age of these users

users = {
    '1' : {
        "first_name": "Sophia",
        "last_name": "Bennet",
        "age": 30
    },
    '2' : {
        "first_name": "Ethan",
        "last_name": "Caldwell",
        "age": 45
    },
    '3' : {
        "first_name" : "Liam",
        "last_name": "Montgomery",
        "age": 32
    },
    '4' : {
        "first_name" : "Ava",
        "last_name": "Thompson",
        "age": 18
    },
    '5' : {
        "first_name" : "Noah",
        "last_name": "Harrison",
        "age": 57
    }
}

######### SOLUTION #########

age_sum = 0
user_counter = 0

for index, user in users.items():
    user_counter += 1
    age_sum += user["age"]

mean = age_sum / user_counter

print(f"Average age: {mean:.1f}")