# numpy

> numpy의 개념과 numpy가 필요한 이유, numpy를 이용하여 벡터와 matrix 즉, 행렬을 만들고 이를 상호변환 시킬 수 있는 API를 사용하는 방법에 대해 알아본다.  
- > [Diving into numpy](https://towardsdatascience.com/diving-into-numpy-b92abfd7a00f)  

## numpy의 개념, 그리고 numpy를 사용하는 이유  

- numpy는 머신러닝 코드 개발을 할 경우 자주 사용되는 벡터, 행렬 등을 표현하고 연산할 때 반드시 필요한 라이브러리다.
- 벡터와 행렬을 이용하면 수치계산이 매우 빨리 수행된다.
- 벡터, 2차원행렬 등을 일반화 => 배열 또는 텐서(tensor)
![tensor](https://github.com/Redwoods/Py/blob/master/pdm2020/my-note/numpy/tensor_order.png)  

## numpy array vs. list  

- 머신러닝에서 숫자, 사람, 동물 등의 인식을 하기 위해서는 이미지 데이터를 행렬(matrix)로 변환하는 것이 중요하다.
- 행렬을 나타내기 위해서는 list를 사용할 수도 있지만, 행렬 연산이 직관적이지 않고 오류 가능성이 높기 때문에 행렬 연산을 위해서는 numpy 사용이 필수적이다.
