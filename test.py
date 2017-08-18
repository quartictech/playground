from quartic import step, writer

print("Generating...")
@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})
