from quartic import step, writer

@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})
