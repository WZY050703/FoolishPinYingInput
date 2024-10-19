# FoolishPinYingInput
linux上无法安装输入法时(通常是wsl?)的简要替代品，功能非常有限。    
When the input method cannot be installed on Linux (usually WSL?) A brief alternative with very limited features.
## 依赖的库和与之对应的文件
<a herf="https://github.com/pyglet/pyglet">pyglet</a>-:-GUI(My*.py的文件和pinying1.py)    
<a herf="https://github.com/letiantian/Pinyin2Hanzi">Pinyin2Hanzi</a>-:-实现拼音转文字的库(Yin2Zi.py)     
<a herf="https://github.com/adityarathod/xerox">xerox</a>-:-实现拷贝进剪贴板的库(Yin2Zi.py)     
感谢所有有关以上项目的开发者和社区
## 安装和运行
前置：确保你安装了所有依赖库(大部分都能通过pip安装)    
运行：`python3 pinying1.py`    
建议带shell运行，因为可以选备选词
## 局限性
没有对拼音的补全和纠错，并且分词不支持元音开头的拼音(比如“xi'an”)    
候选词比较麻烦，需要手动复制    
不支持直接注入，是写到剪贴板里再粘贴     
操作逻辑比较复杂，需要焦点在Label上("GET"模式时)才能输入，且不支持光标移动
## 开源协议
MIT
