#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard libvrary"""

#import code to complete task
import shutil
import os

def main():
    ""code to move files around""
    #force program to start in home directory
    os.chdir("/home/student/mycode/")

    #copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
