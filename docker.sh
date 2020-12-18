#!/bin/sh

set -e

NAME=doc-tower

case "$1" in
  build)
    docker build --tag ${NAME} .
    ;;
  clean)
    docker run --name ${NAME} --rm -it -v $(pwd):/doc ${NAME} clean
    ;;
  generate)
    docker run --name ${NAME} --rm -it -v $(pwd):/doc ${NAME} generate
    ;;
  serve)
    docker run --name ${NAME} --rm -it -v $(pwd):/doc -p 5500:5500 -e LR_HOST=0.0.0.0 ${NAME} serve
    ;;
  *)
    >&2 echo "Unknown command"
    ;;
esac
