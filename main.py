import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Index',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity',
    '/profile', 'Profile',
    '/setting', 'Setting',
    '/update-settings', 'UpdateSettings'

)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})


class Index:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.Home(posts)


class Profile:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.Profile(posts)


class Register:
    def GET(self):
        return render.Register()


class Setting:
    def GET(self):
        return render.Setting()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)
        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['name']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return "Some unexpected error take place try again..."

class Logout:
    def GET(self):
        session['user']=None
        session_data['user']=None
        session.kill()
        return "success"


if __name__ == "__main__":
    app.run()
