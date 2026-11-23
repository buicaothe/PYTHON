# Exercise 4

Use xmlstarlet to print each station name in `week-08/materials/readings.xml` with its latitude and longitude. The station elements belong to the readings vocabulary, and the coordinates belong to the geo vocabulary.

Save the command and it's output in `week-08/student-work/homework/answers/exercise_04.md`.
___________
**ANSWER:**
- CODE: 
```bash
xmlstarlet sel -T \
  -N r="https://example.edu/deai/readings" \
  -N geo="https://example.edu/deai/geo" \
  -t -m "/r:catalog/r:station" \
    -v "r:name" -o " " -v "geo:point/@lat" -o " " -v "geo:point/@lon" -n \
  readings.xml
```
- RESULTS:
```text
Turku 60.45 22.27
Helsinki 60.17 24.94
```