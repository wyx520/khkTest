from flask.ext.script import Manager
from app import create_app

app = create_app('development')

manager = Manager(app)

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)


if __name__ == '__main__':
    manager.run()