#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Use try-except if you suspect input issues, 
    # but the standard way is:
    try:
        line = sys.stdin.read().strip()
        if line:
            n = int(line)
        else:
            sys.exit(0)
    except EOFError:
        sys.exit(0)

    # Core Logic
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
