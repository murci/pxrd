# PC-Axis reader for Python

__pxrd__ is a package for reading data from PX (PC-Axis) statistics files. The specifications for the format can be found [here](https://www.scb.se/globalassets/vara-tjanster/px-programmen/px-file_format_specification_2013.pdf).

The pxrd module allows for parsing of keywords and data from PX files at low level. The parser supports KEY based data as well as NO KEY data. Support for __multilanguage__ is implemented.

## Instalation

```
pip install pxrd
```

## Pandas integration

There's an additional module in the package that allows for conversion to Pandas DataFrame. It's separated to avoid direct dependency to pandas if it's not required.

To read files into a Pandas DataFrame:
```python
import pxrd
from pxrd.pandas import to_pandas

px = pxrd.read('/path/to/pxfile.px')
df = to_pandas(px, categories=True, multiindex=True)
```

When converting to Pandas there are two options:
* __categories__ (default: True): if True, the resulting DataFrame uses Categorical dtype for the stub and heading columns/indexes. Else, it uses zero based indexes into the dimension values/codes.
* __multiindex__ (default: False): if True, the generated DataFrame uses Pandas MultiIndex. Else is a regular DataFrame with stub and headings as columns.


## Command Line Interface

The packages installs a command line shortcut for converting PC-Axis files to CSV. It supports multilanguage PC-Axis files.

```
$ px2csv [-h] [--languages] [--language LANGUAGE] filename
```

Use the ```--languages``` options to obtain a list of available languages and ```--language LAMGUAGE``` to specify the selected language. If no language is specified, the default language is used.


## Low level usage

First, you use read() to parse the PX-File. If you obtain the file via requests or any other mean, you can use reads() and provide the string contents of the file. Both functions return
a PxFile object you can use to query the contents of the file.

```
PxFile.keywords()
```
Returns a list of the keywords found in the file, excluding "DATA"

```
PxFile.language()
```
Returns the default language of the file, None if it's not defined

```
PxFile.languages()
```
Returns the list of languages available in the file

```
PxFile.keyword(keyword, subkey=None, language=None) 
```
Returns the value of the specified keyword in the specfied language or default if None. If a keyword has a subkey you cam query it using the subkey parameter

```
PxFile.variables(language=None)
```
Returns the dimensions of the cube (stub + headings) in the specified language or default if None

```
PxFile.values(variable, language=None)
```
Returns the values for the dimension (or variable) usign the language indicated or the default if None

```
PxFile.codes(variable, language=None)
```
Returns the codes for the dimension (or variable) usign the language indicated or the default if None. If there are no codes, it returns the same values as "values()"

```
PxFile.datum(index)
```
Returns the value for the specified index of the cube. The index must be in the forma of a list containing the integer indexes of the values/codes of the variable. 
The order of the dimensions/variables in the index is the same as returned by "variables()".