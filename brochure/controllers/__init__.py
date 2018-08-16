import os
from glob import glob

globbing = os.path.dirname(__file__) + '/*.py'
__all__ = [os.path.basename(f)[:-3] for f in glob(globbing)]
