class SkyScanner:
    def searchFlights(self,source,destination):
        noOfFlights=1
        nameOfAirlines="Indigo"
        return "No of flights is",noOfFlights,"and name of airlines is",nameOfAirlines
s=SkyScanner()
#Option 1 of capturing data from return
flightInfo=s.searchFlights("Bangkok","Banglore")
print(flightInfo)

#Option 2 of capturing data from return
print(s.searchFlights("Hydrabad","Banglore"))




