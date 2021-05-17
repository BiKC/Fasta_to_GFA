
######################
##   FASTA to GFA   ##
######################
# Usage: python gfa_maker.py infile1.fasta [infile2.fasta infile...] output_location4
# Output can be viewed using bandage

import sys
import os

if len(sys.argv) <= 1:
    print("No file(s) supplied")
    sys.exit()

if len(sys.argv) == 2:
    print("No output location supplied")
    sys.exit()

if not os.isdir(sys.argv[-1]):
    print("Output location is not a directory")

for f in sys.argv[1:-1]:
    try:
        with open(f, 'r') as ifile:
            with open(sys.argv[-1]+"/"+f.split("/")[-1].split(".")[0]+".gfa", "w") as ofile:
                ofile.write("H\tVN:Z:1.0")
                for line in ifile:
                    if not line.startswith(">"):
                        ofile.write(line.strip())
                    else:
                        ofile.write("\nS\t"+line[1:].strip()+"\t")
    except Exception as e:
        print("e")
        continue
