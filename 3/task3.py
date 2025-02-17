import numpy as np
x = [1,2,3]
y = [6,11,8]
X = np.column_stack((np.ones_like(x), x))
  
B = np.linalg.inv(X.T @ X) @ X.T @ y
print(B)
beta_0, beta_1 = B  
y_pred = X @ B  
pred = []
for i in range(len(x)):
    pred.append(beta_0 + beta_1 * x[i])
SSR = np.sum((y - y_pred) ** 2)
print(pred)
print(y_pred)
print(f"Сумма квадратов остатков (SSR): {SSR:.4f}")
