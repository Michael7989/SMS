import fasttext
import jieba
jieba.cut('你好')
def segment(msg):
    data = jieba.cut(msg)
    return ' '.join(data)

def test(model_path):
    classify = fasttext.load_model(model_path, label_prefix='__label__')
    while True:
        msg = input("请输入短信：")
        data = segment(msg)
        pre = classify.predict([data])
        if pre[0][0] == '0':
            print("非垃圾短信")
        else:
            print("垃圾短信")

if __name__ == '__main__':
    model_path = 'msg_model.bin'
    test(model_path)

