import pathlib

class Site:

    def __new__(site, *args, **kwargs):
        print("Create new instance of site")
        return super().__new__(site)

    def __init__(self, source, dest):
        print("Initiliase the new stane of site.")
        self.source = Path( source )
        self.dest = dest

    def create_dir(self, path):
        directory = self.dest+"/"+self.source
        Path( directory ).mkdir( parents=True, exist_ok=True )

    def build():
        Path( self.dest ).mkdir( parents=True, exist_ok=True )
        for path in self.source.rglob("*"):
            if path == directory:
                create_dir(path)
