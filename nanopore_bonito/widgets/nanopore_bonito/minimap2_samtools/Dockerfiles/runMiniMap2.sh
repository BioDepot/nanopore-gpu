#!/bin/bash
makeArrayString() {
	echo $1 | sed 's/[][]//g' | sed 's/\,/ /g'
}
unquotedFile() {
	echo $* | sed 's/\"//g'
}

set -euf -o pipefail
mkdir -p $outputdir

files=($(makeArrayString $inputfiles))
for file in "${files[@]}"; do
	echo "working on $file"
	unquoted=$(unquotedFile $file)
    filename=$(basename -- "$unquoted")
    bambase="$outputdir/${filename%%.*}"-sorted
    minimap2 -ax map-ont $indexfile $inputfiles | samtools view -bS | samtools sort -O BAM | tee "$bambase.bam" | samtools index - "$bambase.bai"
done





