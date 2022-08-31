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

要创建段落, 请使用空白行将一行或多行文本进行分隔.

换行
------------

在一行的末尾添加两个或多个空格, 然后按回车键, 即可创建一个换行.

强调
----------

通过将文本设置为粗体或斜体来强调其重要性.

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

可以将多个条目组织成有序或无序列表.

.. code-block:: rst

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

要将单词或短语表示为代码, 请将其包裹在两个反引号 (`) 中.
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

内部链接:
为了支持对任何文档中任意位置的交叉引用, 使用了标准 reST 标签. 为此, 标签名称在整个文档中必须是唯一的.
::

    .. _my-reference-label:

    Section to cross-reference
    --------------------------

    This is the text of the section.

    It refers to the section itself, see :ref:`my-reference-label`.

引文
------

支持标准 reST 引用, 其附加功能是 "global" , 即所有引用都可以从所有文件引用. 像这样使用它们：
::

    Lorem ipsum [Ref]_ dolor sit amet.
    .. [Ref] Book or article reference, URL or whatever.

引用用法类似于脚注用法,但标签不是数字或以 "＃" 开头.

图片
------------

reST 支持一个 `image <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image>`_ 指令.
在 Sphinx 中使用时, 给定的文件名(此处为 "gnu.png" )必须相对于源文件, 或者绝对意味着它们相对于顶级源目录.
例如, 文件 "sketch/spam.rst" 可以将图像 "images/spam.png" 写为
"../images/spam.png" 或 "/images/spam.png".
::

    .. image:: picture.jpeg
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right

表格
------

网格式表格
~~~~~~~~~~~~~~

网格式表格,需要自己绘制, 对中文支持较差(主要是对不齐). 这边一个可以转换的网站 `tableconvert <https://tableconvert.com/>`_.
::

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+

模拟表格
~~~~~~~~~~~~~~

- 还有一种简化表格, 非常类似markdown所使用的表格方式::

   =====================  ======================================================
   参数                   说明
   =====================  ======================================================
   ``x``                  告诉tar解压缩
   ``-C <directory>``     tar在解压缩之前先进入指定 ``<directory>`` 目录
   ``--numeric-owner``    tar恢复文件的owner帐号数字, 不匹配恢复系统的用户名帐号
   =====================  ======================================================

展现效果如下:

=====================  ======================================================
参数                   说明
=====================  ======================================================
``x``                  告诉tar解压缩
``-C <directory>``     tar在解压缩之前先进入指定 ``<directory>`` 目录
``--numeric-owner``    tar恢复文件的owner帐号数字, 不匹配恢复系统的用户名帐号
=====================  ======================================================

列表表格指令(List Table Directive)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``.. list-table::`` 指令就是将常规的 ``list`` 转换成表格, 每个表格有一定的列, 以及指定表格列宽度的tag。

为了恰当地格式化, 星号 ``*`` 标记每行必须是垂直对齐(align vertically), 而连字符 ``-`` 则表示每一列也要对齐。空白的单元必须记录, 所以一行中每个列都需要标记, 即使这个单元没有内容::

   .. list-table:: Title
      :widths: 25 25 50
      :header-rows: 1

      * - Heading row 1, column 1
        - Heading row 1, column 2
        - Heading row 1, column 3
      * - Row 1, column 1
        -
        - Row 1, column 3
      * - Row 2, column 1
        - Row 2, column 2
        - Row 2, column 3

则显示如下

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3

CSV文件
~~~~~~~~~~~~

通常使用Excel比RST语法更容易创建表格, 所以你可使用Excel将表格保存成CSV文件, 然后在Sphinx的reStructured Text文件中引用这个CSV文件, 就能够展示表格。

要使用CSV文件, 则使用 ``.. csv-table::`` 指令, 对于列宽度, 则制定百分比(但是不需要 ``%`` 符号), 对于行头, 则通常使用1::

   .. csv-table:: CSV案例展示
      :file: csv_example.csv
      :widths: 30, 30, 40
      :header-rows: 1

``csv_example.csv`` 文件内容:

.. literalinclude:: csv_example.csv
   :language: bash
   :linenos:
   :caption:

以上代码案例显示效果：

.. csv-table:: CSV案例展示
   :file: csv_example.csv
   :widths: 30, 30, 40
   :header-rows: 1

数据量小的话, 直接丢进来.

.. csv-table:: CSV案例展示-数据量小
   :widths: 30, 30, 40
   :header-rows: 1

    ITEM,DUE DATE,AMOUNT
    Rent/mortgage,2020/3/12,$800.00
    Electric,2020/4/1,$120.00
    Gas,2020/7/3,$50.00
    Cell phone,2002/9/11,$45.00

注释
------

每个显式标记块都不是有效的标记结构(如上面的脚注), 它被视为注释. 例如:
::

    .. This is a comment.

您可以在评论开始后缩进文本以形成多行注释:
::

    ..
       This whole indented block
       is a comment.

       Still in the comment.

脚注
------

对于脚注, 使用 ``[#name]_`` 标记脚注位置, 并在 "脚注" 标题后添加脚注主体在文档底部, 像这样:
::

    Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

    .. rubric:: Footnotes

    .. [#f1] Text of the first footnote.
    .. [#f2] Text of the second footnote.
