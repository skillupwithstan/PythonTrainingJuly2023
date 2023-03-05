for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server != "server02"):
            print("Add User "+ user + " for " + server)
