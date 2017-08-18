import sys
from quartic import step, writer

print("Generating...")
print("Some error...", file=sys.stderr)

something_is_wrong
@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})
