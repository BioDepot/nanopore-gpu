#!/bin/bash

echo "guppy_basecaller $@"
SECONDS=0
guppy_basecaller $@
echo "$SECONDS for basecalling"
rootname=$(basename $savepath)
mkdir -p $fastqdir
if [ -z $compressed ]; then
	echo "cat $savepath/pass/* > $fastqdir/$rootname.fastq"
	cat $savepath/pass/* > $fastqdir/$rootname.fastq
else
	echo "cat $savepath/pass/* > $fastqdir/$rootname.fastq.gz"
	cat $savepath/pass/* > $fastqdir/$rootname.fastq.gz
fi
echo "$SECONDS for fastq generation"
