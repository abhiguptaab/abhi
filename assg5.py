In [1]: import pandas as pd

In [2]: ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")

In [3]: ds.shape()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-cd979aa95496> in <module>()
----> 1 ds.shape()

TypeError: 'tuple' object is not callable

In [4]: ds.shape
Out[4]: (29216, 10)

In [5]: ds.tail(10)
Out[5]: 
          City  Edition      Sport   ...         Event Event_gender   Medal
29206  Beijing     2008  Wrestling   ...     74 - 84kg            M    Gold
29207  Beijing     2008  Wrestling   ...     74 - 84kg            M  Silver
29208  Beijing     2008  Wrestling   ...     84 - 96kg            M  Bronze
29209  Beijing     2008  Wrestling   ...     84 - 96kg            M  Bronze
29210  Beijing     2008  Wrestling   ...     84 - 96kg            M    Gold
29211  Beijing     2008  Wrestling   ...     84 - 96kg            M  Silver
29212  Beijing     2008  Wrestling   ...    96 - 120kg            M  Bronze
29213  Beijing     2008  Wrestling   ...    96 - 120kg            M  Bronze
29214  Beijing     2008  Wrestling   ...    96 - 120kg            M    Gold
29215  Beijing     2008  Wrestling   ...    96 - 120kg            M  Silver

[10 rows x 10 columns]

In [6]: ds.medal
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-cb7d0b0a909b> in <module>()
----> 1 ds.medal

/usr/local/lib/python2.7/dist-packages/pandas/core/generic.pyc in __getattr__(self, name)
   4374             if self._info_axis._can_hold_identifiers_and_holds_name(name):
   4375                 return self[name]
-> 4376             return object.__getattribute__(self, name)
   4377 
   4378     def __setattr__(self, name, value):

AttributeError: 'DataFrame' object has no attribute 'medal'

In [7]: import matplotlib.pyplot as plt
/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')

In [8]: ds.plot()
Out[8]: <matplotlib.axes._subplots.AxesSubplot at 0x7f2c87087e10>

In [9]: plt.plot(ds.edition)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-ba6ed6588c96> in <module>()
----> 1 plt.plot(ds.edition)

/usr/local/lib/python2.7/dist-packages/pandas/core/generic.pyc in __getattr__(self, name)
   4374             if self._info_axis._can_hold_identifiers_and_holds_name(name):
   4375                 return self[name]
-> 4376             return object.__getattribute__(self, name)
   4377 
   4378     def __setattr__(self, name, value):

AttributeError: 'DataFrame' object has no attribute 'edition'

In [10]: plt.plot(ds.Edition)
Out[10]: [<matplotlib.lines.Line2D at 0x7f2c8bebad10>]

In [11]: jupyter notebook
  File "<ipython-input-11-38d51a0f6338>", line 1
    jupyter notebook
                   ^
SyntaxError: invalid syntax


In [12]: plt.plot(ds.Edition)
Out[12]: [<matplotlib.lines.Line2D at 0x7f2c87087210>]

In [13]: f=plt.plot(ds.Edition)

In [14]: f
Out[14]: [<matplotlib.lines.Line2D at 0x7f2c862676d0>]

In [15]: f=plt.plot(ds.Edition)

In [16]: f.show()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-16-ffb034f3e6e2> in <module>()
----> 1 f.show()

AttributeError: 'list' object has no attribute 'show'

In [17]: f.show
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-a127333e88b8> in <module>()
----> 1 f.show

AttributeError: 'list' object has no attribute 'show'

In [18]: show(f)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-18-cd3d0cd1d2d8> in <module>()
----> 1 show(f)

NameError: name 'show' is not defined

In [19]: show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-19-ca94444d24bc> in <module>()
----> 1 show()

NameError: name 'show' is not defined

In [20]: plt.plot(ds.Edition)
Out[20]: [<matplotlib.lines.Line2D at 0x7f2c8bdf8f90>]

In [21]: show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-21-ca94444d24bc> in <module>()
----> 1 show()

NameError: name 'show' is not defined

In [22]: plt.plot(ds.Edition).show
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-22-fedd8973f561> in <module>()
----> 1 plt.plot(ds.Edition).show

AttributeError: 'list' object has no attribute 'show'

In [23]: plt.plot(ds.Edition).show()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-9a27c3fb5f0f> in <module>()
----> 1 plt.plot(ds.Edition).show()

AttributeError: 'list' object has no attribute 'show'

In [24]: plt.show
Out[24]: <function matplotlib.pyplot.show>

In [25]: plt.show()
    

In [26]: 

In [26]: plt.plot(ds.Edition,color="red",label="year of event")
Out[26]: [<matplotlib.lines.Line2D at 0x7f2c86205b50>]

In [27]: plt.show()

In [28]: plt.legend(loc="upper left")
/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py:519: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
  warnings.warn("No labelled objects found. "

In [29]: plt.plot(ds.Edition,color="red",label="year of event")
Out[29]: [<matplotlib.lines.Line2D at 0x7f2c83827590>]

In [30]: plt.show()

In [31]: plt.plot(ds.Edition,color="red",linewidth=10)
Out[31]: [<matplotlib.lines.Line2D at 0x7f2c837672d0>]

In [32]: plt.show()

In [33]: plt.plot(ds.Edition,color="red",linewidth=50)
Out[33]: [<matplotlib.lines.Line2D at 0x7f2c836a2bd0>]

In [34]: plt.show()

In [35]: plt.plot(ds.Edition,color="red",linewidth=100)
Out[35]: [<matplotlib.lines.Line2D at 0x7f2c83656e50>]

In [36]: plt.show()

In [37]: plt.plot(ds.Edition,color="red",linewidth=1000)
Out[37]: [<matplotlib.lines.Line2D at 0x7f2c8359e3d0>]

In [38]: plt.show()

In [39]: plt.plot(ds.Edition,color="red",linewidth=2.5)
Out[39]: [<matplotlib.lines.Line2D at 0x7f2c834ce690>]

In [40]: plt.show()

In [41]: fig=plt.gcf()

In [42]: ds.plot()
Out[42]: <matplotlib.axes._subplots.AxesSubplot at 0x7f2c836d2550>

In [43]: fig.savefig(my_graph.png)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-43-af8b16aa2ca8> in <module>()
----> 1 fig.savefig(my_graph.png)

NameError: name 'my_graph' is not defined

In [44]: fig.savefig('my_graph.png')

In [45]: plt.legend(loc='upper left')
Out[45]: <matplotlib.legend.Legend at 0x7f2c8c1fef50>

In [46]: plt.plot(ds.Edition,color="red",linewidth=2.5,label="year of event")
Out[46]: [<matplotlib.lines.Line2D at 0x7f2c833d7ed0>]

In [47]: plt.show()

In [48]: fig=plt.gcf()

In [49]: ds.plot()
Out[49]: <matplotlib.axes._subplots.AxesSubplot at 0x7f2c8341d710>

In [50]: fig.savefig('my_graph.png')

In [51]: 

