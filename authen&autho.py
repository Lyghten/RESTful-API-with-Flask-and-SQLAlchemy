from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Example: authenticate user (dummy example)
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad credentials"}), 401
        

from flask_jwt_extended import jwt_required

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'You have accessed a protected route'}, 200
