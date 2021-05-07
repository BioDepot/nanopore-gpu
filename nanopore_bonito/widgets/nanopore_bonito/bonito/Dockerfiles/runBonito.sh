#!/bin/bash
set -euf -o pipefail
mkdir -p $outputDir

runJob(){
 start=$(date +%s.%N)
 savepath=$(makeSavePath $1)
 echo "bonito basecaller ${inputArgs[@]} $modelname $1 > $savepath"
 bonito basecaller ${inputArgs[@]} $modelname $1 > $savepath
 callTime=$(date +%s.%N)
 finishTime=$(date +%s.%N)
 callDiff=$(echo "$callTime - $start" | bc)
 echo "$callDiff seconds used for basecalling "
}
makeArrayString() {
	echo $1 | sed 's/[][]//g' | sed 's/\,/ /g' | sed 's/\"//g'
}
makeSavePath() {
	echo "$outputDir/$(basename $1).fastq"
}

mkdir -p $outputDir
inputDirsArray=($(makeArrayString $inputDirs))
inputArgs=("$@")
printenv
echo "${inputArgs[@]}"
for inputDir in "${inputDirsArray[@]}"; do
	runJob $inputDir
done
exit 0
