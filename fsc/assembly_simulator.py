regs = {"x5":0, "x6":0, "x7":0, "x28":0, "x29":0, "x30":0, "x31":0}
regs["x6"] = 2

x5 = "x5"
x6 = "x6"
x7 = "x7"
x28 = "x28"
x29 = "x29"
x30 = "x30"
x31 = "x31"

def addi(rd, rs1, imm):
    regs[rd] = regs[rs1] + imm
    print(regs[rd])
    return regs[rd]
    

sum = addi(x5, x6, 4)
print(regs)