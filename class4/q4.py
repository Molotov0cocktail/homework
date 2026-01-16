import numpy as np
Class=10
N=eval(input('Please input the number of sample'))
raw_parameter=np.random.randint(0,Class,size=N)
# print(raw_parameter)
onehot_encoding=np.zeros((N,Class),dtype=np.int32)
onehot_encoding[np.arange(N),raw_parameter]=1
print(onehot_encoding)