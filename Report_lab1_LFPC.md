# Laboratory 1 Report

## Theory

- String: In computer science and mathematics, a string is a sequence of characters, which can include letters, numbers, punctuation marks, and other symbols. Strings are often used to represent words, sentences, or other data in a way that a computer can process.

- Alphabet: An alphabet is a set of symbols or characters that can be used to create strings. In computer science, an alphabet is usually a finite set of characters or symbols, such as the set {0, 1} used in binary arithmetic.

- Language: In computer science, a language is a set of strings that are formed from an alphabet. For example, the English language can be considered a set of strings that are formed from the English alphabet.

- Grammar: A grammar is a set of rules for generating strings in a language. In computer science, grammars are often used to describe the syntax of programming languages or other formal languages. A grammar consists of a set of production rules that specify how to form valid strings in the language.

- Finite state automaton: A finite state automaton (FSA) is a mathematical model of computation that can be used to recognize or generate strings in a language. An FSA consists of a finite number of states, which can transition between each other based on input symbols. FSAs are often used in computer science to model simple algorithms or to recognize patterns in input data.

## Objectives

1. Understand what a language is and what it needs to have in order to be considered a formal one.

2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);

b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;

c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

a. Implement a type/class for your grammar;

b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;

## Implementation

The FiniteAutomaton class responds for implementing the Finite Automata. Basically, we have a constructor where we assign values for the attributes:

- Q - a set of states
- Sigma - a set of input symbols
- delta - a transition function that maps a state and an input symbol to a new state
- q0 - the initial state
- F - a set of accepting states

The string_belongs_to_language method takes an input string and returns a boolean value indicating whether the input string is recognized by the FSA. It does this by iterating through each symbol in the input string and checking if it is in the FSA's input alphabet (Sigma). If it is, the transition function is applied to the current state and the symbol to obtain the next state. If the next state is an accepting state, the isAcceptingState flag is set to True. If the next state is not an accepting state or is not a valid state in the FSA (Q), the isAcceptingState flag is set to False. If the symbol is not in the input alphabet or the transition function cannot be applied to the current state and the symbol, the method returns False. Finally, the method returns the value of the isAcceptingState flag.

The Gramar class has 2 methods and the constructor. The constructor is used to instantiate 4 attributes: