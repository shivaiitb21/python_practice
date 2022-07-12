#Binary search algorithms

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            hi = mid - 1  
        elif cards[mid] > query:
            lo = mid + 1
    
    return -1