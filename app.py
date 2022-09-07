from flask import Flask, render_template, request, jsonify, Response, json, redirect
from flask_pymongo import PyMongo, ObjectId
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI']="mongodb://localhost/artdb"
mongo = PyMongo(app)

db = mongo.db.users


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['GET'])
def getUsers():
    new_user = []
    for i in db.find():
        new_user.append(i)

    return render_template("home.html", newuser=new_user)


@app.route("/registration", methods=["POST","GET"])
def createUsers():

    # return Response(
    #     mimetype="application/json",
    #     status=201,
    #     response=json.dumps({"message": "User created successfully", "id":str(id.inserted_id)})
    # )

    if request.method == "POST":

        new_name = request.form['name']
        new_email = request.form['email']
        new_password = request.form['password']
        haspassword = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        id = db.insert_one({
            'name': new_name,
            'email': new_email,
            'password': haspassword
        })

        return redirect("/registration")

    return render_template("register.html")






if __name__ == "__main__":
    app.run(debug=True, port=2000)


# mongo -->   { 
#                  name: tom
#                  email: tom@gmail.com            
# }
