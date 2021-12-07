# DG - A(n) (unusual) programming language

## General structure
- There are no infix-operators (i.e. 1 **+** 1)
- Each operator takes 2 parameters
- When there are more than 2 parameters required, they will be listed by ","
- Code is interpreted line by line
- There must not be blank lines
- Any character that isn't an operator starts a comment (";" is the only one that I can guarantee will stay a comment going forward)

## Syntax
A line followes the general structure `[operator] [first parameter] [second parameter]`
### Operators
| Operator | Description | Syntax |
| ----------- | ----------- | --------|
| v | set variable | `s x 15` [also `s a x` (sets a to 15)] |
| v | make an array | `s b []` |
| v {o} | sets variable to output of equation | `s c o / 1 2` [sets var c to 1 / 2; if `s c o * 3 4` c = 12] |
| + | adds to numbers (only used to set variables) | `v e o + 1 2` |
| - | subtracts to numbers (only used to set variables) | `v e o - 1 2` |
| * | multiplies to numbers (only used to set variables) | `v e o * 1 2` |
| / | divides to numbers (only used to set variables) | `v e o / 1 2` |
| % | modulo of to numbers (in this case used to set variables) | `v e o % 8 3` |
| g | gets element of array and writes to variable | `v e o g b 0` |
| p | prints variable | `p "x: {}, a: {}" x,a` [[see rusts println!](https://doc.rust-lang.org/std/macro.println.html)] |
| a | append to array | `a b 15` [b = [15]] |
| s | sets element in array | `s b 0,12` [b = [12]] |
| g | get element in b | `g b 0` [prints 12] |
| ; | comment | `; I'm a comment`
| > | executes if condition is true | `> x 1 v e o / 1 x` [if x > 1, e will be set to 1 / x] |
| < | executes if condition is true | `< x 1 v e o / 1 x` [if x < 1, e will be set to 1 / x] |
| = | executes if condition is true | `= x 1 v e o / 1 x` [if x == 1, e will be set to 1 / x] |
| ! | executes if condition is true | `! x 1 v e o / 1 x` [if x != 1, e will be set to 1 / x] |
| l | basic for loop | `l 1,10,2 i&v z o / 1 i&p "i:{} z:{} i,z"` [for i from 1 to 9 in steps of 2 (1, 3, 5, etc.) set z = 1/i and print i,z. **BEFORE AND AFTER THE "&" MUST NOT BE A SPACE**] |
