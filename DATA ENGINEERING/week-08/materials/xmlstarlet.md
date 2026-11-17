# Selecting from XML with xmlstarlet

`xmlstarlet` reads an XML file from the shell. This note uses `week-08/materials/readings.xml`. The shape of that file is explained in `xml.md`.

Run the commands from `week-08/materials`, so the file name is `readings.xml`. Check that the program is installed:

```bash
xmlstarlet --version
```

These examples were run with xmlstarlet 1.6.1. Put single quotes around each path. The shell then passes the path to xmlstarlet unchanged.

## 1. Check that the file parses

```bash
xmlstarlet val readings.xml
```

```text
readings.xml - valid
```

With no schema, this checks that the file is well-formed.

## 2. See the element tree

`el` prints a path for every element, from the root down to that element. A path that occurs twice in the file is printed twice. Turku has two readings and Helsinki has two, so `catalog/station/reading` appears four times.

```bash
xmlstarlet el readings.xml
```

```text
catalog
catalog/station
catalog/station/name
catalog/station/geo:point
catalog/station/reading
catalog/station/reading/temperature
catalog/station/reading/rainfall
catalog/station/reading
catalog/station/reading/temperature
catalog/station/reading/rainfall
catalog/station
catalog/station/name
catalog/station/geo:point
catalog/station/reading
catalog/station/reading/temperature
catalog/station/reading/rainfall
catalog/station/reading
catalog/station/reading/temperature
catalog/station/reading/rainfall
```

`-u` prints each different path once. Use this when you want the shape, rather than one line per reading.

```bash
xmlstarlet el -u readings.xml
```

```text
catalog
catalog/station
catalog/station/geo:point
catalog/station/name
catalog/station/reading
catalog/station/reading/rainfall
catalog/station/reading/temperature
```

`-a` adds attributes. An attribute is written with `@` on the element it belongs to. `el -a` repeats a path once per element, the same way `el` does. `sort -u` leaves each path once.

```bash
xmlstarlet el -a readings.xml | sort -u
```

```text
catalog
catalog/@updated
catalog/@xmlns
catalog/@xmlns:geo
catalog/station
catalog/station/@id
catalog/station/geo:point
catalog/station/geo:point/@lat
catalog/station/geo:point/@lon
catalog/station/name
catalog/station/reading
catalog/station/reading/@date
catalog/station/reading/rainfall
catalog/station/reading/rainfall/@unit
catalog/station/reading/temperature
catalog/station/reading/temperature/@unit
```

`catalog/@updated` is the date on the root. `catalog/station/@id` is `turku` or `helsinki`. `catalog/station/reading/@date` is the day of that reading.

## 3. How a select command is built

`xmlstarlet sel` walks the document with a template.

| Piece | Meaning |
| --- | --- |
| `-T` | Print plain text |
| `-N prefix=url` | Bind a prefix to a namespace URL |
| `-t` | Start the output template |
| `-m "xpath"` | Visit each node the path matches |
| `-v "xpath"` | Print the text of a node, or the value of an attribute |
| `-o " "` | Print the characters between the quotes |
| `-n` | Print a newline |
| `-c "xpath"` | Print a copy of the matched XML |

A path after `-m` starts from the document. A path after that `-m` starts from the node `-m` just visited. `@date` means the `date` attribute of the current element.

## 4. Bind the namespaces

The elements with no prefix in the file belong to the default namespace, `https://example.edu/deai/readings`. A query has to give that URL a prefix. This note uses `r`. The prefix in the query is a nickname for the URL. It does not have to be the prefix written in the file.

`geo:point` belongs to `https://example.edu/deai/geo`. Bind that URL to `geo` when a query reads coordinates.

```bash
-N r="https://example.edu/deai/readings" -N geo="https://example.edu/deai/geo"
```

## 5. Read values

How many stations:

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -v "count(/r:catalog/r:station)" -n \
  readings.xml
```

```text
2
```

The station names. `-m` visits each station, and `-v "r:name"` prints the name from there.

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -m "/r:catalog/r:station" -v "r:name" -n \
  readings.xml
```

```text
Turku
Helsinki
```

The date on the catalog is an attribute of the root:

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -v "/r:catalog/@updated" -n \
  readings.xml
```

```text
2026-11-12
```

Turku's temperatures, with the day and the unit. `[@id='turku']` keeps the station whose `id` attribute is `turku`. From each reading, `@date` is the day, `r:temperature` is the number, and `r:temperature/@unit` is the attribute on that element.

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -m "/r:catalog/r:station[@id='turku']/r:reading" \
    -v "@date" -o " " -v "r:temperature" -o " " -v "r:temperature/@unit" -n \
  readings.xml
```

```text
2026-11-01 4.2 C
2026-11-02 3.5 C
```

Every temperature above 3. xmlstarlet reads the element text as a number for `>`. `-m` visits each matching `reading`. `..` is the `station` that contains it, so `../r:name` is that station's name.

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -m "//r:reading[r:temperature > 3]" \
    -v "../r:name" -o " " -v "@date" -o " " -v "r:temperature" -n \
  readings.xml
```

```text
Turku 2026-11-01 4.2
Turku 2026-11-02 3.5
```

The day with no rain. The rainfall text in the file is `0.0`, so the test matches those characters.

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -t -m "//r:reading[r:rainfall='0.0']" \
    -v "../r:name" -o " " -v "@date" -n \
  readings.xml
```

```text
Turku 2026-11-02
```

Coordinates need the second namespace. `@lat` and `@lon` are attributes of `geo:point`.

```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -N geo="https://example.edu/deai/geo" \
  -t -m "/r:catalog/r:station" \
    -v "r:name" -o " " -v "geo:point/@lat" -o " " -v "geo:point/@lon" -n \
  readings.xml
```

```text
Turku 60.45 22.27
Helsinki 60.17 24.94
```

`local-name()` matches an element by its name and ignores the namespace. This prints every temperature with no `-N`. Use the prefixed paths above when two vocabularies could contain the same element name.

```bash
xmlstarlet sel -T \
  -t -m "//*[local-name()='temperature']" -v "." -n \
  readings.xml
```

```text
4.2
3.5
2.8
1.9
```

## 6. Copy one element

`-c` prints the XML of a match, instead of only its text. Leave off `-T` so the tags stay tags. `-I` indents them. This is Turku's first reading. `[1]` means the first match.

```bash
xmlstarlet sel -I \
  -N r="https://example.edu/deai/readings" \
  -t -c "/r:catalog/r:station[@id='turku']/r:reading[1]" \
  readings.xml
```

```xml
<reading xmlns="https://example.edu/deai/readings" xmlns:geo="https://example.edu/deai/geo" date="2026-11-01">
      <temperature unit="C">4.2</temperature>
      <rainfall unit="mm">1.1</rainfall>
    </reading>
```

The copied element repeats the namespace declarations from the root, so the fragment still says which vocabulary `reading` belongs to.
