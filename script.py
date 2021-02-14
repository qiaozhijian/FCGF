import numpy as np
import torch

a = np.random.randn(10, 3)
b = torch.tensor([[0, 1, 2], [0, 1, 2], [0, 1, 2]]).view(-1, 3)
print(a)
print(b)
