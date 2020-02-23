# CheckPoint

## Read Documentation

    checkpoint$ pip install mkdocs
    checkpoint$ mkdocs serve
    Browser Connected: http://127.0.0.1:8000/

# Err
OSError: [Errno 98] Address already in use

    $ sudo lsof -t -i tcp:9999 | xargs kill -9
