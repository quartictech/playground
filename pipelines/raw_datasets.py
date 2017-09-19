from quartic import step, writer
from quartic.incubating import raw, FromBucket

@raw
def register() -> "employees":
    return FromBucket("quartic-employees.csv", name="Quartic employees list")

@raw
def register() -> "employees_surname":
    return FromBucket("employees_surnames.csv", name="Quartic employees surnames")

@raw
def register() -> "employees_address":
    return FromBucket("employees_address.csv", name="Quartic employees address")