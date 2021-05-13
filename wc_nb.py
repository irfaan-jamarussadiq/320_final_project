from json import load
from sys import argv

def loc(nb, option):
    if option == 'code':
        cells = load(open(nb))['cells']
        f = lambda c : len(c['source'])
        return sum(f(c) for c in cells)
    else:
        import io
        from nbformat import current

        with io.open(nb, 'r', encoding='utf-8') as f:
            nb = current.read(f, 'json')

        word_count = 0
        for cell in nb.worksheets[0].cells:
            if cell.cell_type == "markdown":
                word_count += len(cell['source'].replace('#', '').lstrip().split(' '))
        return word_count

def run(ipynb_files):
    x = sum(loc(nb, 'code') for nb in ipynb_files)
    y = sum(loc(nb, 'markdown') for nb in ipynb_files)

    print("Code:", x)
    print("Markdown:", y)

if __name__ == '__main__':
    run(argv[1:])