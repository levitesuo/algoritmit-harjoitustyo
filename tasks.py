from invoke import task


@task
def run(ctx):
    ctx.run("python3 src/index.py")
