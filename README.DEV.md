# Requeriment System

- Linux Ubuntu 19.10, Windons 10
- Python 3.7
- Java 7
- Anaconda

# Create projects dev

    $ conda create --name checkpoint python=3.7

### To activate this environment, use

    $ conda activate checkpoint

### To deactivate an active environment, use

    $ conda deactivate

### Python create requirements txt

    $ pip freeze > requirements.txt

    $ export FLASK_ENV=development
    $ export FLASK_ENV=production
    
    $ flask run

# Create Executable Appp
## Stap 01

Install Compiler [Py2Exe](https://wiki.python.org.br/Py2ExeSimples)

    $ pip install py2exe

Build Run

    $ python make.py run.py

The .EXE file will be saved in the DIST folder.

## Stap 02
### Used [Inno Setup](http://www.jrsoftware.org/isinfo.php)