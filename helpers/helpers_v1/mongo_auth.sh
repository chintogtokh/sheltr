use sheltr
db.createUser(
  {
    'user': "admin",
    'pwd': "AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA=",
    roles: [
       { role: "readWrite", db: "sheltr" },
    ]
  }
)