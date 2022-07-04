import os.path as path
import sys

sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from moduleA import SomeClass

myClass = SomeClass()
myClass.work('InstatSport')
