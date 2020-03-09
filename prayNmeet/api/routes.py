from .controllers.user import( 
    UsersApi, UserRegister, 
    UserLogin
)


def initialize_routes(api):
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')