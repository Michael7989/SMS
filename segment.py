import jieba
from sklearn.model_selection import train_test_split

def segment(in_path, out_path):
    f_in = open(in_path, 'r', encoding='utf-8')
    f_out = open(out_path, 'w', encoding='utf-8')
    cnt = 0
    for line in f_in:
        data = line.strip().split('\t')
        try:
            msg = jieba.cut(data[2])
            f_out.write(' '.join(msg) + '\t__label__' + data[1] + '\n')
        except:
            print(data)
            continue
        cnt += 1
        if cnt % 1000 == 0:
            print('已处理' + str(cnt) + '行')

def split(in_path, out_train, out_test):
    f_in = open(in_path, 'r', encoding='utf-8')
    data = []
    for line in f_in:
        data.append(line.strip())
    y = [0] * len(data)
    x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2)
    f_out_train = open(out_train, 'w', encoding='utf-8')
    for line in x_train:
        f_out_train.write(line+'\n')
    print('训练集拆分完成')
    f_out_test = open(out_test, 'w', encoding='utf-8')
    for line in x_test:
        f_out_test.write(line+'\n')
    print('测试集拆分完成')


if __name__ == '__main__':
    in_path = '垃圾短信训练集80W条.txt'
    out_path = 'seg_msg'
    # segment(in_path, out_path)
    split(out_path, 'train_seg', 'test_seg')
