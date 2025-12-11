import os
import sys

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.core.bot import main

if __name__ == "__main__":
    main()
