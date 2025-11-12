from invoke import task

@task
def clean(c):
    """Windows Clean up temporary files."""
    c.run("rmdir /S /Q temp_files "
          "|| echo No temporary files to remove.")

@task(pre=[clean])
def build(c):
    """Build the project."""
    c.run("echo Building the project...")