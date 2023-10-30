'''
문제 설명
양방향 연결 리스트를 활용하여 큐 (queue) 의 추상적 자료구조 (abstract data structure) 구현을 완성하세요.
정의하고자 하는 큐의 추상적 자료구조는 class LinkedListQueue 로 구현됩니다. 이 문제는 해당 클래스의 메서드들의 구현을 빈칸 채우기 형태로 완성하는 것으로 되어 있으며, 이 클래스의 구현은 L120 부터 시작합니다.
그 위에는 (LL1-117) 이 추상적 자료구조를 구현하기 위해서 이용할 class DoublyLinkedList 와, 또한 여기서 이용하는 class Node 의 구현이 정의되어 있습니다.
이 코드는 이전의 "양방향 연결 리스트" 강의에서 다루어진 것과 완전히 동일합니다.
정확성 테스트는 class LinkedListQueue 의 각 메서드가 올바르게 구현되어 있는지를 검사합니다. "코드 실행" 을 눌렀을 때 예시 테스트 케이스를 통과하는 것은 아무런 의미가 없습니다.
'''

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    # 사이즈 반환
    def size(self):
        return self.data.getLength()

    # 비었는지 체크
    def isEmpty(self):
        return self.data.getLength() == 0

    # append 구현
    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1, node)

    # 첫번째 요소 빼기
    def dequeue(self):
        return self.data.popAt(1)

    # 첫번째 요소의 데이터 반환
    def peek(self):
        return self.data.getAt(1).data

def solution(x):
    return 0