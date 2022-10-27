import pandas as pd # csv 파일 읽기
import numpy as np # 행렬 연산
import matplotlib.pyplot as plt # 예측 데이터 표시
from keras.models import Sequential # 딥러닝 모델 예측
from keras.layers import LSTM, Dropout, Dense, Activation


data = pd.read_csv('003670.KS.csv')
data.head()

high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 50 #윈도우 사이즈 50
sequence_length = seq_len + 1 # 50개 후 1개 예측

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index: index + sequence_length])

normalized_data = []
for window in result:
    normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

# 9:1 테스트 셋 : 트레이닝 셋
row = int(round(result.shape[0] * 0.9))
train = result[:row, :]
np.random.shuffle(train)

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

x_train.shape, x_test.shape

model = Sequential() #모델을 순차적으로 정의하는 클래스

model.add(LSTM(50, return_sequences=True, input_shape=(50, 1))) #LSTM 레이어
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear')) #output 1개
model.compile(loss='mse', optimizer='rmsprop')
model.summary()

model.fit(x_train, y_train,
    validation_data=(x_test, y_test),
    batch_size=10,
    epochs=20)
pred = model.predict(x_test)

fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
ax.plot(pred, label='Prediction')
ax.legend()
plt.show()