def solution(fees, records):
    def get_time(time1, time2):
        time1 = time1.split(':')
        time2 = time2.split(':')
        return (
            (int(time2[0]) * 60 + int(time2[1]))
            - (int(time1[0]) * 60 + int(time1[1]))
            )
    
    def get_fee(t):
        price = fees[1]
        if t > fees[0]:
            t -= fees[0]
            price += int((t / fees[2]) + 0.9999999) * fees[3]
        return price

    answer = []
    dict = {}
    fee_dict = {}
    for record in records:
        record = record.split()
        if record[2] == 'IN':
            dict[record[1]] = record[0]
        elif record[2] == 'OUT':
            t = get_time(dict[record[1]], record[0])
            fee_dict[record[1]] = fee_dict.get(record[1], 0) + t
            dict[record[1]] = 0
    for car in dict:
        if dict[car]:
            t = get_time(dict[car], '23:59')
            fee_dict[car] = fee_dict.get(car, 0) + t
    
    for car in fee_dict:
        fee_dict[car] = get_fee(fee_dict[car])
    fee_dict = sorted(fee_dict.items(), key=lambda x:x[0])
    answer = [x[1] for x in fee_dict]

    return answer