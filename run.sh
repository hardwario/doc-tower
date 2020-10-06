#!/bin/sh

set -e

case "$1" in
  clean)
    make clean
    ;;
  generate)
    make html
    ;;
  serve)
    python serve.py
    ;;
  *)
    >&2 echo "Unknown command"
    ;;
esac
