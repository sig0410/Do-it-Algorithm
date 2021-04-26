#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Any

class FixedStack:
    
    class Empty(Exception):
        pass
        # 비어있는 Stack에 팝이나 피크할 때 내보내는 예외 처리 
        
    class Full(Exception):
        pass
        # 가득 찬 Stack에 푸시할 때 내보내는 예외 처리 
        
    def __init__(self, capacity : int = 256) -> None:
        # 초기화
        self.stk = [None] * capacity # 스택 본체 
        self.capacity = capacity # 스택 크기 
        self.ptr = 0 # 스택 포인터
        
    def __len__(self) -> int:
        # 스택에 쌓여있는 데이터 개수 반환 
        return self.ptr
    
    def is_empty(self) -> bool:
        # 스택이 비어 있는지 판단 
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        # 스택이 가득 차 있는지 판단 
        return self.ptr >= self.capacity
    
    def push(self, value : Any) -> None:
        # 스택에 value를 PUSH(데이터를 추가)
        if self.is_full():
            raise FixedStack.Full
            # 스택이 가득찬 경우 예외 처리 가능 
            
        self.stk[self.ptr] = value 
        # value를 가장 앞에 넣어줌 
        self.ptr += 1
        # ptr을 1개 추가 
        
    def pop(self) -> Any:
        # 스택에서 value를 POP(데이터를 꺼냄)
        if self.is_empty():
            raise FixedStack.Empty 
            # 스택이 비어있는 경우 예외 처리 가능 
            
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        # 스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)
        if self.is_empty():
            raise FixedStack.Empty 
            # 스택이 비어있는 경우 예외 처리 가능 
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        # 스택에 있는 모든 value 삭제(빈 스택을 만듬 )
        self.ptr = 0
        
    def find(self, value : Any) -> Any:
        # 스택에서 value를 찾아 인덱스를 반환(없으면 -1)
        for i in range(self.ptr - 1, -1, -1): # 후입선출이라서 거꾸로 해야함
            if self.stk[i] == value:
                return i 
        return -1
    
    def count(self, value : Any) -> bool:
        # 스택에 있는 value 개수 반환 
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value: 
                c += 1
        return c
    
    def __contains__(self, value : Any) -> bool:
        # 스택에 value가 있는지 판단 
        return self.count(value)
    
    def dump(self) -> None:
        # dump(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
        
# raise문으로 프로그램의 예외 처리를 의도적으로 내보낼 수 있음 

