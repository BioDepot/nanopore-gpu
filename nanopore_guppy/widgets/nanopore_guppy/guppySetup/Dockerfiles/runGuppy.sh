#!/bin/bash
shopt -s extglob
runJob(){
 savepath=$(makeSavePath $1)
 local args=("-i $1 -s $savepath ${inputArgs[@]}")
 start=$(date +%s.%N)
 mkdir -p $savepath 
 guppy_basecaller ${args[@]}
 callTime=$(date +%s.%N)
 rootname=$(basename $savepath)
 mkdir -p $fastqdir
 local filelist=($(find $savepath/pass -type f))
 [ ${#filelist[@]} -eq 0 ] && echo "no reads mapped" && return 1
 echo "concatenating reads ${filelist[@]}"
 if [ -z $compressed ]; then
	cat "${filelist[@]}" > $fastqdir/$rootname.fastq
 else	
	cat "${filelist[@]}" > $fastqdir/$rootname.fastq.gz 
 fi
 finishTime=$(date +%s.%N)
 callDiff=$(echo "$callTime - $start" | bc)
 finishDiff=$(echo "$finishTime - $start" | bc)
 echo "$callDiff seconds used for basecalling "
 echo "$finishDiff sedonds used for basecalling "
}
makeArrayString() {
	echo $1 | sed 's/[][]//g' | sed 's/\,/ /g' | sed 's/\"//g'
}
makeSavePath() {
	echo "$outputDir/$(basename $1)"
}
set -euf -o pipefail
mkdir -p $outputDir
inputDirsArray=($(makeArrayString $inputDirs))
inputArgs=("$@")  
for inputDir in "${inputDirsArray[@]}"; do
	runJob $inputDir
done
exit 0
