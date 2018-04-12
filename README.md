# pyidenticon

A identicon python implementation.

This package is a translation of another identicon project written by golang. Thanks https://github.com/issue9/identicon (Under MIT License).

![./screenshots/many_index_2.png](./screenshots/many_index_2.png)
![./screenshots/many_index_3.png](./screenshots/many_index_3.png)
![./screenshots/many_index_8.png](./screenshots/many_index_8.png)
![./screenshots/many_index_12.png](./screenshots/many_index_12.png)
![./screenshots/many_index_56.png](./screenshots/many_index_56.png)

## Usage

```console
   $ pip install pyindeticon
```


```python
   from pyindenticon import make

   # basic use
   img = make('jeremaihloo')
   img.save('jeremaihloo.png')
   img.close()

   # argb color
   img = make('argb_fore_color.125.200.136', fore_color=(150, 125, 200, 136), bg_color='grey')
   img.save('data/arbb_color.125.200.136.png')
   img.close()

   # named color
   img = make('named_fore_color.blue', fore_color='blue', bg_color='grey')
   img.save('data/named_for_color.blue.png')
   img.close()
```


## Formats

Support `png`, `jpg`, `jpeg`, `bmp` .etc all supported formats by Pillow.

## License

The MIT License (MIT)
Copyright (c) 2018 jeremaihloo
