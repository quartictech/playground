from quartic import step, writer

@step
def join(in1: "clean_employees",
         in2: "clean_employees_surname",
         in3: "clean_employees_address") -> "employees_joined":
    #get dataframes and join them
    employees = in1.reader().parquet()
    emp_surnames = in2.reader().parquet()
    emp_addresses = in3.reader().parquet()

    merged = employees.merge(emp_surnames, on="Name").merge(emp_addresses, on="Name")

    return writer("Quartic employees table", "Parquet file of merged employees data.").parquet(merged)