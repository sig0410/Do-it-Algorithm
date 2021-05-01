#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Any

class FixedQueue:
    
    class Empty(Exception):
        
        pass 
    # 비어있는 고정된 큐에서 디큐 또는 피크할 때 사용하는 예외처리 
    
    class Full(Exception):
        
        pass
    # 가득 차 있는 고정된 큐에서 인큐할 때 사용하는 예외처리 
    
    def __init__(self, capacity : int) -> None:
        
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
        
        # 큐 초기화 
        # 큐 배열을 생성하는 등의 준비 작업 
        
    def __len__(self) -> int:
        
        return self.no 
    # 큐에 있는 데이터 개수 반환 
    
    def is_empty(self) -> bool:
        
        return self.no <= 0
    # 큐가 비어 있는지 판단 
    
    def is_full(self) -> bool:
        
        return self.no >= self.capacity
    
    def enque(self, x : Any) -> None:
        
        if self.is_full():
            raise FixedQueue.Full 
            # 큐에 데이터가 가득 차 있을때 사용하는 예외처리 함수
            
        self.que[self.rear] = x
        # 선입선출방식으로 가장 나중인 순서에 새로운 데이터인 x를 넣는 것 
        self.rear += 1
        # 이후 rear의 값을 1추가 
        self.no += 1
        # 데이터를 추가했으니 1 추가 
        if self.rear == self.capacity:
            self.rear = 0
        # rear와 capacity가 같으면 인덱스 값의 최대값이므로 다시 인덱스 0으로 가야함 
        
        # 데이터를 넣는 함수 
        
    def deque(self) -> Any:
        
        if self.is_empty():
            raise FixedQueue.Empty
            # 큐에 데이터가 없을 때 사용하는 예외처리 함수
            
        x = self.que[self.front]
        # 선입선출방식으로 가장 먼저 들어간 데이터를 빼는 것 
        self.front += 1
        # 이후 front의 값을 1추가
        self.no -= 1
        # 데이터를 제거했으니 1 제거
        if self.front == self.capacity:
            self.front = 0
        # front와 capacity가 같으면 인덱스 값의 최대값이므로 다시 인덱스 0으로 가야함 
            
        return x 
    
        # 데이터를 빼는(디큐) 함수 
        
    def peek(self) -> Any:
        
        if self.is_empty():
            raise FixedQueue.Empty
            # 데이터가 비어있으면 데이터를 볼 수 없으니 예외 처리 
            
        return self.que[self.front]
    
        # 큐에서 데이터를 피크(맨 앞 데이터를 들여다보는 것)
        
    def find(self, value : Any) -> Any:
        
       
        for i in range(self.no): 
            # 데이터 개수만큼 반복
            idx = (i + self.front) % self.capacity 
            # 이렇게 나머지 함수를 사용하면 모든 인덱스를 얻을 수 있다 
            if self.que[idx] == value: # 검색 성공 
                return idx
            # 해당 인덱스 반환 
                
        return -1 # 검색 실패시 -1을 반환 
    
        # 큐에서 찾고자 하는 데이터의 인덱스를 찾는 함수 
    
    def count(self, value : Any) -> bool:
        
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value: # 검색 성공 
                c += 1 # 개수가 몇개인지 반환하기 위해서 사용 
                
        return c
    
        # 큐에서 찾고자 하는 데이터가 몇개가 있는지 찾는 함수 
    
    def __contains__(self, value : Any) -> bool:
        
        return self.count(value)
    
        # 큐에서 찾고자 하는 데이터가 있는지 찾고자 하는 함수 
        
    def clear(self) -> None:
        
        self.no = self.front = self.rear = 0
        
        # 큐의 모든 데이터를 비우는 함수 
        
    def dump(self) -> None:
        
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = '')
                # 각 인덱스별로 front부터 rear까지 출력하는 듯?
                
            print()

