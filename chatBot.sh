#!/bin/bash

case "$1" in
  "train")
    # run training script
    python scripts/train.py
    ;;
  "start")
    # Start the server
    gunicorn --bind 0.0.0.0:8000 run:app
    ;;
  "serve")
    # Open http://127.0.0.1:8000/ in default browser
    python -m webbrowser http://127.0.0.1:8000/

    # Start the server
    gunicorn --bind 0.0.0.0:8000 run:app
    ;;
  *)
    printf "invalid / insufficient argument. \n \
          1. ./chatBot.sh train - start training \n \
          2. ./chatBot.sh start - start the server \n \
          3. ./chatBot.sh serve - start server & open browser \n"
    ;;
esac
