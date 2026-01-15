prime1=99991
prime2=11527
N=32
seed=eval(input("Please input a number"))
Sequence=set()
for i in range(1000):
    seed*=prime1
    seed+=prime2
    seed%=2**32
    if seed in Sequence:
        break
    else:
        Sequence.add(seed)
print(len(Sequence))
print(Sequence)