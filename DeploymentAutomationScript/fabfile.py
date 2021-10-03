from fabric2 import Connection,task


SSH_CONNECTION_PROPERTIES = {
    "user":"your_username_here",
    "password":"your_password_here",
    "host":"your_hostname_here",
    "connect_kwargs": {
        "key_filename": "path to rsa file if using public key auth"
    },
}

GIT_BRANCH = "main"
DIRECTORY_PATH = "path/to/your/directory"

@task
def git_pull(ctx):
    ctx.run("git pull origin {}".format(GIT_BRANCH))
@task
def docker_build(ctx):
    ctx.run("docker-compose up --build -d")
@task 
def docker_down(ctx):
    ctx.run("docker-compose down")

@task
def deploy(ctx):
        with Connection(*SSH_CONNECTION_PROPERTIES) as c:
            with c.cd(DIRECTORY_PATH):
                docker_down()
                git_pull()
                docker_build()    




