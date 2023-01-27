from typing import List
from pathlib import Path

class Parser:
    extensions = List[str] = []

    def valid_extensions(extension):
        for e in self.extensions:
            if e == extension:
                return True
            else:
                return False
