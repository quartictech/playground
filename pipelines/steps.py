from quartic import step, writer

@step
def join(in1: "employees", in2: "employees_surname", in3: "employees_address") -> "employees_joined":
    #get dataframes and join them
    employees = in1.reader().csv()
    emp_surnames = in2.reader().csv()
    emp_addresses = in3.reader().csv()

    merged = employees.merge(emp_surnames, on="Name").merge(emp_addresses, on="Name")

    return writer("Quartic employees table", "Parquet file of merged employees data.").parquet(merged)
