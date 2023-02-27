import string

from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:

    def __init__(self):
        self.productions = {
            'S': ['aA'],
            'A': ['bS','dD'],
            'C': ['bA','a'],
            'D': ['bC','aD'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

if __name__ == '__main__':
    main = Main()
    main.generate_strings(5)
    print(main.generate_strings(0))
    auto = main.grammar.to_finite_automaton()
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    'alphabet': {'a', 'b'},
    'transition': {
        'q0': {'a': 'q1'},
        'q1': {'b': 'q0', 'd': 'q3'},
        'q2': {'a': 'q4', 'b': 'q5'},
        'q3': {'b': 'q2', 'a': 'q3'},
        'q4': {'b': 'q2', 'a': 'q4'},
        'q5': {'a': 'q6', 'b': 'q1'},
        'q6': {'a': 'q3', 'b': 'q5'}

    },
    'start_state': 'q0',
    'final_states': {'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
    }



    checker = FiniteAutomaton(automaton)
    checker.check_strings(['adba', 'abadba', 'adaba', 'adbbaba', 'aabadab'])
    