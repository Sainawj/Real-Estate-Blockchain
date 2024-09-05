sudo systemctl start mongod

# Open MongoDB shell
mongo

# Switch to admin database
use admin

# Create a new database (replace `realestate_db` with your preferred name)
use realestate_db

# Create a new user for the database
db.createUser({
  user: "realestate_user",
  pwd: "your_password",
  roles: [
    { role: "readWrite", db: "realestate_db" }
  ]
})

# Exit the MongoDB shell
exit