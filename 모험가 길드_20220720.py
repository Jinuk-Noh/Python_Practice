#이것이 코딩 테스트다 p506 A01

def Solution(n, array):
    array = sorted(array)
    
    # 중복제거
    temp_array = list(set(array))

    # 그룹
    result = 0

    # 해당 공포도에서 남은 인원
    remain = 0
    for i in temp_array:
        # 해당 공포도 인원 수 + 해당 공포도 보다 낮은 공포도의 남은 인원
        p =  array.count(i) + remain 
        
        # 해당 공포도 인원에서 그 인원 수 만큼 그룹을 형성
        a,b = divmod(p,i)

        # 형성 된 그룹(a)은 더하고 남은 인원들은 다음 공포도 인원 수에 합함 
        result += a
        remain = b

    return result


print(Solution(6,[2,3,1,2,2,4]))
