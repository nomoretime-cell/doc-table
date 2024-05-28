#!/bin/bash

latest_tag=$(git describe --tags --abbrev=0)
module_name=doc-table

docker run \
  -d -it \
  -e WORKER_NUM=2 \
  -p 8003:8003 \
  --name ${module_name} \
  ${module_name}:${latest_tag}
