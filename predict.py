import pickle
import numpy as np
import bilstm
import param

# 標籤種類，需與訓練時的一致
tags = param.TAGS
n_tags = len(tags)

# 載入之前訓練時的 word2idx
wordf = open("word2idx.pkl", 'rb')
word2idx = pickle.load(wordf)
n_words = len(word2idx)

#載入pre-trained word2vec
from gensim.models import word2vec
from gensim import models

w2v_model = models.Word2Vec.load("embedding/zh.bin")
embedding_matrix = np.zeros((n_words, param.EMBEDDING_DIMENSION))
for w, i in word2idx.items():
    if w in w2v_model:
        embedding_vector = w2v_model[w]
        embedding_matrix[i] = embedding_vector

# 建立雙向 LSTM 模型
model = bilstm.createModel(n_words, n_tags, param.SENTENCE_MAX_LEN, embedding_matrix) 

# 載入已經訓練好的網路參數權重
model.load_weights("ner_model.h5")

# 請使用者輸入想要進行 NER 標注的句子
sentence = input("請輸入句子：")

# 將使用者輸入的句子進行填充到固定的長度
from keras.preprocessing.sequence import pad_sequences
X_test = [[word2idx[w[0]] for w in sentence]]
X_test = pad_sequences(maxlen=param.SENTENCE_MAX_LEN, sequences=X_test, padding="post",value=n_words - 1)

# 利用模型進行預測
p = model.predict(np.array([X_test[0]]), verbose=0)
p = np.argmax(p, axis=-1) # 取得預測出來機率最大的類別
count = 0
for w, pred in zip(X_test[0], p[0]):
    if w == n_words - 1: # 如果已經到達用於填充的 ENDPAD 字元，迴圈跳出
        break
    print("{:3}: {}".format(sentence[count],tags[pred]))
    count += 1
