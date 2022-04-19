import numpy as np
import torch

a = torch.tensor(np.random.randint(10, size=(3,3)), dtype=torch.int32)
print(f'A:\n{a.numpy()}\nShape:{a.shape}')
print('='*40)


b = torch.tensor(np.random.randint(10, size=(1,3)), dtype=torch.int32).unsqueeze(2).unsqueeze(3)
print(f'b:\n{b.numpy()}\nShape:{b.shape}')
print('='*40)

bTa = torch.matmul(torch.transpose(b, 1,3), a)

aTb = torch.matmul(torch.transpose(a, 0, 1), torch.transpose(b, 1, 2))

einsum = torch.einsum('nkld, kj->njld', [b, a])

print(f'b^T X A:\n{bTa.numpy()}\nShape:{bTa.shape}')
print('='*40)
print(f'A^T X b:\n{aTb.numpy()}\nShape:{aTb.shape}')
print('='*40)
print(f'NKLD, KJ->NJLD:\n{einsum.numpy()}\nShape:{einsum.shape}')
print('='*40)

