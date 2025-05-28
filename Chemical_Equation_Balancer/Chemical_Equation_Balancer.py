# Creat lists of reactant and product molecules

numR = int(input('How many reactant molecules? --> '))
numP = int(input('How many product molecules? --> '))

R, P = [], []
for i in range(numR):
    R.append(str(input(f'Chemical formula of reactant molecule {i+1} --> ')))
for i in range(numP):
    P.append(str(input(f'Chemical formula of product molecule {i+1} --> ')))


# Create dictionaries containing the number of atoms for each element in a molecule

import re

def create_dict(mol_list, mol_dict):
    atom_list = []
    for molecule in mol_list:
        if '(' in molecule:
            bracket = re.findall('\(\w+\)\d+', molecule)[0]
            bracket_subsc = int(re.findall('\d+', bracket)[-1])
            in_bracket = re.findall('[A-Z][a-z]?\d*', bracket)
            for i in range(len(in_bracket)):
                if any(char.isdigit() for char in in_bracket[i]) == True:
                    subscript = int(re.findall('\d+', in_bracket[i])[0])
                    in_bracket[i] = re.sub('\d+', str(subscript * bracket_subsc), in_bracket[i])
                else:
                    in_bracket[i] += str(bracket_subsc)
            molecule = molecule.replace(bracket, ''.join(in_bracket))
            
        atom_list += [re.findall('[A-Z][a-z]?\d*', molecule)]
    
    for i in range(len(mol_list)):
        dicti = mol_dict[i]
        for atom in atom_list[i]:
            element = re.findall('[A-Za-z]+', atom)[0]
            if any(char.isdigit() for char in atom) == True:
                subscript = int(re.findall('\d+', atom)[0])
                dicti[element] = dicti.get(element, 0) + subscript
            else:
                dicti[element] = dicti.get(element, 0) + 1
    
    return mol_dict

reactants, products = [{} for i in range(len(R))], [{} for i in range(len(P))]
create_dict(R, reactants)
create_dict(P, products)


# Summarize the occurrence of each element in the unbalanced equation

elements = set()
for molecule_dict in (reactants + products):
    for key in molecule_dict.keys():
        elements.add(key)

sub = {key:[] for key in elements}
for key in sub.keys():
    for molecule_dict in reactants:
        if key in molecule_dict.keys():
            sub[key].append(molecule_dict.get(key))
        else:
            sub[key].append(0)
    for molecule_dict in products:
        if key in molecule_dict.keys():
            sub[key].append(-molecule_dict.get(key))
        else:
            sub[key].append(0)


# Find the coefficients

import random as rd

def rd_coeff(length):
    rd_set = []
    for i in range(length):
        rd_set.append(rd.randint(1,20))
    return rd_set

while True:
    coeff = rd_coeff(numR+numP)
    summations = []
    for value in sub.values():
        summation = sum(list(a*b for a, b in zip(value, coeff)))
        summations.append(summation)
    if summations == [0]*len(sub):
        break

GCD = 1  # Greatest Common Divisor
for i in range(1, min(coeff)+1):
    if [j % i for j in coeff] == [0]*len(coeff):
        GCD = i
coeff = [i // GCD for i in coeff]


# Print the balanced equation

def write_eq(start, end, comp, coeff):
    eq = ''
    for i in range(start, end):
        if coeff[i] == 1:
            eq += (comp[i] + ' + ')
        else:
            eq += (str(coeff[i]) + ' ' + comp[i] + ' + ')
    return eq[:-3]

equation = write_eq(0, len(R), R, coeff) + ' = ' + write_eq(len(R), len(R+P), R+P, coeff)

print(equation)