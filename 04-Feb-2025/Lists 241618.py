# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        commands = input().split()
        if commands[0] == 'insert':
            result.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == 'remove':
            result.remove(int(commands[1]))
        elif commands[0] == 'append':
            result.append(int(commands[1]))
        elif commands[0] == 'pop':
            result.pop()
        elif commands[0] == 'sort':
            result.sort() 
        elif commands[0] == 'reverse':
            result.reverse() 
        else:
            print(result)