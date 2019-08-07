# 「數位文本探勘」課程 — 專有名詞辨識 NER 範例實作

## 檔案說明
* param.py : 模型相關參數設定皆位於此
* bilstm.py : 雙向LSTM模型建置定義
* dataload.py : 載入訓練與測試資料集
* train.py : 訓練步驟實作
* predict.py : 完成訓練後，可輸入句子取得辨識結果
* ner_model.h5 : 訓練出來的模型檔案 (train.py時會自動產生，predict.py需用到)
* word2idx.pkl : 記錄 word 與其 id 對應的 dictionary pickle (train.py時會自動產生)

## 目錄說明
* data : 訓練資料與測試資料目錄
* embedding : 預訓練詞向量

## 執行所需環境
* Python 3
* TensorFlow
* Keras
* numpy

## 進行訓練
    python train.py

## 進行預測
    python predict.py
