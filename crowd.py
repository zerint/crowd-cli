import confuse
import typer
from components.group import Groups

source = confuse.YamlSource('config.yml')
config = confuse.RootView([source])
app = typer.Typer(add_completion=False)

group = Groups(config)

app.add_typer(group.get_app(), name='group')

if __name__ == "__main__":
    app()
