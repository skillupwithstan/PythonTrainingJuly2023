#pass
for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            pass
            print("Add User "+ user + " for " + server)

print("*******************************************")
#break
for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            break
        print("Add User "+ user + " for " + server)

print("*******************************************")
#continue
for server in "server01","server02","server03":
    for user in "user01","user02":
        if(user == "user02"):
            continue
        print("Add User "+ user + " for " + server)

print("*******************************************")
