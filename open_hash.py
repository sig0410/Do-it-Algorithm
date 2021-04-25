#!/usr/bin/env python
# coding: utf-8

# In[4]:


from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED = 0 # 데이터 저장 
    EMPTY = 1 # 비어있음 
    DELETE = 2 # 삭제 완료
    
class Bucket:
    # 해시를 구성하는 버킷 
    
    def __init__(self, key : Any = None, value : Any = None, stat : Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat
        
    def set_status(self, stat: Status) -> None:
        
        self. stat = stat
        
class OpenHash:
    # 오픈 주소법으로 구현하는 해시 클래스 
    
    def __init__(self, capacity : int) -> None:
        self.capacity = capacity 
        self.table = [Bucket()] * self.capacity
        
    def hash_value(self, key : Any) -> int:
        # 해시값을 구하는 것 
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)% self.capacity)
    
    def rehash_value(self, key : Any) -> int:
        # 재해시값을 구함 
        return(self.hash_value(key) + 1) % self.capacity # 해당 노드에 값이 있으면 키에 +1을 더해 다음 노드로 이동시키는 것(재해시 과정)
    
    def search_node(self, key : Any) -> Any:
        hash = self.hash_value(key) # 해시값 
        p = self.table[hash]
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY: # 버킷이 비어있으면 멈춤 
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p 
            # 버킷에 데이터가 없고 p의 키와 검색하고자 하는 키가 값으면 p를 리턴 
            hash = self.rehash_value(hash) # 재해시 
            p = self.table[hash]
        return None
    
    def search(self, key : Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
        
    def add(self, key : Any, value : Any) -> bool:
        if self.search(key) is not None:
            return False 
        # 이미 값이 있으므로 추가 할 수 없음 
        
        hash = self.hash_value(key) # 추가하고자 하는 키의 해시값
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True 
            # 위의 조건을 만족하면 새로운 버킷을 만들어서 그것을 추가 
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False 
    
    def remove(self, key : Any) -> int:
        
        p = self.search_node(key)
        if p is None:
            return False 
        # 값이 없으므로 삭제 못함 
        p.set_status(Status.DELETED)
        return True # 삭제 성공 
    
    def dump(self) -> None:
        # 해시 테이블의 구성을 보여주는 함수 
        for i in range(self.capacity):
            print(f'{i:2} ', end = '')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제 완료 --')
        # Status에 따라서 도출되는 결과를 보여줌 
        


# In[ ]:




