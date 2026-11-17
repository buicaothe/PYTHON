# XML

`week-08/materials/readings.xml` is the XML file used in this note and in `xmlstarlet.md`.

## JSON versus XML

JSON and XML both write structured data as text. A program can read either one back into records.

### A JSON object and the same facts in XML

This JSON object is one station on one day. The keys are `station`, `date`, `temperature`, and `rainfall`. `readings` would be a list if there were several days. Here there is one day, so the list has one object.

```json
{
  "station": "Turku",
  "id": "turku",
  "date": "2026-11-01",
  "temperature": 4.2,
  "rainfall": 1.1
}
```

The same facts as XML:

```xml
<station id="turku">
  <name>Turku</name>
  <reading date="2026-11-01">
    <temperature unit="C">4.2</temperature>
    <rainfall unit="mm">1.1</rainfall>
  </reading>
</station>
```

The pieces line up like this.

| JSON | In the XML above |
| --- | --- |
| An object `{ ... }` | An element that contains other elements: `<station>...</station>` |
| A key | The name of an element, or the name of an attribute |
| A string or a number | The text between a start tag and an end tag |
| A list `[ ... ]` | The same element repeated once per item |

JSON writes `4.2` as a number. XML writes the characters `4.2` between tags. A program that reads the XML can turn those characters back into a number.

`id="turku"` and `unit="C"` are attributes. An attribute sits inside the start tag and names one fact about that element. JSON has no attributes, so the same fact would be another key, for example `"unit": "C"`.

## The sample file

`readings.xml` is two stations, Turku and Helsinki, with two days each. The top of the file is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<catalog xmlns="https://example.edu/deai/readings"
         xmlns:geo="https://example.edu/deai/geo"
         updated="2026-11-12">
```

`<?xml ...?>` says the file is XML and the text is UTF-8. `<catalog>` is the root. One XML document has one root element, and everything else sits inside it.

A comment is text for a person. A program skips it.

```xml
<!-- Two stations, two days each. -->
```

## Elements, text, and attributes

An element is a start tag, the content, and the end tag. The end tag repeats the name with a slash.

```xml
<name>Turku</name>
```

`name` is the element name. `Turku` is the text.

Elements nest. A `station` contains a `name` and two `reading` elements. A `reading` contains `temperature` and `rainfall`. The date belongs to the reading, so it is an attribute of that element:

```xml
<reading date="2026-11-01">
  <temperature unit="C">4.2</temperature>
  <rainfall unit="mm">1.1</rainfall>
</reading>
```

An element with nothing inside it can be written as one tag that closes itself. The coordinates are that kind of element. The numbers are attributes.

```xml
<geo:point lat="60.45" lon="22.27"/>
```

## A list stays in order

A JSON list keeps the order of its items. XML does the same by repeating an element. In the file, Turku's 1 November reading comes before the 2 November reading, because that is the order of the two `<reading>` elements.

```xml
<reading date="2026-11-01">...</reading>
<reading date="2026-11-02">...</reading>
```

Helsinki is a second `<station>`, after Turku, for the same reason.

## Two vocabularies in one file

A name on its own can mean two things. Here both elements are called `point`. One is a label, the other is a coordinate.

```xml
<station>
  <point>city centre</point>
  <point lat="60.45" lon="22.27"/>
</station>
```

A namespace gives each vocabulary its own long name, which is a URL. The prefix in front of a tag is a short local nickname for that URL. `geo:point` is the `point` from the vocabulary `https://example.edu/deai/geo`. The label stays an ordinary `point`.

```xml
<station xmlns:geo="https://example.edu/deai/geo">
  <point>city centre</point>
  <geo:point lat="60.45" lon="22.27"/>
</station>
```

The URL identifies the vocabulary. It does not have to be a page that exists. The prefix is chosen in this file. Another file can bind the same URL to a different prefix, and the elements are still the same vocabulary.

`readings.xml` uses two vocabularies. The line `xmlns="https://example.edu/deai/readings"` is the default namespace. An element with no prefix, such as `<station>` and `<temperature>`, belongs to that vocabulary. The line `xmlns:geo="https://example.edu/deai/geo"` binds the prefix `geo`. Only `<geo:point>` belongs to the second vocabulary.

Attributes in this file, such as `id`, `date`, `unit`, `lat`, and `lon`, have no prefix. They belong to the element they sit on.

## A tag inside a sentence

XML can mix text and elements in one parent. This note is a sentence, and the place name is its own element inside that sentence.

```xml
<note>Rain in <place>Turku</place> was light.</note>
```

The parent has three parts in order: the text `Rain in `, the element `place`, and the text ` was light.` This kind of mix is what XML was built for. The sample file does not use it. The readings are records, and each value is a whole element.

## Well-formed XML, and a schema

A file is well-formed when the tags fit together. Every start tag has an end tag, the root is the only outermost element, and each attribute value is in quotes.

This fragment is not well-formed. The `temperature` element never closes, and `unit` has no quotes.

```xml
<temperature unit=C>4.2
```

A well-formed file can still hold the wrong kind of value. This element is well-formed, and `warm` is not a temperature a chart can plot.

```xml
<temperature unit="C">warm</temperature>
```

A schema is a second file that lists the elements a document is allowed to use and what kind of text they may contain. Checking the document against that schema rejects `warm` even though the tags themselves are fine. This course stops at reading the XML. The schema check is the reason publishers of large XML feeds can say what a correct file looks like.

## XPath

XPath is the path language inside `xmlstarlet sel`. A path names a place in the XML tree. `-m` visits each node the path matches. `-v` prints the text at a path.

A path is a chain of steps. A `/` at the start means the document root. Each later `/` steps down to a child. `/r:catalog/r:station/r:name` starts at the catalog, enters a station, and stops at that station's name. `//` finds a matching element anywhere below the current point, so `//r:temperature` is every temperature in the file. From the node you are on, `.` is that node and `..` is its parent. `../r:name` on a reading is the station name above it.

`@` is the attribute axis. It steps to an attribute of the current element. `@date` is the date on a reading. `r:temperature/@unit` is the unit attribute on the temperature element.

Brackets are a predicate. They keep a node when the test inside is true. `r:station[@id='turku']` keeps the station whose `id` is `turku`. `r:reading[r:temperature > 3]` keeps a reading whose temperature is greater than 3. `r:reading[r:rainfall='0.0']` keeps a reading whose rainfall text is those characters. A number in brackets is a position: `r:reading[1]` is the first reading.

`/r:catalog/r:station/r:reading[r:rainfall]/r:rainfall` uses the bracket as a filter, then steps into the rainfall child. `-v` on that path prints the rainfall text only.

A step with a prefix matches an element in that namespace. In `readings.xml` the elements with no prefix belong to `https://example.edu/deai/readings`, so a query names them `r:catalog` and `r:station` after `-N r="https://example.edu/deai/readings"`. `geo:point` belongs to `https://example.edu/deai/geo`, so a coordinate path binds `geo` as well. The prefix in the path is a nickname for the URL. It can differ from the prefix written in the file.
