# 垃圾短信识别系统
## model: `fasttext`
作者：李栋<563408650@qq.com><br>
这是一个python版的垃圾短信识别算法<br>
系统环境要求：Linux<br>
本文件夹包含文件如下：<br>
	-test_seg fasttext格式测试集<br>
	-segment.py 分词代码<br>
	-train.py 训练模型代码<br>
	-test.py 测试集测试代码<br>
	-test_online.py 手动输入测试<br>
	-msg_model.bin 已训练好的模型<br>
	-requirement.txt pip依赖<br>
	-README.md<br>
本系统已自带训练好的模型，可直接调用进行测试，测试集测试精确度99.7%<br>
测试步骤:<br>
1.在当前目录下在终端中运行"pip install -r requirement.txt"(若为pip3，则运行"pip3 install -r requirement.txt")<br>
2.①代码测试，可运行"python test.py"，得到运行数据准确率的信息。<br>
  ②手动测试：运行"python test_online.py"，根据提示手动输入待验证短信即可。<br>

