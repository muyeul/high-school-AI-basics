# 데이터를 학습, 평가 데이터로 분리하기

# 데이터 준비하기
import pandas as pd               # 모듈 추가하기
df= pd.read_csv('temp_ice.csv',encoding='euc-kr')
#df.head(5)

# 학습(train) 데이터를 입력변수와 출력변수로 나누기
import numpy as np
data = np.array(df)
X= data[:,1]     # 평균기온 열의 데이터를 출력변수로 지정 
Y= data[:,-1]    # 아이스크림/빙수 열의 데이터를 출력변수로 지정 

# 비용을 계산하고 업데이트하기

# 입력변수와 출력변수 각각의 평균(mean) 구하기
mean_x = np.mean(X)
mean_y = np.mean(Y)
 
# X변수의 개수 구하기
n = len(X)

# 최소제곱법을 이용하여 beta0과 beta1 구하기
temp1 = 0
temp2 = 0
for i in range(n):
  temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
  temp2 += (X[i] - mean_x) ** 2
beta1 = temp1 / temp2
beta0 = mean_y - (beta1 * mean_x)
 
# 평가하기 ------------------------------------------------------------
def RMSE(beta0,beta1,x,y):
  RMSE = np.sqrt(((y-(beta0+beta1*x))**2).mean())
  return RMSE


results = RMSE(beta0,beta1,X,Y)
print("손실값 결과는? {0}".format(results))


