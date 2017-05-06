# Static Semantics

## Intro
---

Static semantics is broadly any requirements imposed at compile time for the program to be considered "good" or "well formed". Stuff like "variables have to be defined before they are used" is static semantics. This is stuff we can't enforce with a CFG and thus we need to have the step of semantic analysation via a semantic analyser. 

The semantic analyser enforces a languages semantic constraints. there are two types of constraints

1. Scope Rules
2. Type Rules

And the semantic analysis happens in 2 phases
1. Identification (symbol table)
2. Type checking

All stuff we have dealt with before in programming. 
Our assignment 4 uses 1 pass to do both these steps and esstentially is a type checker. 

## Blocks
---

A Block is a language construct that can contain declerations for example

- the compilation units (code files)
- Procedures and functions and methods
- compound statements

It's basically just any section of code that has a distinct scope. 

Within VC we have 2 block types

1. the entire program (i.e the outermost block)
2. compound statements, anything within curly braces `{ ... }`





