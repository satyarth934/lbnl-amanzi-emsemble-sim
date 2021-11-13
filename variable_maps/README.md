# File formats of variable maps

Variable map YAML files are accepted in either of the following formats:

## Format 1

Range values for the variable

Example file:
```
"@Perm@": 
  low:  5e-12*0.8
  high: 5e-12*1.2

"@Por@": 
  low: 0.39*0.8
  high: 0.39*1.2
```

## Format 2

Single values for the variable

Example file:
```
"@Perm@": 
- 5e-12*0.8

"@Por@": 
- 0.39*0.8
```

## Format 3

Multiple values for the variable

Example file:
```
"@Perm@": 
- 5e-12*0.8
- 5e-12*1.2

"@Por@": 
- 0.39*0.8
- 0.39*1.2
```

A combination of the three can also be used to define values for the variables.
When multiple values are provided for one or more variables, all permutations are considered for the simulations.
