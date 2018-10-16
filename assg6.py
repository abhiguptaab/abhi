In [1]: import pandas as pd

In [2]: ds=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")

In [3]: ds.shape
Out[3]: (5043, 28)

In [4]: ds.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5043 entries, 0 to 5042
Data columns (total 28 columns):
color                        5024 non-null object
director_name                4939 non-null object
num_critic_for_reviews       4993 non-null float64
duration                     5028 non-null float64
director_facebook_likes      4939 non-null float64
actor_3_facebook_likes       5020 non-null float64
actor_2_name                 5030 non-null object
actor_1_facebook_likes       5036 non-null float64
gross                        4159 non-null float64
genres                       5043 non-null object
actor_1_name                 5036 non-null object
movie_title                  5043 non-null object
num_voted_users              5043 non-null int64
cast_total_facebook_likes    5043 non-null int64
actor_3_name                 5020 non-null object
facenumber_in_poster         5030 non-null float64
plot_keywords                4890 non-null object
movie_imdb_link              5043 non-null object
num_user_for_reviews         5022 non-null float64
language                     5031 non-null object
country                      5038 non-null object
content_rating               4740 non-null object
budget                       4551 non-null float64
title_year                   4935 non-null float64
actor_2_facebook_likes       5030 non-null float64
imdb_score                   5043 non-null float64
aspect_ratio                 4714 non-null float64
movie_facebook_likes         5043 non-null int64
dtypes: float64(13), int64(3), object(12)
memory usage: 1.1+ MB

In [5]: ds.head()
Out[5]: 
   color         ...          movie_facebook_likes
0  Color         ...                         33000
1  Color         ...                             0
2  Color         ...                         85000
3  Color         ...                        164000
4    NaN         ...                             0

[5 rows x 28 columns]

In [6]: ds.tail()
Out[6]: 
      color         ...          movie_facebook_likes
5038  Color         ...                            84
5039  Color         ...                         32000
5040  Color         ...                            16
5041  Color         ...                           660
5042  Color         ...                           456

[5 rows x 28 columns]

In [7]: ds['movie_title']
Out[7]: 
0                                                AvatarÂ 
1              Pirates of the Caribbean: At World's EndÂ 
2                                               SpectreÂ 
3                                 The Dark Knight RisesÂ 
4       Star Wars: Episode VII - The Force AwakensÂ   ...
5                                           John CarterÂ 
6                                          Spider-Man 3Â 
7                                               TangledÂ 
8                               Avengers: Age of UltronÂ 
9                Harry Potter and the Half-Blood PrinceÂ 
10                   Batman v Superman: Dawn of JusticeÂ 
11                                     Superman ReturnsÂ 
12                                    Quantum of SolaceÂ 
13           Pirates of the Caribbean: Dead Man's ChestÂ 
14                                      The Lone RangerÂ 
15                                         Man of SteelÂ 
16             The Chronicles of Narnia: Prince CaspianÂ 
17                                         The AvengersÂ 
18          Pirates of the Caribbean: On Stranger TidesÂ 
19                                       Men in Black 3Â 
20            The Hobbit: The Battle of the Five ArmiesÂ 
21                               The Amazing Spider-ManÂ 
22                                           Robin HoodÂ 
23                  The Hobbit: The Desolation of SmaugÂ 
24                                   The Golden CompassÂ 
25                                            King KongÂ 
26                                              TitanicÂ 
27                           Captain America: Civil WarÂ 
28                                           BattleshipÂ 
29                                       Jurassic WorldÂ 
                              ...                        
