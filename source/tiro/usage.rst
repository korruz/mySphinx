.. _grammer:

基本语法
========================

标题
----------

一级标题 ::
    
    这是一级标题
    =============

二级标题 ::

    这是二级标题
    -------------

三级标题 ::

    这是三级标题
    ~~~~~~~~~~~~~

段落
------------

要创建段落，请使用空白行将一行或多行文本进行分隔。

换行
------------

在一行的末尾添加两个或多个空格，然后按回车键,即可创建一个换行。

强调
----------

通过将文本设置为粗体或斜体来强调其重要性。

斜体 ::

    *斜体*

加粗 ::

    **加粗**

引用
------------

::

    ::

    Great idea!

列表
----------

可以将多个条目组织成有序或无序列表。

.. code-block:: none

    * 第一层1
    * 第一层2

        * 第二层1
        * 第二层2
    
    * 第一层3

    1. 第一项 有序.
    2. 第二项 有序.

    #. 第一项 有序.
    #. 第二项 有序.

代码
------------

要将单词或短语表示为代码，请将其包裹在两个反引号 (`) 中。
::

    ``code``

链接
------------

外部链接：
::

    `Python文档 <https://docs.python.org/zh-cn/3/>`_
    或者
    This is a paragraph that contains `a link`_.
    .. _a link: https://domain.invalid/

内部链接：  
为了支持对任何文档中任意位置的交叉引用，使用了标准reST标签。为此，标签名称在整个文档中必须是唯一的。
::

    .. _my-reference-label:

    Section to cross-reference
    --------------------------

    This is the text of the section.

    It refers to the section itself, see :ref:`my-reference-label`.

引文
------

支持标准reST引用，其附加功能是 “global” ，即所有引用都可以从所有文件引用。像这样使用它们：
::
    
    Lorem ipsum [Ref]_ dolor sit amet.
    .. [Ref] Book or article reference, URL or whatever.

引用用法类似于脚注用法，但标签不是数字或以“＃”开头。

图片
------------

reST支持一个 `image <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image>`_ 指令。
在Sphinx中使用时，给定的文件名(此处为“gnu.png”)必须相对于源文件，或者绝对意味着它们相对于顶级源目录。
例如，文件“sketch/spam.rst”可以将图像 “images/spam.png”写为“../images/spam.png”或 “/images/spam.png”。
::
    
    .. image:: picture.jpeg
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right

表格
------

.. admonition:: 注意

    标记语言对表格支持还是不太行。

网格式表格，需要自己绘制，对中文支持较差（主要是对不齐）。这边一个可以转换的网站 `tableconvert <https://tableconvert.com/>`_。
::

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+

简单表格更容易撰写，但有限制：它们必须包含不止一行，第一列单元格不能包含多行。如:
::

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

注释
------

每个显式标记块都不是有效的标记结构(如上面的脚注)，它被视为注释。例如：
::

    .. This is a comment.

您可以在评论开始后缩进文本以形成多行注释：
::

    ..
       This whole indented block
       is a comment.

       Still in the comment.

脚注
------

对于脚注，使用 ``[#name]_`` 标记脚注位置，并在“脚注”标题后添加脚注主体在文档底部，像这样：
::

    Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

    .. rubric:: Footnotes

    .. [#f1] Text of the first footnote.
    .. [#f2] Text of the second footnote.
