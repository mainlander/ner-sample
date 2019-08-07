TRAIN_FILE = "data/train.txt"
TEST_FILE = "data/test.txt"

def load():
    train_sentences = []
    test_sentences = []
    words = []
    tags = []

    with open(TRAIN_FILE, 'rb') as f:
        temp_segs = []
        for line in f:
            line = line.decode('utf-8', 'ignore')
            line = line.strip()
            if line == '':
                train_sentences.append(temp_segs)
                temp_segs = []
            else:
                ss = line.split(' ')
                word = ss[0].strip()
                tag = ss[1].strip()
                if word not in words:
                    words.append(word)
                if tag not in tags:
                    tags.append(tag)
                temp_segs.append( (word, tag) )
    with open(TEST_FILE, 'rb') as f:
        temp_segs = []
        for line in f:
            line = line.decode('utf-8', 'ignore')
            line = line.strip()
            if line == '':
                test_sentences.append(temp_segs)
                temp_segs = []
            else:
                ss = line.split(' ')
                word = ss[0].strip()
                tag = ss[1].strip()
                if word not in words:
                    words.append(word)
                temp_segs.append( (word, tag) )

    # 過濾掉長度大於200個字的句子
    train_sentences = list(filter(lambda x: len(x) < 200, train_sentences))
    test_sentences = list(filter(lambda x: len(x) < 200, test_sentences))
    #將vocabulary裡面加上用來填充的單字 ENDPAD
    words.append('ENDPAD')

    return train_sentences, test_sentences, words, tags

    
