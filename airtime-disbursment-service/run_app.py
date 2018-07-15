from service import Service

airtime_service = Service()

if __name__ == "__main__":
    # initialize the airtime disbursmet service
    airtime_service.init_service()
    # run the airtime disbursment service
    airtime_service.send_airtime()