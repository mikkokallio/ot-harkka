from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/maksukortti.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
