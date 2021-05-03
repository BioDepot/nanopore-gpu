#!/bin/bash
build(){
  [ -n "$overwrite" ] || docker image inspect biodepot/guppy:gpu >/dev/null 2>&1 && return 0
    echo  "docker build -t biodepot/guppy:gpu -f Dockerfile-$1 --build-arg gpu_url=$gpu_url ." && docker build -t biodepot/guppy:gpu -f Dockerfile-gpu --build-arg gpu_url=$gpu_url .
}
[ -n "$gpu_url" ] && echo "building gpu guppy" && build gpu || exit 1
