# Instruction numbers
PUSH, ADD, PRINT = range(3)

# full runtime state of a process
# number of remaining steps, instruction pointer, instruction list
state_example = [100, 0, [[PUSH, 1], [PUSH, 2], [ADD], [PRINT]]]

# indexes of the state components
STEPS, IP, CODE = range(3)

def execute(state):

	# Runtime stack for data manipulation
	stack = []
	
	while True:
		
		# Uncomment this to see the program state and stack each step
		print("STATE:", state)
		print("STACK:", stack)
		
		steps = state[STEPS]
		ip = state[IP]
		code = state[CODE]
		
		# We are out of steps, stop the process
		if steps <= 0:
			break
		
		# No instructions are left, stop the process
		if ip >= len(code):
			break
		
		if len(code[ip]) == 2:
			# Some instructions have an argument, unpack that as well
			instruction, argument = code[ip]
		else:
			instruction = code[ip][0]
			argument = None
		
		
		if instruction == PUSH:
			# Push the argument to the top of the stack
			stack.append(argument)
		elif instruction == ADD:
			# Pop the two topmost elements from the stack, add them and push the result back on the stack
			stack.append(stack.pop(-1) + stack.pop(-1))
		elif instruction == PRINT:
			# Pop the topmost element from the stack and print it
			print("OUTPUT:", stack.pop(-1))
		
		# Move the instruction pointer one step forward to point to the next instruction
		state[IP] += 1
		
		# Reduce the number of remaining steps by one
		state[STEPS] -= 1
		
		# Print a newline after each iteration
		print("")

execute(state_example)
