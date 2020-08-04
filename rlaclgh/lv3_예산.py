def solution(budgets, M):
    budgets.sort()
    if budgets[0] * len(budgets) > M:
        return M // len(budgets)
    if sum(budgets) <= M:
        return max(budgets)
    else:
        length =  len(budgets)
        
        lt  , rt = 0 , length -1
        while rt - lt != 1 :
            mid = (lt+rt) //2
            # 올려야되
            if sum(budgets[:mid]) + budgets[mid]*(length-mid) <M :
                lt = mid
            elif sum(budgets[:mid]) + budgets[mid]*(length-mid) >M :
                rt = mid
            else:
                return budgets[mid]
        
        M -= sum(budgets[:rt])
        return M //(length-rt)
        
        
#         new_lt  , new_rt = budgets[lt] , budgets[rt]
#         while new_lt new_rt:
#             new_mid = (new_rt+new_lt)//2
#             if sum(budgets[:rt]) + new_mid * (length- rt) <M:
#                 new_lt = new_mid
#             else:
#                 new_rt = new_mid
            
            
        
    return rt