## QUESTIONS
---

1. WHY BOTHER FORMING A DFA FROM A NFA RATHER THEN DIRECTLY / WHY NOT USE A NFA

2. Whats up with Chomsky’s Hierarchy????


## EXAM PLAN
---

1. revise lectures
2. revise assignment code + tutorial questions
3. extra

## Intro
---

The only part of the compiler that needs to know the arcitecture of the machine it's compiling for is the Code generation step. 

retargetable compilers run off the idea that multiple different languages can be compiled into the same IR using multiple front ends. Once in this form you can use generic IR optimization tools and then feed this ir into different back ends depending on the system. 

M languages + N architectures -> M frontends + N backends

not MN frontends + NN backends

## Lexical Analysis
---

Tokens are just a basic unit of syntax, a token in the enlish language is a word for example. 

a lexeme is the actual text forming a token, known to be a `instance` of a token. 

Note tokens can also have attributes which basically just describe the tokens value for later steps. 

Tokenisation is done by the lexer usually through regex or other patterns. 
Note that if a token begings to get matched but doesn't get fully matched (like a string with no terminating double quote) this can be raised as a lexical error. 

some lexical errors stop the compiler because they are unrecoverable (like a open comment with no close) whereas other's can be recovered from by going to the next white space / new line. 

note the only difference between Kleene Closure and Positive closure is that postive closure can't have the empty string. Note that L^3 is a klene closure with a set limit, as in L* but rather then ANY amount of L we only have no L, one L, LL, or LLL. 

remember that a Language is a set of Strings in a certain alphabet. further note with RE * has the highest precendence followed by concatentation and "|". Stating this lets us take out brackets. 

A|B*C is the same as (A)|(B\*C) NOT (A|B)\*C as the \* attaches to the B first, then the C attaches to the B\* and that whole stement attaches to the A via |

a Finate State Automata is in essence just a way to represent a machine/automata/system which has a finite number of states and a fixed set of ways to transition between those state. for ys it lets us define symbols in a alphabet and how you can transition from one to another. 

in a DFA every input causes a state change. You can convert RE into NFA's through a series of ways, One of those ways is Thompsons construction. This method is syntax driven, Inductive, and important.

Inductive just means the cases in the construction of the NFA follow the cases in the definition of REs and important means that if a symbol occurs several times in a RE , a separate NFA is constructed for each occurrence

## Syntax analysis
---

this is the parser, it groups tokens together into gramatical phrases. YOu can do this in many ways but representing this grouping as a AST is quite effective and common. 

Because the pardsr works off a grammar it can correct errors and give meaningful error messahes about how the statement was structured rather then why it doesn't translate into machine code. 

this thens feeds into the symantic analyser (the recogniser) which does type checking and makes sure the ast is valid given the language constraints. 

For programming languages semantics can be split into two parts

Static Semantics is context-sensitive restrictions enforced at compile-time stuff like all identifiers declared before use, assignment must be type-compatible etc. 

Run Time Semantics is what the program does or computes, i.e the meaning of a program or what happens when it is executed. Is specified by code generation routines.

syntax-directed translation is where a grammar is defined in a way that we can skip every step after the parser and go straight to code generation. 

note that context free grammars and context sensitive grammars are different because in a context free grammar the left side must be a single non terminal. 
I.e the non terminal evalutes to the same set of terminals and non terminals regardless of context. Whereas for a context sensitive grammar we can have `aAbB -> aabb` where the non terminals in the left have a context of other non terminals and terminals surronding them. 

note sentential forms are the transition states of a sentence as it ets converted from grammar to concrete. i.e
```
<sentence>
<word> SPACE <word>   (this is a sentential form)
HELLO SPACE WORLD
```

a CFL (context free language) is the language generated by a CFG. remember the CFG specifies a set of strings over some alphabet, this set of strings forms a language. 

why do we use a tree rather then a left/right derrivation??It's a graphical representation of the same information and makes it easier to think, furthermore computer science is deeply familiar with tree structures and has gotten very good at manipulating them.

note that a BNF is the pure form of CFG and EBND has regex in it with the ? and + and *.

note, higher precedence operators bind to their operands before lower precedence operators and thus appear lower in the tree.
`A + B * 10` breaks down to `A+(B*10)` because `*` has higher precendence. 

note a grammar is ambigious if the same sentence can be interpreted in more then one way.

note Regular Expressions and Regular Grammars both define a set of strings over some alphabet and are basically the same. The expressions are usually just expressed differently. Note that Finite Automata also do the same thing, define a set of strings over a alphabet. 
All three define a language. 
But note all 3 can't "count" or "nest" meaning that you can't enforce decleration before use of a indeifier unless you enforce that all variables must be in a block before the code starts. (which is what VC does lmao)
Furthermore it can't count/check types with a declaraton so it really can't do function param checking or type checking. 

a right linear grammar is one with at most 1 non-terminal on the right end of the result side. `A->aB`

when converting right linear grammars to NFA's remember to have only 1 end state as the structure basically enforces that you add in a new non terminal state that translates to epsilon. You can't have a non terminal convert to a terminal because then it isn't right linear!!!

the first set for a non terminal is the left most non terminal that arsies if you keep reducing the left hand side as much as possible. Note that you only add in epsilon into the first set if the entire symbol can evaulate to epsilon, not if one of the non terminals involved goes to epsilon. 

The expression Grammar is a form of grammar that does not have any left recursion and thus no ambiguity. With left recursion we don't know how many times we will loop for. 

Follow sets tell us the series of symbols that follow a given nonterminal A which helps us determine if removing this non terminal is the right move. 
take this example

S -> aAb
A -> a | <epsilon>
consider parsing the string 'ab' we go S->aAb then A->epsilon

when we have aAb our logic would go "alright we have a, the lookahead symbol is now b, how can we convert A into b" and would crash. BUT if we said "alright well Follow(A) = {b} lets just have A go to epsilon to get our lookahead token in a round about way"

The select set for a production A→α:

If epsilon is in First(α), then
    Select(A→α) = (First(α) − {ϵ}) ∪ Follow(A)
Otherwise:
    Select(A→α) = First(ϵϵ)

A grammer is LL(1) is for every nonterminal the select set of every branch produces a unique terminal. i.e no two branches can ever produce the same terminal. Once we have this we know there is only one specific path that leads to null because null can only appear once by the rules. This means we don't have to worry about null in any of the parsing, hence select sets just becomes first sets other then the single nullable case!

Note that Left Recursion means that we can't be LL(1) because we can go into a infinite loop if we try to follow the left most path. Non-Direct Left Recursion is just something like A->Ba B->Ab. 

Note that if you have statements with common prefixes then you can't have LL(1) cause you need another lookahead token to tell which of the two to choose. see dangling else grammar. 




## Immediate code generation
---

The Intermediate Code Generator generates an explicit IR from the AST. The IR isn't like universally defined but it must be easy to generate while also being easy to convert into machine code.

for some compilers this step can be skipped and the AST is used to generate code directly. (what we do with our decorated AST)

note some common optimisations that can we done on the IR is to remove code that can't be reached, replace some variable access with a constant if it happens a lot and remove reduant computation or move code around so it runs better. 






