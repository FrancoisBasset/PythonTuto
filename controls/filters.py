def filter_names1():
    users = { "François": "active", "Théophile": "inactive", "Francis": "active" }

    for user, status in users.copy().items():
        if status == "inactive":
            del users[user]

    print(users)

def filter_names2():
    users = { "François": "active", "Théophile": "inactive", "Francis": "active" }
    active_users = {}

    for user, status in users.items():
        if status == 'active':
            active_users[user] = status

    print(active_users)

def filter_names3():
    users = { "François": "active", "Théophile": "inactive", "Francis": "active" }
    actives = {name : status for name, status in users.items() if status == "active"}

    print(actives)
    