from quartic import step, writer


@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})

@step
def step2(test2: "output") -> "output2":
    return writer("Something else", "something else").json({})
