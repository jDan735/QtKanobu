from os import system
from __init__ import __version__

system("pyinstaller __main__.py --onefile --noconsole --icon qtkanobu.ico")
system(f"mv dist/__main__.exe dist/QtKanobu-{__version__}.exe")
