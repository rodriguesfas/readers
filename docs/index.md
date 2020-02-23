# Welcome to CheckPoint

Is a Python library to interface with RFID readers. It is a pure-Python implementation of the Low Level Reader Protocol (LLRP) by [sllurp](https://github.com/EMS-TU-Ilmenau/sllurp).

These readers are known to work well with sllurp, but it should be adaptable with not much effort to other LLRP-compatible readers:

- Impinj Speedway (R1000)
- Impinj Speedway Revolution (R220, R420)
- Impinj Speedway xPortal
- Motorola MC9190-Z (handheld)

<img src="http://127.0.0.1:8000/assets/img/leitor_impinj_speedway_r420.jpg">

## Architecture

<img src="http://127.0.0.1:8000/assets/img/architecture.png">

- <b>GUI</b>: Graphical user interface.
- <b>CLI</b>: Command line interface.
- <b>Collector</b>: Module that connects to the RFID reader and reads the read tags in the database.
- <b>Audit</b>: Module for auditing data.
- <b>MongoDB</b>: Document oriented database.

## Features
- Import Tag registration.
- Performs RFID Tag readings.
- Conducts Tag inventories.
- Exporta relatorio de Tag.

## Licence

GNU General Public License - 2019.