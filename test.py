import fasttext

def test(in_path, model_path):
    classify = fasttext.load_model(model_path)
    result = classify.test(in_path)
    print('P@1:', result.precision)
    print('R@1:', result.recall)
    print('Number of examples:', result.nexamples)

def test2(in_path, model_path, out_path):
    classify = fasttext.load_model(model_path, label_prefix='__label__')
    with open(in_path, 'r', encoding='utf-8') as f_in:
        true = []
        result = []
        for line in f_in:
            data = line.strip().split('\t')
            pre = classify.predict([data[0]])
            result.append(pre[0][0])
            true_label = data[1].split('__label__')[1]
            true.append(true_label)
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(str(result)+'\n')
        f_out.write(str(true)+'\n')


if __name__ == '__main__':
    # test('test_seg', 'msg_model.bin')
    test2('test_seg', 'msg_model.bin', 'result')
