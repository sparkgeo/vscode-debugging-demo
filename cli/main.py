import typer

app = typer.Typer()


BANNED_NAMES = [
    "voldemort", "sauron", "trump", "r.kelly", "bill cosby"
]


def is_name_banned(name: str):
    if name.lower() in BANNED_NAMES:
        return True
    return False


@app.command()
def hello(name: str):
    
    if is_name_banned(name):
        raise ValueError("I cannot Speak this name")

    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()