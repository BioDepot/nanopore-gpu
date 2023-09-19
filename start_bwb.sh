#!/bin/bash 

docker run -p 6080:6080 -v /root:/data -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/.X11-unix:/tmp/.X11-unix biodepot/bwb:latest
