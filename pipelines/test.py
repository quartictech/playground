from quartic import step, writer
from pipelines.noob.test import *

print("YES")

@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})

@step
def step2(test2: "output") -> "input":
    return writer("Something else", "something else").json({})
