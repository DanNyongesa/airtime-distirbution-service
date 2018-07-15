from service import Service

airtime_service = Service()

if __name__ == "__main__":
    # initialize the airtime disbursmet service
    airtime_service.init_service(api_key='34ff6792bc73f2ac02db08d8dc667b79f64cd127b3519b1a117002751fabee6f')
    # run the airtime disbursment service
    airtime_service.send_airtime()
    # airtime_service.parse_csv()