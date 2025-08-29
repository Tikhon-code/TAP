# TAP
## Tikhon Arg Parser
This is a minimal library for parse arguments command line

# Examples
```
#main.py
import sys
from TAP import Parser

parser = Parser(len(sys.argv), sys.argv)
parser.add_opts("-test")
parser.run()

for arg in parser.retopts:
  opt, value = arg
  if opt == "-test":
    print(value)
```
