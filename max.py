#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    
    maximum = a[0]
    
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print('최대값 구함')
    
    num = int(input('원소 수 입력 : '))
    
    x = [None] * num # num의 개수만큼 빈 리스트 생성 
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] 값을 입력하세여 : '))
                         
    print(f'최댓값은 {max1(x)} 입니다.')
                   
# Any는 제약이 없는 임의의 자료형을 의미  

