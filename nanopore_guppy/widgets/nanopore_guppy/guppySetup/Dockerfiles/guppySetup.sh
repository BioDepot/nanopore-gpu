#!/bin/bash
build(){
  if [ -n "$overwrite" ]; then 
    echo  "Will overwrite existing image"
    echo "docker build -t biodepot/guppy:gpu -f Dockerfile-$1 --build-arg gpu_url=$gpu_url ." && docker build -t biodepot/guppy:gpu -f Dockerfile-gpu --build-arg gpu_url=$gpu_url . && echo "build successfully" && return 0
  elif [ docker image inspect biodepot/guppy:gpu >/dev/null 2>&1 ]; then 
	echo "image exists - will not build unless overwrite flag is set" && return 0
  else
	echo "no existing image - will build"
	docker build -t biodepot/guppy:gpu -f Dockerfile-gpu --build-arg gpu_url=$gpu_url . && echo "build successfully" && return 0
  fi
  return 1
}
[ -n "$gpu_url" ] && echo "checking if we need to build gpu guppy" && build gpu || exit 1
