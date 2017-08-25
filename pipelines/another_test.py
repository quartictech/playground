from quartic import step, writer


@step
def step1(a_new_test: "new_input") -> "new_output":
    return writer("Something", "Something").json({})

@step
def step2(test2: "new_output") -> "output2":
    return writer("Something else", "something else").json({})
