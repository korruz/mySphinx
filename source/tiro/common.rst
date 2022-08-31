.. _common:

一般语法
==========

解析 Python 类
------------------

自动解析写好的 `python` 类、函数。

主要有以下步骤：

#. 在 `conf.py` 文档的 `extention` 中添加 `"sphinx.ext.autodoc"`

#. 在 `conf.py` 文档中加入 `sys.path.insert(0, os.path.abspath("../pythonclass"))` ，
   一般是在开头，其中的 `../pythonclass` 是想要导入的类对于 `conf.py` 的位置的相对路径。

#. 在想要添加的位置加入 `.. autoclass:: Test.Test` ，这里是相对与第二点加入的路经而言。

.. autoclass:: Test.Test
    :members: