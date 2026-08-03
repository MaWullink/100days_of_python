class FlightData:

    def __init__(self, price, origin, destination, out_date, return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data, return_date):

    if data is None:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    if not all_flights:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = all_flights[0]

    cheapest_flight = FlightData(
        first_flight["price"],
        first_flight["flights"][0]["departure_airport"]["id"],
        first_flight["flights"][-1]["arrival_airport"]["id"],
        first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0],
        return_date
    )

    lowest_price = first_flight["price"]

    for flight in all_flights:

        if "price" not in flight:
            continue

        if flight["price"] < lowest_price:
            lowest_price = flight["price"]

            cheapest_flight = FlightData(
                flight["price"],
                flight["flights"][0]["departure_airport"]["id"],
                flight["flights"][-1]["arrival_airport"]["id"],
                flight["flights"][0]["departure_airport"]["time"].split(" ")[0],
                return_date
            )

    return cheapest_flight