5013                                             ManitoÂ 
5014                                            RampageÂ 
5015                                            SlackerÂ 
5016                                        Dutch KillsÂ 
5017                                          Dry SpellÂ 
5018                                           FlywheelÂ 
5019                                             ExeterÂ 
5020                                         The RidgesÂ 
5021                                    The Puffy ChairÂ 
5022                               Stories of Our LivesÂ 
5023                                   Breaking UpwardsÂ 
5024                           All Superheroes Must DieÂ 
5025                                     Pink FlamingosÂ 
5026                                              CleanÂ 
5027                                         The CircleÂ 
5028                                        Tin Can ManÂ 
5029                                           The CureÂ 
5030                                     On the DownlowÂ 
5031                       Sanctuary; Quite a ConundrumÂ 
5032                                               BangÂ 
5033                                             PrimerÂ 
5034                                             CaviteÂ 
5035                                        El MariachiÂ 
5036                                    The Mongol KingÂ 
5037                                          NewlywedsÂ 
5038                            Signed Sealed DeliveredÂ 
5039                          The FollowingÂ             
5040                               A Plague So PleasantÂ 
5041                                   Shanghai CallingÂ 
5042                                  My Date with DrewÂ 
Name: movie_title, Length: 5043, dtype: object

In [8]: ds[duration[:10]]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-e881f1e9ffb1> in <module>()
----> 1 ds[duration[:10]]

NameError: name 'duration' is not defined

In [9]: ds.[duration[:10]]
  File "<ipython-input-9-0c534f14c3e4>", line 1
    ds.[duration[:10]]
       ^
SyntaxError: invalid syntax


In [10]: ds['duration'][:5]
Out[10]: 
0    178.0
1    169.0
2    148.0
3    164.0
4      NaN
Name: duration, dtype: float64

In [11]: ds[ds['duration']>60]
Out[11]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
30               Color         ...                         80000
...                ...         ...                           ...
5011             Color         ...                           489
5012             Color         ...                         10000
5013             Color         ...                            61
5014             Color         ...                             0
5015   Black and White         ...                          2000
5016             Color         ...                            33
5017             Color         ...                           200
5018             Color         ...                           725
5019             Color         ...                             0
5020               NaN         ...                            33
5021             Color         ...                           297
5023             Color         ...                           324
5024             Color         ...                           835
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5028   Black and White         ...                           105
5029             Color         ...                           817
5030             Color         ...                            22
5031             Color         ...                           424
5032             Color         ...                            20
5033             Color         ...                         19000
5034             Color         ...                            74
5035             Color         ...                             0
5036             Color         ...                             4
5037             Color         ...                           413
5038             Color         ...                            84
5040             Color         ...                            16
5041             Color         ...                           660
5042             Color         ...                           456

[4919 rows x 28 columns]

In [12]: ds.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5043 entries, 0 to 5042
Data columns (total 28 columns):
color                        5024 non-null object
director_name                4939 non-null object
num_critic_for_reviews       4993 non-null float64
duration                     5028 non-null float64
director_facebook_likes      4939 non-null float64
actor_3_facebook_likes       5020 non-null float64
actor_2_name                 5030 non-null object
actor_1_facebook_likes       5036 non-null float64
gross                        4159 non-null float64
genres                       5043 non-null object
actor_1_name                 5036 non-null object
movie_title                  5043 non-null object
num_voted_users              5043 non-null int64
cast_total_facebook_likes    5043 non-null int64
actor_3_name                 5020 non-null object
facenumber_in_poster         5030 non-null float64
plot_keywords                4890 non-null object
movie_imdb_link              5043 non-null object
num_user_for_reviews         5022 non-null float64
language                     5031 non-null object
country                      5038 non-null object
content_rating               4740 non-null object
budget                       4551 non-null float64
title_year                   4935 non-null float64
actor_2_facebook_likes       5030 non-null float64
imdb_score                   5043 non-null float64
aspect_ratio                 4714 non-null float64
movie_facebook_likes         5043 non-null int64
dtypes: float64(13), int64(3), object(12)
memory usage: 1.1+ MB

In [13]: ds.content_rating.describe()
Out[13]: 
count     4740
unique      18
top          R
freq      2118
Name: content_rating, dtype: object

In [14]: ds.aspect_ratio.fillna('')
Out[14]: 
0       1.78
1       2.35
2       2.35
3       2.35
4           
5       2.35
6       2.35
7       1.85
8       2.35
9       2.35
10      2.35
11      2.35
12      2.35
13      2.35
14      2.35
15      2.35
16      2.35
17      1.85
18      2.35
19      1.85
20      2.35
21      2.35
22      2.35
23      2.35
24      2.35
25      2.35
26      2.35
27      2.35
28      2.35
29         2
        ... 
