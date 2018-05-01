FORMULAS_PATH = "formulas.txt"

file = open(FORMULAS_PATH, "r")

print(file.read())
file.seek(0)
lines = file.readlines()
file.seek(0)

section_starts = []
formulas = []
formula_indexs = []

print(lines)
for index, line in enumerate(lines):
  if line.startswith("#"):
    section_starts.append(index)
  elif index-1 >= 0 and index+1 <= len(lines):
    if lines[index-1].startswith("{") and lines[index+1].startswith("}"):
      formulas.append(line)
      formula_indexs.append(index)


formulas = list(map(lambda x: x[:-1], formulas))


print(section_starts)
print(formulas)
print(formula_indexs)

def read_formula(formula):
  
  out_name, formula_ = formula.split("=")
  
  front_bracket = None
  back_bracket = None
  
  vars_ = []
  
  for ind, char in enumerate(list(formula_)):
    if front_bracket == None and char == "<":
      front_bracket = ind
    
    if back_bracket == None and front_bracket != None and char == ">":
      back_bracket = ind
      vars_.append(formula_[front_bracket+1:back_bracket])
      back_bracket, front_bracket = None, None
  
  return parsed_formula

print(read_formula(formulas[0]))
print(read_formula(formulas[1]))
