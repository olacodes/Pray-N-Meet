from .controllers.user import( 
    UsersApi, UserRegister, 
    UserLogin
)
from .controllers.github_login import GithubLogin

def initialize_routes(api):
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(GithubLogin, '/login/github')
    