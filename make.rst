make
====

利用计算机所有线程来进行编译

::

    make -j
    
    让make最多允许4个编译线程同时执行
    make -j 4
    
    make --help
    -j [N], --jobs[=N]          Allow N jobs at once; infinite jobs with no arg.

