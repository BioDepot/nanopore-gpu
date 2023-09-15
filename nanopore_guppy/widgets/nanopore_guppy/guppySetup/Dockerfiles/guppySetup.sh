#!/bin/bash
dockerbuild(){
    if [ -n "$CUDA_VERSION" ]; then
      echo "docker build -t biodepot/guppy:gpu -f Dockerfile-gpu  --build-arg CUDA_VERSION=$CUDA_VERSION --build-arg gpu_url=$gpu_url ."
      docker build -t biodepot/guppy:gpu -f Dockerfile-gpu  --build-arg CUDA_VERSION=$CUDA_VERSION --build-arg gpu_url=$gpu_url .
    else
      echo "docker build -t biodepot/guppy:gpu -f Dockerfile-gpu --build-arg gpu_url=$gpu_url ."
	    docker build -t biodepot/guppy:gpu -f Dockerfile-gpu --build-arg gpu_url=$gpu_url .
    fi
}
build(){
  if [ -n "$overwrite" ]; then 
    echo  "Will overwrite existing image"
    dockerbuild && echo "built successfully" && return 0
  elif [ docker image inspect biodepot/guppy:gpu >/dev/null 2>&1 ]; then 
	  echo "image exists - will not build unless overwrite flag is set" && return 0
  else
	  echo "no existing image - will build"
    dockerbuild && echo "built successfully" && return 0
  fi
  return 1
}
[ -n "$gpu_url" ] && echo "checking if we need to build gpu guppy" && build || exit 1
