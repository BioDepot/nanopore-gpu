#!/bin/bash
echo "$@"
[ -f $outputfile ] && [ -z $overwrite ] && echo "index $outputfile already exists" && exit 0
echo "minimap2 -x map-ont $@ "
minimap2 -x map-ont $@

