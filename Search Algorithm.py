#!/usr/bin/env python
# coding: utf-8

# ### Linear Search
#     - 직선(선형) 모양으로 늘어선 배열에서 검색하는 경우 원하는 키값을 가진 원소를 찾을 때까지 순서대로 검색하는 알고리즘 

# While문을 사용한 Linear Search

# In[4]:


from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int:
    
    i = 0
    
    while True:
        if i == len(a):
        # 원하는 키값을 찾지 못하고 검색 실패한 경우
            return -1 
        # 검색을 실패했으니 -1을 반환 
        
        if a[i] == key:
            return i 
        # 원하는 키값을 찾아 해당 인덱스 번호를 출력 
        i += 1 
        
if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    # x에 원소를 넣어줌 
    
    ky = int(input('검색할 값 입력 : '))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print('검색한 원소가 없습니다.')
        
    else:
        print(f'검색한 값은 x[{idx}]에 존재합니다.')
    


# for문을 사용한 Linear Search

# In[5]:


from typing import Any, Sequence

def seq_search1(a : Sequence, key : Any) -> int:
    
    for i in range(len(a)):
        if a[i] == key:
            return i
        
    return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    # x에 원소를 넣어줌 
    
    ky = int(input('검색할 값 입력 : '))
    
    idx = seq_search1(x, ky)
    
    if idx == -1:
        print('검색한 원소가 없습니다.')
        
    else:
        print(f'검색한 값은 x[{idx}]에 존재합니다.')
    

