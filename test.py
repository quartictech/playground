import sys
from quartic import step, writer

print("Generating...")
print("Some error...", file=sys.stderr)
@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})
