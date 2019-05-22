import fasttext
import json
import time

def trainClassifer(document_path = 'G:/cail2018_big/seg_data/cail2018_big_seg_text_law.txt', out_model_path = 'classifer_law_2grams_model_pre.bin'):
    a = time.time()
    print("开始训练模型。。。")
    classifier = fasttext.supervised(document_path, out_model_path, dim = 300, word_ngrams = 1, lr=0.1, lr_update_rate=100, epoch=25, min_count = 15, thread=12, label_prefix='__label__')
    b = time.time()
    print("训练完毕，共用时"+str(b-a)+"秒")

if __name__ == '__main__':
    trainClassifer('train_seg', 'msg_model')
