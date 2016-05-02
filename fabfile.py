from fabric.api import *

# env.hosts = ['115.159.190.97']
# env.user = 'ubuntu'
# env.password = ''


def hello():
    print "hello world"


# def deploy():
#     with cd('/home/ubuntu/Todo'):
#         run('git pull')
#         sudo('supervisorctl restart todo')
#         sudo('supervisorctl status')