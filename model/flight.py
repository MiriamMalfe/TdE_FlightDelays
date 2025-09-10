from dataclasses import dataclass
from datetime import date


@dataclass
class Flight:
    ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    TAIL_NUMBER: str
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    SCHEDULED_DEPARTURE_DATE: date
    DEPARTURE_DELAY: int
    ELAPSED_TIME: int
    DISTANCE: int
    ARRIVAL_DATE: date
    ARRIVAL_DELAY: int

    def __hash__(self):
        return self.ID
    def __str__(self):
        return self.ID
    def __eq__(self, other):
        return self.ID==other.ID
