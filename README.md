# MNIST Stroke Data

The following dataset contains the MNIST dataset in stroke/point form. The data in this repository was based on the data obtained from the following project: https://github.com/edwin-de-jong/mnist-digits-stroke-sequence-data

The data is supplied in the JSON format and contained in the `strokes` directory. Each file follows the following format: `sample-<digit>-<sample-number>.json.`

For example, in the file: `sample-3-1970.json`:

```json 
{
   "count":2,
   "instance":1970,
   "digit":"3",
   "strokes":[
      [
         {
            "y":5,
            "x":12
         },
         {
            "y":6,
            "x":13
         },
         {
            "y":6,
            "x":14
         },
         {
            "y":6,
            "x":15
         },
         {
            "y":6,
            "x":16
         },
         {
            "y":7,
            "x":17
         },
         {
            "y":8,
            "x":17
         },
         {
            "y":9,
            "x":16
         },
         {
            "y":10,
            "x":16
         },
         {
            "y":11,
            "x":16
         },
         {
            "y":12,
            "x":16
         },
         {
            "y":12,
            "x":15
         },
         {
            "y":12,
            "x":14
         },
         {
            "y":12,
            "x":13
         },
         {
            "y":13,
            "x":12
         },
         {
            "y":13,
            "x":12
         }
      ],
      [
         {
            "y":13,
            "x":17
         },
         {
            "y":13,
            "x":18
         },
         {
            "y":13,
            "x":19
         },
         {
            "y":14,
            "x":19
         },
         {
            "y":15,
            "x":19
         },
         {
            "y":16,
            "x":19
         },
         {
            "y":17,
            "x":19
         },
         {
            "y":18,
            "x":19
         },
         {
            "y":19,
            "x":18
         },
         {
            "y":20,
            "x":17
         },
         {
            "y":21,
            "x":16
         },
         {
            "y":22,
            "x":15
         },
         {
            "y":22,
            "x":14
         },
         {
            "y":22,
            "x":13
         },
         {
            "y":22,
            "x":12
         },
         {
            "y":22,
            "x":11
         },
         {
            "y":22,
            "x":10
         },
         {
            "y":22,
            "x":9
         },
         {
            "y":22,
            "x":8
         },
         {
            "y":22,
            "x":7
         },
         {
            "y":22,
            "x":7
         }
      ]
   ]
}
```

If a given symbol has more than one stroke it is represented by having more than one array of `x` and `y` dictionaries. This information mas also be obtained via the top level `count` attribute. 

Other attributes:

- `digit` - the digit this set of strokes represents
- `instance` - the example number
- `strokes`  - an array of arrays of JSON dictionaries of points. 


# Building the Data Set

To build the dataset, execute the script `strokedata.py` contained in the root of this distribution. 


<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-88910845-1', 'auto');
  ga('send', 'pageview');

</script>
