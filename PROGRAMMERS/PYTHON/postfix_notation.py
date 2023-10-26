""""
인자로 주어진 문자열 expr 은 소괄호와 사칙연산 기호, 그리고 정수들로만 이루어진 중위 표현 수식입니다. 함수 solution() 은 
이 수식의 값을 계산하여 그 결과를 리턴하도록 작성되어 있습니다. 
이 함수는 차례로 splitTokens(), infixToPostfix(), 그리고 postfixEval() 함수를 호출하여 이 수식의 값을 계산하는데,

splitTokens() - 강의 내용에서와 같은 코드로 이미 구현되어 있습니다.
infixToPostfix() - 지난 강의의 연습문제에서 작성했던 코드를 수정하여, 문자열이 아닌 리스트를 리턴하도록 작성합니다.
postfixEval() - 이번 강의의 연습문제입니다. 함수의 내용을 완성하세요.
즉, 두 개의 함수 infixToPostfix() 와 postfixEval() 을 구현하는 연습입니다. 스택을 이용하기 위하여 class ArrayStack 이 정의되어 있으므로 그것을 활용하세요.

[참고] Python 에는 eval() 이라는 built-in 함수가 있어서, 이 함수에 문자열을 인자로 전달하면, 
그 문자열을 그대로 Python 표현식으로 간주하고 계산한 결과를 리턴하도록 되어 있습니다. 이 built-in 함수 eval() 을 이용하면 이 연습문제는 전혀 직접 코드를 작성하지 않고도 정답을 낼 수 있을 것이지만, 
스택을 이용하여 중위표현식을 계산하는 프로그래밍 연습을 위한 것이니, 강의 내용에서 설명한 절차를 수행하도록 코드를 작성해 보세요.
"""
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    #스택(연산자)
    opStack = ArrayStack()
    #후위표현
    postfixList = []
    for i in tokenList:
        #알파벳일때 출력에 추가
        if isinstance(i,int):
            postfixList.append(i)
        # 여는 괄호일때 스택에 추가
        elif i == "(":
            opStack.push(i)
        # 닫는 괄호일 때 여는 괄호가 나올때까지 출력에 추가, 괄호 빼기
        elif i == ")":
            while prec[opStack.peek()] != 1:
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            while not opStack.isEmpty() and prec[i] <= prec[opStack.peek()]:
                postfixList.append(opStack.pop())
            opStack.push(i)
    
    # 스택에 남은거 다 빼서 출력에 추가        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return postfixList


def postfixEval(tokenList):
    #AB+CD+* (A+B)*(C+D) // AB-CD-/
    val = 0
    opStack = ArrayStack()
    #숫자면 스택에 추가
    for i in tokenList:
        if isinstance(i,int):
            opStack.push(i)
        else:
            #연산자면 스택 맨 위에 있는거는 뒤로
            #두번째꺼는 앞으로 해서 연산 (우선순위), val에 추가
            later = opStack.pop()
            front = opStack.pop()
            if i == '+':
                val= front+later
            elif i == '-':
                val=  front-later
            elif i == '*':
                val=  front*later
            elif i == '/':
                val=  front/later
            # 연산한 값 넣기
            opStack.push(val)
    
    return opStack.peek()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val