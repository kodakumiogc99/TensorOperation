# TensorOperation

## MatMulandEinsum.py
* 比較 Matmul 和 Einsum 的差別。
* X 是 data ，其維度為 (*# data, # node, # time, # feature)
  * 資料的數量: n。
  * 每筆資料有多少 node: k。
  * 每個 node 值會隨時間變化: l。
  * 每個 node 有 d 個 feature: d。
* A 是 adjacency matrix, 代表一張 DAG (Bayesian Network)，其維度為(# node, # node)
* ![alt text](./MatMulandEinsum/DataDescription.png)
* 簡化問題: n=1, k=3, l=1, d=1，於是 X=(1,3,1,1), A=(3,3)
* ![alt text](./MatMulandEinsum/Simple.png)
* 計算<img alt="H=X^T\times A" src="https://render.githubusercontent.com/render/math?math=H%3DX%5ET%5Ctimes%20A" style="transform: translateY(20%);" />
* ![alt text](./MatMulandEinsum/XTA.png)
* 計算 <img alt="H=A^T\times X" src="https://render.githubusercontent.com/render/math?math=H%3DA%5ET%5Ctimes%20X" style="transform: translateY(20%);" />
* ![alt text](./MatMulandEinsum/ATX.png)
* 計算 einsum(NKLD, KJ->NJLD)
* ![alt text](./MatMulandEinsum/Einsum.png)
