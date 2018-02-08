class Service:
    secret = "귄분은 귀엽다"


Guin = Service()

print(Guin.secret)
print(Service.secret)

Service.secret = "귄분은 멋지다"

print(Guin.secret)
