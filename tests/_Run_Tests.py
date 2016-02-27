##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import subprocess
import sys

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

_input = input if sys.version_info >= (3, 0) else raw_input

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def run_tests():
    """Runs all found test scripts. Returns True if all tests pass."""
    fail = 0
    okay = 0
    for i in os.listdir("."):
        if i.find("_test_") > -1 and i.endswith(".py"):
            if 0 != subprocess.call("python " + i):
                fail += 1
            else:
                okay += 1
    print("[DONE]"),
    if fail:
        print("Errors in unit tests!")
        return False
    print("All %u tests completely successfully!" % (okay))
    return True

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    okay = run_tests()
    _input("Press ENTER to continue...")
    sys.exit(0 if okay else 1)