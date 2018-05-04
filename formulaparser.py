FORMULAS_PATH = "formulas.txt"

file = open(FORMULAS_PATH, "r")

file = open("formulas.txt", "r")

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
  
  consts_ = []
  consts_use = {}
  
  for ind, char in enumerate(list(formula_)):
    if front_brackaet == None and char == "{":
      front_bracket = ind
    
    if back_bracket == None and front_bracket != None and char == "}":
      back_bracket = ind
      consts_.append(formula_[front_bracket+1:back_bracket])
      back_bracket, front_bracket = None, None
  
  print(consts_)
  if "pi" in consts_:
    consts_use["pi"] = 3.1415926535
  
  # for const_ in consts_:
    # if const_ in CONSTS.keys:
      
  
  def formula_calc(**kwargs):
    kwargs.update(consts_use)
    print(kwargs)
    print(formula_)
    return eval(formula_.format(**kwargs))
  
  formula_calc.__name__ = out_name
  
  return formula_calc

# print(read_formula(formulas[0])(W=5, L=5))
# print(read_formula(formulas[1])(W=5, L=5))


# circlearea = read_formula(formulas[2])
# print(circlearea(r=4))

# sphere_volume = read_formula(formulas[3])
# print(sphere_volume(r=4))

# randoms = read_formula(formulas[4])
# print(randoms(x=9.5))

