#!/bin/bash

echo "guppy_basecaller $@"
guppy_basecaller $@

rootname=$(basename $savepath)
mkdir -p $fastqdir
if [ -z $compressed ]; then
	echo "cat $savepath/pass/* > $fastqdir/$rootname.fastq"
	cat $savepath/pass/* > $fastqdir/$rootname.fastq
else
	echo "cat $savepath/pass/* > $fastqdir/$rootname.fastq.gz"
	cat $savepath/pass/* > $fastqdir/$rootname.fastq.gz
fi

