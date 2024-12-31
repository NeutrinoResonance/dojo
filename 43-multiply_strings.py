class Solution:
    def __init__(self):
        self.mult_pre_compute = {}
        self.mpc = self.mult_pre_compute
        
        for i in range(0, 10):
            i_pre_compute = {}
            self.mult_pre_compute[str(i)] = i_pre_compute
            
            for j in range(0, 10):
                i_pre_compute[str(j)] = i * j
        
    def multiply(self, num1:str, num2:str) -> str:
        radix = 1
        current_sum = 0
        
        addend = 0
        for (i_idx, i) in enumerate(reversed(num1)):
            saved_radix = radix
            
            for (j_idx, j) in enumerate(reversed(num2)):
                mult = self.mpc[i][j]
                mult += addend

                if j_idx != len(num2) - 1:
                    remainder = mult % 10
                    current_sum += radix * remainder
                    addend = int((mult - remainder) / 10)
                    radix *= 10
                else:
                    current_sum += radix * mult
                    addend = 0

                
            
            radix = saved_radix * 10
            
        return str(current_sum)
