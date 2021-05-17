# Fasta_to_GFA
A small python script converting Fasta files to GFA files for visualization in Bandage. This is just for visualization, since no coverage or linking information is available from a Fasta file. This also means that there are no circular fragments in these GFA files.

This can be used in cases like polishing with Medaka and Racon after a Flye assembly. Since Medaka and Racon do not provide a GFA output file, but Flye does.

## Usage
python gfa_maker.py infile1.fasta [infile2.fasta infile...] output_location

Any number of inputfiles can be provided. These should be in Fasta format, but don't necessarily need a .fasta extension.
The last argument will be the output directory. For current directory use ./

## Output
For every inputfile (infile*.fasta) an output file (infile*.gfa) will be created in the output location.
The output GFA can be visualized in https://rrwick.github.io/Bandage/
Note that there won't be any links or depth information since this is not present in a Fasta file.