5013    1.78
5014    2.35
5015    1.37
5016        
5017    1.78
5018    1.85
5019    1.85
5020        
5021        
5022        
5023    2.35
5024    2.35
5025    1.37
5026    2.35
5027    1.85
5028    1.33
5029    1.85
5030        
5031      16
5032        
5033    1.85
5034        
5035    1.37
5036        
5037        
5038        
5039      16
5040        
5041    2.35
5042    1.85
Name: aspect_ratio, Length: 5043, dtype: object

In [15]: ds.title_year.fillna()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-15-98e837b8e32b> in <module>()
----> 1 ds.title_year.fillna()

/usr/local/lib/python2.7/dist-packages/pandas/core/series.pyc in fillna(self, value, method, axis, inplace, limit, downcast, **kwargs)
   3423                                           axis=axis, inplace=inplace,
   3424                                           limit=limit, downcast=downcast,
-> 3425                                           **kwargs)
   3426 
   3427     @Appender(generic._shared_docs['replace'] % _shared_doc_kwargs)

/usr/local/lib/python2.7/dist-packages/pandas/core/generic.pyc in fillna(self, value, method, axis, inplace, limit, downcast)
   5346         """
   5347         inplace = validate_bool_kwarg(inplace, 'inplace')
-> 5348         value, method = validate_fillna_kwargs(value, method)
   5349 
   5350         self._consolidate_inplace()

/usr/local/lib/python2.7/dist-packages/pandas/util/_validators.pyc in validate_fillna_kwargs(value, method, validate_scalar_dict_value)
    344 
    345     if value is None and method is None:
--> 346         raise ValueError("Must specify a fill 'value' or 'method'.")
    347     elif value is None and method is not None:
    348         method = clean_fill_method(method)

ValueError: Must specify a fill 'value' or 'method'.

In [16]: ds.title_year.fillna('')
Out[16]: 
0       2009
1       2007
2       2015
3       2012
4           
5       2012
6       2007
7       2010
8       2015
9       2009
10      2016
11      2006
12      2008
13      2006
14      2013
15      2013
16      2008
17      2012
18      2011
19      2012
20      2014
21      2012
22      2010
23      2013
24      2007
25      2005
26      1997
27      2016
28      2012
29      2015
        ... 
5013    2002
5014    2009
5015    1991
5016    2015
5017    2013
5018    2003
5019    2015
5020    2011
5021    2005
5022    2014
5023    2009
5024    2011
5025    1972
5026    2004
5027    2000
5028    2007
5029    1997
5030    2004
5031    2012
5032    1995
5033    2004
5034    2005
5035    1992
5036    2005
5037    2011
5038    2013
5039        
5040    2013
5041    2012
5042    2004
Name: title_year, Length: 5043, dtype: object

In [17]: ds.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5043 entries, 0 to 5042
Data columns (total 28 columns):
color                        5024 non-null object
director_name                4939 non-null object
num_critic_for_reviews       4993 non-null float64
duration                     5028 non-null float64
director_facebook_likes      4939 non-null float64
actor_3_facebook_likes       5020 non-null float64
actor_2_name                 5030 non-null object
actor_1_facebook_likes       5036 non-null float64
gross                        4159 non-null float64
genres                       5043 non-null object
actor_1_name                 5036 non-null object
movie_title                  5043 non-null object
num_voted_users              5043 non-null int64
cast_total_facebook_likes    5043 non-null int64
actor_3_name                 5020 non-null object
facenumber_in_poster         5030 non-null float64
plot_keywords                4890 non-null object
movie_imdb_link              5043 non-null object
num_user_for_reviews         5022 non-null float64
language                     5031 non-null object
country                      5038 non-null object
content_rating               4740 non-null object
budget                       4551 non-null float64
title_year                   4935 non-null float64
actor_2_facebook_likes       5030 non-null float64
imdb_score                   5043 non-null float64
aspect_ratio                 4714 non-null float64
movie_facebook_likes         5043 non-null int64
dtypes: float64(13), int64(3), object(12)
memory usage: 1.1+ MB

In [18]: ds['budget']
Out[18]: 
0       237000000.0
1       300000000.0
2       245000000.0
3       250000000.0
4               NaN
5       263700000.0
6       258000000.0
7       260000000.0
8       250000000.0
9       250000000.0
10      250000000.0
11      209000000.0
12      200000000.0
13      225000000.0
14      215000000.0
15      225000000.0
16      225000000.0
17      220000000.0
18      250000000.0
19      225000000.0
20      250000000.0
21      230000000.0
22      200000000.0
23      225000000.0
24      180000000.0
25      207000000.0
26      200000000.0
27      250000000.0
28      209000000.0
29      150000000.0
           ...     
5013        24000.0
5014            NaN
5015        23000.0
5016        25000.0
5017        22000.0
5018        20000.0
5019            NaN
5020        17350.0
5021        15000.0
5022        15000.0
5023        15000.0
5024        20000.0
5025        10000.0
5026         4500.0
5027        10000.0
5028        10000.0
5029      1000000.0
5030            NaN
5031       200000.0
5032            NaN
5033         7000.0
5034         7000.0
5035         7000.0
5036         3250.0
5037         9000.0
5038            NaN
5039            NaN
5040         1400.0
5041            NaN
5042         1100.0
Name: budget, Length: 5043, dtype: float64

In [19]: ds.budget.fillna(ds.budget.mean())
Out[19]: 
0       2.370000e+08
1       3.000000e+08
2       2.450000e+08
3       2.500000e+08
4       3.975262e+07
5       2.637000e+08
6       2.580000e+08
7       2.600000e+08
8       2.500000e+08
9       2.500000e+08
10      2.500000e+08
11      2.090000e+08
12      2.000000e+08
13      2.250000e+08
14      2.150000e+08
15      2.250000e+08
16      2.250000e+08
17      2.200000e+08
18      2.500000e+08
19      2.250000e+08
20      2.500000e+08
21      2.300000e+08
22      2.000000e+08
23      2.250000e+08
24      1.800000e+08
25      2.070000e+08
26      2.000000e+08
27      2.500000e+08
28      2.090000e+08
29      1.500000e+08
            ...     
5013    2.400000e+04
5014    3.975262e+07
5015    2.300000e+04
5016    2.500000e+04
5017    2.200000e+04
5018    2.000000e+04
5019    3.975262e+07
5020    1.735000e+04
5021    1.500000e+04
5022    1.500000e+04
5023    1.500000e+04
5024    2.000000e+04
5025    1.000000e+04
5026    4.500000e+03
5027    1.000000e+04
5028    1.000000e+04
5029    1.000000e+06
5030    3.975262e+07
5031    2.000000e+05
5032    3.975262e+07
5033    7.000000e+03
5034    7.000000e+03
5035    7.000000e+03
5036    3.250000e+03
5037    9.000000e+03
5038    3.975262e+07
5039    3.975262e+07
5040    1.400000e+03
5041    3.975262e+07
5042    1.100000e+03
Name: budget, Length: 5043, dtype: float64

In [20]: ds.budget.fillna(ds.budget.sum())
Out[20]: 
0       2.370000e+08
1       3.000000e+08
2       2.450000e+08
3       2.500000e+08
4       1.809142e+11
5       2.637000e+08
6       2.580000e+08
7       2.600000e+08
8       2.500000e+08
9       2.500000e+08
10      2.500000e+08
11      2.090000e+08
12      2.000000e+08
13      2.250000e+08
14      2.150000e+08
15      2.250000e+08
16      2.250000e+08
17      2.200000e+08
18      2.500000e+08
19      2.250000e+08
20      2.500000e+08
21      2.300000e+08
22      2.000000e+08
23      2.250000e+08
24      1.800000e+08
25      2.070000e+08
26      2.000000e+08
27      2.500000e+08
28      2.090000e+08
29      1.500000e+08
            ...     
5013    2.400000e+04
5014    1.809142e+11
5015    2.300000e+04
5016    2.500000e+04
5017    2.200000e+04
5018    2.000000e+04
5019    1.809142e+11
5020    1.735000e+04
5021    1.500000e+04
5022    1.500000e+04
5023    1.500000e+04
5024    2.000000e+04
5025    1.000000e+04
5026    4.500000e+03
5027    1.000000e+04
5028    1.000000e+04
5029    1.000000e+06
5030    1.809142e+11
5031    2.000000e+05
5032    1.809142e+11
5033    7.000000e+03
5034    7.000000e+03
5035    7.000000e+03
5036    3.250000e+03
5037    9.000000e+03
5038    1.809142e+11
5039    1.809142e+11
5040    1.400000e+03
5041    1.809142e+11
5042    1.100000e+03
Name: budget, Length: 5043, dtype: float64

In [21]: ds.budget.fillna(ds.budget.max())
Out[21]: 
0       2.370000e+08
1       3.000000e+08
2       2.450000e+08
3       2.500000e+08
4       1.221550e+10
5       2.637000e+08
6       2.580000e+08
7       2.600000e+08
8       2.500000e+08
9       2.500000e+08
10      2.500000e+08
11      2.090000e+08
12      2.000000e+08
13      2.250000e+08
14      2.150000e+08
15      2.250000e+08
16      2.250000e+08
17      2.200000e+08
18      2.500000e+08
19      2.250000e+08
20      2.500000e+08
21      2.300000e+08
22      2.000000e+08
23      2.250000e+08
24      1.800000e+08
25      2.070000e+08
26      2.000000e+08
27      2.500000e+08
28      2.090000e+08
29      1.500000e+08
            ...     
5013    2.400000e+04
5014    1.221550e+10
5015    2.300000e+04
5016    2.500000e+04
5017    2.200000e+04
5018    2.000000e+04
5019    1.221550e+10
5020    1.735000e+04
5021    1.500000e+04
5022    1.500000e+04
5023    1.500000e+04
5024    2.000000e+04
5025    1.000000e+04
5026    4.500000e+03
5027    1.000000e+04
5028    1.000000e+04
5029    1.000000e+06
5030    1.221550e+10
5031    2.000000e+05
5032    1.221550e+10
5033    7.000000e+03
5034    7.000000e+03
5035    7.000000e+03
5036    3.250000e+03
5037    9.000000e+03
5038    1.221550e+10
5039    1.221550e+10
5040    1.400000e+03
5041    1.221550e+10
5042    1.100000e+03
Name: budget, Length: 5043, dtype: float64

In [22]: ds.budget=ds.budget.fillna(ds.budget.max())

In [23]: ds
Out[23]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
4                  NaN         ...                             0
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
...                ...         ...                           ...
5013             Color         ...                            61
5014             Color         ...                             0
5015   Black and White         ...                          2000
5016             Color         ...                            33
5017             Color         ...                           200
5018             Color         ...                           725
5019             Color         ...                             0
5020               NaN         ...                            33
5021             Color         ...                           297
5022   Black and White         ...                            45
5023             Color         ...                           324
5024             Color         ...                           835
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5028   Black and White         ...                           105
5029             Color         ...                           817
5030             Color         ...                            22
5031             Color         ...                           424
5032             Color         ...                            20
5033             Color         ...                         19000
5034             Color         ...                            74
5035             Color         ...                             0
5036             Color         ...                             4
5037             Color         ...                           413
5038             Color         ...                            84
5039             Color         ...                         32000
5040             Color         ...                            16
5041             Color         ...                           660
5042             Color         ...                           456

[5043 rows x 28 columns]

In [24]: ds.budget=ds.budget.fillna(ds.budget.max())

In [25]: ds.budget.fillna(ds.budget.max())
Out[25]: 
0       2.370000e+08
1       3.000000e+08
2       2.450000e+08
3       2.500000e+08
4       1.221550e+10
5       2.637000e+08
6       2.580000e+08
7       2.600000e+08
8       2.500000e+08
9       2.500000e+08
10      2.500000e+08
11      2.090000e+08
12      2.000000e+08
13      2.250000e+08
14      2.150000e+08
15      2.250000e+08
16      2.250000e+08
17      2.200000e+08
18      2.500000e+08
19      2.250000e+08
20      2.500000e+08
21      2.300000e+08
22      2.000000e+08
23      2.250000e+08
24      1.800000e+08
25      2.070000e+08
26      2.000000e+08
27      2.500000e+08
28      2.090000e+08
29      1.500000e+08
            ...     
5013    2.400000e+04
5014    1.221550e+10
5015    2.300000e+04
5016    2.500000e+04
5017    2.200000e+04
5018    2.000000e+04
5019    1.221550e+10
5020    1.735000e+04
5021    1.500000e+04
5022    1.500000e+04
5023    1.500000e+04
5024    2.000000e+04
5025    1.000000e+04
5026    4.500000e+03
5027    1.000000e+04
5028    1.000000e+04
5029    1.000000e+06
5030    1.221550e+10
5031    2.000000e+05
5032    1.221550e+10
5033    7.000000e+03
5034    7.000000e+03
5035    7.000000e+03
5036    3.250000e+03
5037    9.000000e+03
5038    1.221550e+10
5039    1.221550e+10
5040    1.400000e+03
5041    1.221550e+10
5042    1.100000e+03
Name: budget, Length: 5043, dtype: float64

In [26]: ds.dropna(how='all')
Out[26]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
4                  NaN         ...                             0
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
...                ...         ...                           ...
5013             Color         ...                            61
5014             Color         ...                             0
5015   Black and White         ...                          2000
5016             Color         ...                            33
5017             Color         ...                           200
5018             Color         ...                           725
5019             Color         ...                             0
5020               NaN         ...                            33
5021             Color         ...                           297
5022   Black and White         ...                            45
5023             Color         ...                           324
5024             Color         ...                           835
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5028   Black and White         ...                           105
5029             Color         ...                           817
5030             Color         ...                            22
5031             Color         ...                           424
5032             Color         ...                            20
5033             Color         ...                         19000
5034             Color         ...                            74
5035             Color         ...                             0
5036             Color         ...                             4
5037             Color         ...                           413
5038             Color         ...                            84
5039             Color         ...                         32000
5040             Color         ...                            16
5041             Color         ...                           660
5042             Color         ...                           456

[5043 rows x 28 columns]

In [27]: ds.dropna(how='any')
Out[27]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
30               Color         ...                         80000
...                ...         ...                           ...
4936             Color         ...                             0
4941             Color         ...                           667
4944             Color         ...                             0
4955             Color         ...                             0
4956             Color         ...                             0
4959             Color         ...                           471
4960             Color         ...                             0
4962   Black and White         ...                             0
4964             Color         ...                             0
4971             Color         ...                             0
4973   Black and White         ...                         24000
4975             Color         ...                            30
4977             Color         ...                             0
4978             Color         ...                             0
4979             Color         ...                           812
4984             Color         ...                           265
4987             Color         ...                             0
4997             Color         ...                           451
4998             Color         ...                             0
5001             Color         ...                             0
5008   Black and White         ...                             0
5011             Color         ...                           489
5012             Color         ...                         10000
5015   Black and White         ...                          2000
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5033             Color         ...                         19000
5035             Color         ...                             0
5042             Color         ...                           456

[3975 rows x 28 columns]

In [28]: ds.dropna(axis=1,how='any')
Out[28]: 
                                                 genres         ...          movie_facebook_likes
0                       Action|Adventure|Fantasy|Sci-Fi         ...                         33000
1                              Action|Adventure|Fantasy         ...                             0
2                             Action|Adventure|Thriller         ...                         85000
3                                       Action|Thriller         ...                        164000
4                                           Documentary         ...                             0
5                               Action|Adventure|Sci-Fi         ...                         24000
6                              Action|Adventure|Romance         ...                             0
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...                         29000
8                               Action|Adventure|Sci-Fi         ...                        118000
9                      Adventure|Family|Fantasy|Mystery         ...                         10000
10                              Action|Adventure|Sci-Fi         ...                        197000
11                              Action|Adventure|Sci-Fi         ...                             0
12                                     Action|Adventure         ...                             0
13                             Action|Adventure|Fantasy         ...                          5000
14                             Action|Adventure|Western         ...                         48000
15                      Action|Adventure|Fantasy|Sci-Fi         ...                        118000
16                      Action|Adventure|Family|Fantasy         ...                             0
17                              Action|Adventure|Sci-Fi         ...                        123000
18                             Action|Adventure|Fantasy         ...                         58000
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...                         40000
20                                    Adventure|Fantasy         ...                         65000
21                             Action|Adventure|Fantasy         ...                         56000
22                       Action|Adventure|Drama|History         ...                         17000
23                                    Adventure|Fantasy         ...                         83000
24                             Adventure|Family|Fantasy         ...                             0
25                       Action|Adventure|Drama|Romance         ...                             0
26                                        Drama|Romance         ...                         26000
27                              Action|Adventure|Sci-Fi         ...                         72000
28                     Action|Adventure|Sci-Fi|Thriller         ...                         44000
29                     Action|Adventure|Sci-Fi|Thriller         ...                        150000
...                                                 ...         ...                           ...
5013                                       Drama|Family         ...                            61
5014                              Action|Crime|Thriller         ...                             0
5015                                       Comedy|Drama         ...                          2000
5016                               Crime|Drama|Thriller         ...                            33
5017                                     Comedy|Romance         ...                           200
5018                                              Drama         ...                           725
5019                            Horror|Mystery|Thriller         ...                             0
5020                              Drama|Horror|Thriller         ...                            33
5021                               Comedy|Drama|Romance         ...                           297
5022                                              Drama         ...                            45
5023                                            Romance         ...                           324
5024                                    Sci-Fi|Thriller         ...                           835
5025                                Comedy|Crime|Horror         ...                             0
5026                                Drama|Music|Romance         ...                           171
5027                                              Drama         ...                           697
5028                                             Horror         ...                           105
5029                      Crime|Horror|Mystery|Thriller         ...                           817
5030                                              Drama         ...                            22
5031                             Comedy|Horror|Thriller         ...                           424
5032                                        Crime|Drama         ...                            20
5033                              Drama|Sci-Fi|Thriller         ...                         19000
5034                                           Thriller         ...                            74
5035                Action|Crime|Drama|Romance|Thriller         ...                             0
5036                                        Crime|Drama         ...                             4
5037                                       Comedy|Drama         ...                           413
5038                                       Comedy|Drama         ...                            84
5039                       Crime|Drama|Mystery|Thriller         ...                         32000
5040                              Drama|Horror|Thriller         ...                            16
5041                               Comedy|Drama|Romance         ...                           660
5042                                        Documentary         ...                           456

[5043 rows x 8 columns]

In [29]: ds.dropna(axis=1,how='all')
Out[29]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
4                  NaN         ...                             0
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
...                ...         ...                           ...
5013             Color         ...                            61
5014             Color         ...                             0
5015   Black and White         ...                          2000
5016             Color         ...                            33
5017             Color         ...                           200
5018             Color         ...                           725
5019             Color         ...                             0
5020               NaN         ...                            33
5021             Color         ...                           297
5022   Black and White         ...                            45
5023             Color         ...                           324
5024             Color         ...                           835
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5028   Black and White         ...                           105
5029             Color         ...                           817
5030             Color         ...                            22
5031             Color         ...                           424
5032             Color         ...                            20
5033             Color         ...                         19000
5034             Color         ...                            74
5035             Color         ...                             0
5036             Color         ...                             4
5037             Color         ...                           413
5038             Color         ...                            84
5039             Color         ...                         32000
5040             Color         ...                            16
5041             Color         ...                           660
5042             Color         ...                           456

[5043 rows x 28 columns]

In [30]: ds.dropna(thresh=5)
Out[30]: 
                 color         ...          movie_facebook_likes
0                Color         ...                         33000
1                Color         ...                             0
2                Color         ...                         85000
3                Color         ...                        164000
4                  NaN         ...                             0
5                Color         ...                         24000
6                Color         ...                             0
7                Color         ...                         29000
8                Color         ...                        118000
9                Color         ...                         10000
10               Color         ...                        197000
11               Color         ...                             0
12               Color         ...                             0
13               Color         ...                          5000
14               Color         ...                         48000
15               Color         ...                        118000
16               Color         ...                             0
17               Color         ...                        123000
18               Color         ...                         58000
19               Color         ...                         40000
20               Color         ...                         65000
21               Color         ...                         56000
22               Color         ...                         17000
23               Color         ...                         83000
24               Color         ...                             0
25               Color         ...                             0
26               Color         ...                         26000
27               Color         ...                         72000
28               Color         ...                         44000
29               Color         ...                        150000
...                ...         ...                           ...
5013             Color         ...                            61
5014             Color         ...                             0
5015   Black and White         ...                          2000
5016             Color         ...                            33
5017             Color         ...                           200
5018             Color         ...                           725
5019             Color         ...                             0
5020               NaN         ...                            33
5021             Color         ...                           297
5022   Black and White         ...                            45
5023             Color         ...                           324
5024             Color         ...                           835
5025             Color         ...                             0
5026             Color         ...                           171
5027             Color         ...                           697
5028   Black and White         ...                           105
5029             Color         ...                           817
5030             Color         ...                            22
5031             Color         ...                           424
5032             Color         ...                            20
5033             Color         ...                         19000
5034             Color         ...                            74
5035             Color         ...                             0
5036             Color         ...                             4
5037             Color         ...                           413
5038             Color         ...                            84
5039             Color         ...                         32000
5040             Color         ...                            16
5041             Color         ...                           660
5042             Color         ...                           456

[5043 rows x 28 columns]

In [31]: ds.rename({'title_year','year')
   ....: ds.rename({'title_year','year')
   ....: ds.rename({'title_year','year'})
   ....: ds.rename({'title_year':'year'})
   ....: ds.rename('title_year','year')
   ....: ds
   ....: ds.dropna(thresh=5)
   ....: 
In [13]: import matplotlib.pyplot as plt

In [14]: ds.plot()
Out[14]: <matplotlib.axes._subplots.AxesSubplot at 0x7f5a7dba7f50>

In [15]: plt.plot(ds.title_year)
Out[15]: [<matplotlib.lines.Line2D at 0x7f5a7c8bc450>]

In [16]: plt.show()

In [17]:  plt.plot(ds.budget,color="red",linewidth=2.5)
Out[17]: [<matplotlib.lines.Line2D at 0x7f5a79f61fd0>]

In [18]: plt.show()

In [19]: plt.legend(loc='upper left')
/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py:519: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
  warnings.warn("No labelled objects found. "

In [20]:  plt.plot(ds.budget,color="red",linewidth=2.5)
Out[20]: [<matplotlib.lines.Line2D at 0x7f5a79e22910>]

In [21]: plt.show()

In [22]:  plt.plot(ds.budget,color="red",linewidth=2.5)
Out[22]: [<matplotlib.lines.Line2D at 0x7f5a79d5b850>]

In [23]: plt.legend(loc='upper left')
Out[23]: <matplotlib.legend.Legend at 0x7f5a825ee810>

In [24]: plt.show()

In [25]:  plt.plot(ds.title_year,color="red",linewidth=2.5)
Out[25]: [<matplotlib.lines.Line2D at 0x7f5a79ca3a10>]

In [26]: plt.legend(loc='upper left')
Out[26]: <matplotlib.legend.Legend at 0x7f5a79fefd90>

In [27]: plt.show()



