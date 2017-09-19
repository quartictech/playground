from quartic import step, writer
import pandas as pd

@step
def join(in1: "employees", in2: "employees_surname", in3: "employees_address") -> "employees_joined":
    employees = pd.read_csv(in1)
    emp_surnames = pd.read_csv(in2)
    emp_addresses = pd.read_csv(in3)

    merged = employees.merge(emp_surnames, on="Name").merge(emp_addresses, on="Name")

    return writer("Quartic employees table", "Parquet file of merged employees data.").parquet(merged)
