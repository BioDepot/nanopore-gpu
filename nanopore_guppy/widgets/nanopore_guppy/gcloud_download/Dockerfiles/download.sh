#!/bin/bash

bucket=$1
outputDir=$2
err=0

# Set gsutil default command line options
cmd="gsutil -m cp "
# Append option to not overwrite files if set
[ -n "$noClobber" ] && cmd+="-n"

function gcloud_download() {
	local cmd="$1"
	echo $cmd
	$cmd
	return $?
}

if ! gsutil -q ls gs://${bucket}/ &>/dev/null; then
	echo "cannot find cloud directory ${bucket}"
	exit -1
fi

mkdir -p $outputDir

# Check if user passed directories to download
if [ -z $DIRS ]; then
	echo "no directories to download"
elif [ "$DIRS" == "[]" ] && [[ $(gsutil ls gs://${bucket}) ]]; then
	echo "downloading the entire bucket $bucket"
	gcloud_download "$cmd -r gs://${bucket}/* $outputDir/." || err=$?
else
	darray=( $(echo $DIRS | jq -r '.[]') )
	if [ -z $darray ]; then
		echo "cannot parse $DIRS"
		err=-1
	else
		for d in "${darray[@]}"; do
			if gsutil -q ls gs://${bucket}/${d} &>/dev/null && [[ $(gsutil ls gs://${bucket}/${d}) ]]; then
				echo "downloading ${bucket}/${d}"
				gcloud_download "$cmd -r gs://${bucket}/${d}/* $outputDir/." || err=$?
			else
				echo "cannot find or cannot access ${bucket}/${d}"
				err=-1
			fi
		done
	fi
fi
# Check if user passed files to download
if [ -z $FILES ]; then
	echo "no files to download"
else
	echo $FILES
	farray=( $(echo $FILES | jq -r '.[]') )
	if [ -z $farray ]; then
		echo "cannot parse $FILES"
		err=-1
	else
		for f in "${farray[@]}"; do
			if gsutil -q ls gs://${bucket}/${f} &>/dev/null; then
				echo "downloading ${bucket}/${f}"
				gcloud_download "$cmd gs://${bucket}/${f} $outputDir/." || err=$?
			else
				echo "cannot find or cannot access ${bucket}/${f}"
				err=-1
			fi
		done
	fi
fi

exit $err
