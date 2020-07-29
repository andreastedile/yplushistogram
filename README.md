# yPlus Histogram

Inspired by a [Dale Kramer's project](https://www.simscale.com/forum/t/yplus-histogram-program-as-a-new-metric-for-y-mapping-evaluation/85842).

## Installation

Clone the repository and install it with `pip`:

```
git clone https://github.com/andreastedile/yplushistogram
pip install --user .
```

## Usage

With Paraview:

- Use filter `Extract Surface` to extract the surface of the desired object.
- Use filter `Cell Size` and flag Compute Area.
- Open SpreadSheet View, select Cell Data as Attribute.
- The presented spreadsheet should have at least two columns for Area and yPlus.
- Export the spreadsheet in CSV.


Then, open the program with the command line:

```
yplushistogram
```

And open the previously exported CSV file.

![demo](https://github.com/andreastedile/yplushistogram/blob/master/demo.gif)

