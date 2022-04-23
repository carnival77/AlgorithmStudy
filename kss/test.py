import pdb
import latex2mathml.converter
pdb.set_trace()
inp = "f:V\to Z"
output = latex2mathml.converter.convert(inp)
print(output)
