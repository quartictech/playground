from quartic import step, writer
from quartic.incubating import raw, FromBucket

@raw
def register() -> "first_input":
    return FromBucket("quartic-employees.csv", name="Quartic employees list")