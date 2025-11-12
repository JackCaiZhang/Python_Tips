import click
import rich_click as rc
from rich.console import Console
from rich.table import Table

console = Console()

# 使用 rich_click 美化帮助
rc.SYSTEM_HELPTEXT = 'bold cyan'
rc.SYSTEM_OPTION = 'bold green'
rc.STYLE_COMMAND = 'bold yellow'
rc.GLOBAL_HELP_HEADER = '✨ Awesome CLI工具 ✨'
rc.GLOBAL_HELP_FOOTER = '感谢使用！🚀'

@click.group(help='一个使用 rich_click 打造的漂亮 CLI 工具')
def cli():
    pass

@cli.command(help='打印问候语')
@click.option('--name', '-n',
              default='朋友', help='你的名字')
def hello(name):
    console.print(f'👋 你好, [bold magenta]{name}[/]!')

@cli.command(help='显示数据表格')
def show():
    table = Table(title='用户列表')

    table.add_column('ID',
                     justify='right',
                     style='cyan',
                     no_wrap=True)
    table.add_column('Name',
                     style='magenta')
    table.add_column('Role',
                     justify='center',
                     style='green')

    table.add_row('1', 'Jack Zhang', 'Admin')
    table.add_row('2', 'Bob', 'User')
    table.add_row('3', 'Charlie', 'Guest')

    console.print(table)

@cli.command(help='模拟任务进度')
def progress():
    from rich.progress import Progress
    import time

    with Progress() as prog:
        task = prog.add_task("[cyan]处理任务...",
                             total=100)
        for _ in range(100):
            prog.update(task, advance=1)
            time.sleep(0.05)

if __name__ == '__main__':
    cli()