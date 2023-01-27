from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self.source = Path( source )
        self.dest = Path( dest )

    def create_dir(self, path):
        directory = ""
        directory = self.dest + "/" + Path.relative_to(self.source)
        directory.mkdir( parents=True, exist_ok=True )

    def build():
        Path( self.dest ).mkdir( parents=True, exist_ok=True )
        for path in self.source.rglob("*"):
            if path == directory:
                create_dir(path)
