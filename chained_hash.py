#!/usr/bin/env python
# coding: utf-8

# In[4]:


from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    # 해시를 구성하는 노드
    
    def __init__(self, key : Any, value : Any, next : Node) -> None:
        
        self.key = key
        self.value = value
        self.next = next
        
class ChainedHash:
    
    def __init__(self, capacity : int) -> None:
        
        self.capacity = capacity 
        # 해시 테이블 크기 지정 
        
        self.table = [None] * capacity
        # 해시 테이블을 선언 
        # 현재 해시 테이블안에는 모든 버킷이 비어있음 
        # 해시 테이블을 크게 만들면 충돌을 피할 수 있지만 그것은 메모리를 낭비
        # 충돌을 피하기 위해 해시 함수가 해시 테이블 크기보다 작거나 같은 정수를 고르게 생성 
        
    def hash_value(self, key : Any) -> int:
        # 해시 값 구하는 것 
        if isinstance(key, int):
            return key % self.capacity # 키를 테이블 크기만큼 나눈 것을 리턴 
        return(int(hashlib.sha20256(str(key).encode()).hexdigest(),16) % self.capacity)
    
    def search(self, key : Any) -> Any:
        # 키가 key인 원소를 검색하여 값을 반환 
        hash = self.hash_value(key)
        # 검색하는 키의 해시값 
        p = self.table[hash]
        
        while p is not None:
            if p.key == key: # p의 키와 내가 찾고 싶은 키가 같으면 
                return p.value # 검색 성공 
            p = p.next # 뒤쪽 노드 주목 
        return None # 검색 실패 
    
    def add(self, key : Any, value : Any) -> bool:
        
        hash = self.hash_value(key)
        # 추가하고자하는 key의 해시값 
        p = self.table[hash]
        
        while p is not None:
            if p.key == key: # p의 키와 내가 찾고 싶은 키가 같으면 
                return False # 추가 실패 
            p = p.next # 뒤쪽 노드 주목 
        
        temp = Node(key, value, self.table[hash]) # 새로운 노드 생성 
        self.table[hash] = temp # 노드에 해시값 넣기 
        return True # 성공 
    
    def remove(self, key : Any) -> bool:
        # 키가 key인 원소 삭제 
        
        hash = self.hash_value(key) # 해시값 도출 
        p = self.table[hash] # 노드 주목 
        pp = None 
        
        while p is not None: # None이 아닐때 
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next 
                else:
                    pp.next = p.next
                return True # key 삭제 성공 
            pp = p
            p = p.next 
        return False # 삭제 실패 
    
    def dump(self) -> None:
        
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end = '')
                p = p.next
            print()
            
    # dump()함수는 해시 테이블의 내용을 한꺼번에 통째로 출력하는 것 


# In[ ]:




