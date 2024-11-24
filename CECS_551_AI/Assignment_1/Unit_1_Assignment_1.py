# Brainfu*k Interpreter in Python CSULB APL Assignment CECS 524 Unit 1
def interpret(code):
    memory_tape = [0] * 1000  # tape of size 1000
    ptr_tape = 0  # pointer on the tape
    i = 0  # another pointer to read the string
    bracket_mapper = {}  # Bracket map for jumps
    input_buffer = []  # Buffer to handle multi-character input
    # Bracket map to handle matching '[' and ']', using map for O(1) fast retrieval instead of nested loop
    stack = []
    for idx, char in enumerate(code):
        if char == '[':
            stack.append(idx)
        elif char == ']':
            start = stack.pop()
            bracket_mapper[start] = idx
            bracket_mapper[idx] = start
    
    while i < len(code):
        if code[i] == '>':
            ptr_tape = (ptr_tape + 1) % 1000  # Prevents going out of bounds
        elif code[i] == '<':
            ptr_tape = (ptr_tape - 1) % 1000
        elif code[i] == '+':
            memory_tape[ptr_tape] = (memory_tape[ptr_tape] + 1) % 256  # Ensures memory value is between 0-255 for wrap arounds
        elif code[i] == '-':
            memory_tape[ptr_tape] = (memory_tape[ptr_tape] - 1) % 256 
        elif code[i] == '.':
            print(chr(memory_tape[ptr_tape]), end='')
        elif code[i] == ',':
            if not input_buffer:  # If the buffer is empty, request input
                input_buffer = list(input("Input: "))  # Take input as a string
            if input_buffer:
                memory_tape[ptr_tape] = ord(input_buffer.pop(0))  # Take one character at a time from the buffer
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
    # Sample Test
    #++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
    print("Interpreter Output:")
    interpret(code)
