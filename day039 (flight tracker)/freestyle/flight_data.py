from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class FlightData:
    origin: str
    destination: str
    outbound_date: date
    return_date: date
    price: float
    currency: str
    duration_minutes: int
    stops: int
    airlines: tuple[str, ...]
    price_level: str | None = None
    typical_low: float | None = None
    booking_token: str | None = None

    @property
    def route_key(self):
        return f"{self.origin}-{self.destination}-{self.outbound_date}-{self.return_date}"

    @property
    def score(self):
        discount = 0.0
        if self.typical_low and self.typical_low > 0:
            discount = max(0.0, (self.typical_low - self.price) / self.typical_low * 100)
        level_bonus = {"low": 20, "typical": 0, "high": -20}.get(
            (self.price_level or "").lower(), 0
        )
        return round(discount + level_bonus - self.stops * 12 - self.duration_minutes / 120, 1)

    @property
    def duration_label(self):
        hours, minutes = divmod(self.duration_minutes, 60)
        return f"{hours}h {minutes:02d}m"

    def alert_message(self):
        stops = "direct" if self.stops == 0 else f"{self.stops} stop{'s' if self.stops != 1 else ''}"
        usual = f" Typical fares start near {self.typical_low:.0f} {self.currency}." if self.typical_low else ""
        return (
            f"Weekend escape: {self.origin} -> {self.destination}\n"
            f"{self.outbound_date:%d %b} - {self.return_date:%d %b} | {self.price:.0f} {self.currency}\n"
            f"{stops}, {self.duration_label} | {', '.join(self.airlines)}."
            f"{usual} Deal score: {self.score:.1f}"
        )
