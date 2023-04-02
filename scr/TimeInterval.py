from datetime import datetime, date, time
#Если есть пересечение интервалов времени - True
#Если пересечение отсутствует - FALSE
def TimeInterval(TI1start, TI1end, TI2start, TI2end):
    latest_start = max(TI1start, TI2start)
    earliest_end = min(TI1end, TI2end)
    return latest_start <= earliest_end
    
#Если начало интервала меньше конца интервала - True
#Если конец интервала меньше начала интервала - FALSE   
def ProverkaInterval(TIstart, TIend)
    return TIstart<=TIend