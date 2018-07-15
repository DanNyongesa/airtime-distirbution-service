# AIRTIME DISBURSMENT SERVICE

A program that uses [AfricasTalking APIs](http://docs.africastalking.com/) to send Airtime to recipients.
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
Add the csv file under the `airtime-disbursment-service/assets/` directory and set its file name so that our program can pick it up
```bash
$ export CSV_FILENAME=your_csv_filename.csv
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

Sample Expected output
```bash
2018-07-15 20:13:17,986 - root - INFO - Invalid amount 1oo
2018-07-15 20:13:17,986 - root - INFO - Invalid amount 6Y8
2018-07-15 20:13:19,356 - root - INFO - received 9 responses
2018-07-15 20:13:19,356 - root - INFO - {'phoneNumber': '+254700888932', 'errorMessage': 'None', 'amount': 'KES 38.6700', 'status': 'Sent', 'requestId': 'ATQid_593abf827d8f6c653cd69812531414f1', 'discount': 'KES 1.5468'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700767876', 'errorMessage': 'None', 'amount': 'KES 666.0000', 'status': 'Sent', 'requestId': 'ATQid_9e3f1d1914cbbd72c95b74d55f833007', 'discount': 'KES 26.6400'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700555444', 'errorMessage': 'None', 'amount': 'KES 78.7800', 'status': 'Sent', 'requestId': 'ATQid_f73bf88bbc4a695779c8788189aa7326', 'discount': 'KES 3.1512'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700888222', 'errorMessage': 'None', 'amount': 'KES 38.6700', 'status': 'Sent', 'requestId': 'ATQid_bbd4d7c19b26c12bc1e5dadd9e5c1509', 'discount': 'KES 1.5468'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700333444', 'errorMessage': 'None', 'amount': 'KES 455.0000', 'status': 'Sent', 'requestId': 'ATQid_76473583d556d15e9fd54e9c81ddaacd', 'discount': 'KES 18.2000'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700111222', 'errorMessage': 'None', 'amount': 'KES 35.0000', 'status': 'Sent', 'requestId': 'ATQid_a77d735c44b52072b9f287aced498310', 'discount': 'KES 1.4000'}
2018-07-15 20:13:19,357 - root - INFO - {'phoneNumber': '+254700123456', 'errorMessage': 'None', 'amount': 'KES 250.0000', 'status': 'Sent', 'requestId': 'ATQid_c76401286cfbdea1289a0e1e44a00d7f', 'discount': 'KES 10.0000'}
2018-07-15 20:13:19,358 - root - INFO - {'phoneNumber': '+254700666434', 'errorMessage': 'Value Outside The Allowed Limits', 'amount': 'KES 20000.0000', 'status': 'Failed', 'requestId': 'None', 'discount': '0'}
2018-07-15 20:13:19,358 - root - INFO - {'phoneNumber': '+254700343222', 'errorMessage': 'Value Outside The Allowed Limits', 'amount': 'KES 12500.0000', 'status': 'Failed', 'requestId': 'None', 'discount': '0'}
2018-07-15 20:13:19,358 - root - INFO - Successfull 7 Failed 2

```

## Running the tests

### Unittests

Activate your virtual environment
```bash
$ source .venv/bin/activate
```
cd into the projects directory
```bash
$ cd jumo-interview/airtime-disbursment-service
```
Run
```bash
$ python -m unittest
```

## Doctest

Activate your virtual environment
```bash
$ source .venv/bin/activate
```
cd into the projects directory
```bash
$ cd jumo-interview/airtime-disbursment-service
```
Run
```bash
$ python service.py -v
```

## Built With

* [Python 3.6](https://docs.python.org/3.6/)

## Authors

* **Pius Dan Nyongesa**
