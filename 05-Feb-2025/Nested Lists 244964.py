# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    records = sorted(records, key=lambda record:record[1])
    lowest_score = records[0][1]
    second_lowest_score = None
    
    for name, score in records:
        if score > lowest_score:
            second_lowest_score = score
            break
    answer = [name for name, score in records if score == second_lowest_score]
    answer.sort()
    for name in answer:
        print(name)