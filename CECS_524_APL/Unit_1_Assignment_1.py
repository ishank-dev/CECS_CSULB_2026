# Brainfu*k Interpreter in Python CSULB APL Assignment CECS 524 Unit 1
def interpret(code):
    memory_tape = [0] * 1000  # tape of size 1000
    ptr_tape = 0  # pointer on the tape
    i = 0  # another pointer to read the string
    bracket_mapper = {}  # Bracket map for jumps
    # Bracket map to handle matching '[' and ']', using map for O(1) fast retreival instead of nested loop
    stack = []
    for idx, char in enumerate(code):
        if char == '[':
            stack.append(idx)
        elif char == ']':
            start = stack.pop()
            bracket_mapper[start] = idx
            bracket_mapper[idx] = start
#    print(bracket_mapper)
    while i < len(code):
        
        if code[i] == '>':
            ptr_tape = (ptr_tape + 1) 

        elif code[i] == '<':
            ptr_tape = (ptr_tape - 1) 

        elif code[i] == '+':
            memory_tape[ptr_tape] = (memory_tape[ptr_tape] + 1)

        elif code[i] == '-':
            memory_tape[ptr_tape] = (memory_tape[ptr_tape] - 1)

        elif code[i] == '.':
            print(chr(memory_tape[ptr_tape]), end='')

        elif code[i] == ',':
            memory_tape[ptr_tape] = ord(input()[0])
            

        elif code[i] == '[':
            # move to end of matching closed bracket if pointer is pointing to zero bytes
            if memory_tape[ptr_tape] == 0:
                i = bracket_mapper[i]

        elif code[i] == ']':
            # move to starting of matching open bracket if pointer is pointing to non zero bytes
            if memory_tape[ptr_tape] != 0:
                i = bracket_mapper[i]
        i += 1

if __name__ == "__main__":
    code = input("Welcome to the BrainFu*k Interpreter\nPlease Enter the Brainfu*k code: ")
    #++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
    print("Interpreter Output:")
    interpret(code)