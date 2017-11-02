from quartic import step, writer
for ds in ['employees', 'employees_surname', 'employees_address']:
    @step
    def clean(in1: ds) -> "clean_{}".format(ds):
        df = in1.reader().csv()
        df_lower = df.apply(lambda x: x.astype(str).str.lower())
        return writer("Cleaned table {}".format(ds)).parquet(df_lower)
    