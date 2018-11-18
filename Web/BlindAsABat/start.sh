#!/bin/bash

cd /${NAME}
gunicorn -b 0.0.0.0:${PORT} -w 8 app:app 0.0.0.0 ${PORT} &
