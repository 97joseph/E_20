# Examples of variables in memory.
# var1 is a label identifying a memory address
# containing 30, and var2 is a label identifying
# a memory address containing 5. We load the value
# at var1 into $1, and the value at var2 into $2.
# Then we AND them into $3, and OR them into $4.
# Then we store $3 into var3.

    lw $1,var1($0)    # read from address var1 + 0
    lw $2,var2($0)    # read from address var2 + 0
    and $3, $1, $2     # AND the values together
    or $4, $1, $2      # then OR them together
    sw $3,var3($0)    # write the AND result into memory
    movi $5, var3      # put the address (not the value!) in $5

    halt               # program ends

var1:
    .fill 30

var2:
    .fill 5

var3:
    .fill 0
#--
#--
#--MACHINE CODE
# ram[0] = 16'b1000000010000111;		// lw $1,var1($0)
# ram[1] = 16'b1000000100001000;		// lw $2,var2($0)
# ram[2] = 16'b0000010100110010;		// and $3,$1,$2
# ram[3] = 16'b0000010101000011;		// or $4,$1,$2
# ram[4] = 16'b1010000110001001;		// sw $3,var3($0)
# ram[5] = 16'b0010001010001001;		// movi $5,var3
# ram[6] = 16'b0100000000000110;		// halt 
# ram[7] = 16'b0000000000011110;		// var1: .fill 30
# ram[8] = 16'b0000000000000101;		// var2: .fill 5
# ram[9] = 16'b0000000000000000;		// var3: .fill 0
#--
#--
#--EXECUTION OUTPUT
# Final state:
# 	pc=    6
# 	$0=    0
# 	$1=   30
# 	$2=    5
# 	$3=    4
# 	$4=   31
# 	$5=    9
# 	$6=    0
# 	$7=    0
# 8087 8108 0532 0543 a189 2289 4006 001e 
# 0005 0004 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
# 0000 0000 0000 0000 0000 0000 0000 0000 
