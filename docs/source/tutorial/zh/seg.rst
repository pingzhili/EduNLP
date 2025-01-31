成分分解
=========

由于教育资源是一种多模态数据，包含了诸如文本、图片、公式等数据结构；
同时在语义上也可能包含不同组成部分，例如题干、选项等，因此我们首先需要对教育资源的不同组成成分进行识别并进行分解：

* 语义成分分解
* 结构成分分解

主要处理内容
--------------------

1.将字典输入形式的选择题通过 `语法解析 <parse.rst>`_ 转换为符合条件的item；

2.将输入的item按照元素类型进行切分、分组。

学习路线图
--------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   语义成分分解 <seg/语义成分分解>
   结构成分分解 <seg/结构成分分解>

