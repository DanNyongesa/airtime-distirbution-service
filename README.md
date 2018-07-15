# AIRTIME DISBURSMENT SERVICE

A program thatutilizes [AfricasTalking APIs](http://docs.africastalking.com/) to send Airtime to recipients.
The program takes a CSV file as input

### Example CSV file

| Employee-Name | Phone-Number | Amount  |
| --- | --- | --- |
|kiriamiti | 254700123456 | 250 |
| Meja Mwangi | 254700111222 | 35 |
| Marjorie Oludhe Macgoye | 254700333444 | 455 |
| Miguna Miguna | 254700888222 | 38.67 |
| Yvonne Adhiambo | 254700555444 | 78.78 |

## Getting Started

Cd into the airtime-disbursment-service drectory
```bash
$ cd airtime-disbursment-service
```
Add running permission to the runner script
```bash
$ chmod +x ./run.sh
```
Run the program
```bash
$ ./run.sh
```
### Prerequisites

A working Linux installation (You can also use windows though a linux distro is highly recommended) 
A working version of python>=3.6

```bash
# on linux
$ sudo apt-get update
$ sudo apt-get install python3.6
```

### Installation

Assuming you have downloaded the program into a directory of your choice
Cd into the jumo-interview directory
```bash
$ cd jumo-interview
```
Create your project's virtual environment
```bash
$ python3 -m venv .env
```
Activate the virtual environment
```bash
$ source .venv/bin/activate
```
Add running permission to the runner script
```bash
$ chmod +x ./run.sh
```
Provide your [AfricasTalking API key and Username](http://docs.africastalking.com/)
```bash
$ export AT_APIKEY=my_africastalking_api_key
$ export AT_USERNAME=my_africastalking_username

```
Run the program
```bash
$ ./run.sh
```

Expected output
```bash

```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Python 3.6](https://docs.python.org/3.6/)

## Authors

* **Pius Dan Nyongesa**
