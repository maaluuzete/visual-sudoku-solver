import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout

con=Console()
DELAY=0.05

def rd():
    con.print("[bold cyan]Cole o Sudoku 9x9 (. ou 0 p/ vazio):[/bold cyan]")
    ln=[]
    while len(ln)<9:
        s=input().strip()
        if s: ln.append(s)
    b=[]
    if len(ln)!=9: raise ValueError("Precisa de 9 linhas")
    for r in ln:
        if len(r)!=9: raise ValueError("Linha != 9")
        row=[]
        for c in r:
            if c in ".0": row.append(0)
            elif c.isdigit() and 1<=int(c)<=9: row.append(int(c))
            else: raise ValueError("Char inválido")
        b.append(row)
    return b

def fe(b):
    for i in range(9):
        for j in range(9):
            if b[i][j]==0: return i,j
    return None

def ok(b,n,r,c):
    if n in b[r]: return False
    for i in range(9):
        if b[i][c]==n: return False
    br=(r//3)*3
    bc=(c//3)*3
    for i in range(br,br+3):
        for j in range(bc,bc+3):
            if b[i][j]==n: return False
    return True

def draw(b,hl=None):
    t=Table(show_header=False,box=None,padding=(0,1))
    for _ in range(9): t.add_column(justify="center")
    for i in range(9):
        rw=[]
        for j in range(9):
            v=b[i][j]
            tx=Text(str(v) if v else ".")
            if hl==(i,j): tx.stylize("bold yellow")
            rw.append(tx)
        t.add_row(*rw)
        if i in {2,5}: t.add_row(*["─"*3 for _ in range(9)])
    return t

def solve(b,lv,ly):
    e=fe(b)
    if not e:
        ly["st"].update(Panel("[bold green]Resolvido![/bold green]",title="Status"))
        return True
    r,c=e
    for n in range(1,10):
        ly["st"].update(Panel(f"[cyan]Tentando {n} em ({r+1},{c+1})[/cyan]",title="Status"))
        if ok(b,n,r,c):
            b[r][c]=n
            ly["bd"].update(Panel(draw(b,(r,c)),title="Sudoku"))
            lv.refresh()
            time.sleep(DELAY)
            if solve(b,lv,ly): return True
            b[r][c]=0
            ly["st"].update(Panel(f"[red]BACKTRACK ({r+1},{c+1})[/red]",title="Status"))
            ly["bd"].update(Panel(draw(b,(r,c)),title="Sudoku"))
            lv.refresh()
            time.sleep(DELAY)
    return False

def main():
    try: b=rd()
    except ValueError as e:
        con.print(f"[red]{e}[/red]")
        return
    ly=Layout()
    ly.split_row(Layout(name="bd",ratio=3),Layout(name="st",ratio=2))
    ly["bd"].update(Panel(draw(b),title="Sudoku"))
    ly["st"].update(Panel("Iniciando...",title="Status"))
    with Live(ly,console=con,refresh_per_second=30) as lv:
        solve(b,lv,ly)
    con.print("\n[bold green]Final:[/bold green]")
    con.print(draw(b))

if __name__=="__main__":
    main()
