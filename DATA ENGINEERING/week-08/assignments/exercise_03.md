# Exercise 3

Use xmlstarlet to print the catalog `updated` date, then each station name with each reading's date and temperature, in the order the readings appear in `week-08/materials/readings.xml`.

Save the command and its output in `week-08/student-work/homework/answers/exercise_03.md`.

Scroll down for a hint
________________
**ANSWER:**
- code: 
```bash
xmlstarlet sel -t \
  -v "/_:catalog/@updated" -n \
  -m "//_:station/_:reading" \
    -v "../_:name" -o " " \
    -v "@date" -o " " \
    -v "_:temperature" -n readings.xml`
```
- result:
```text
2026-11-12
Turku 2026-11-01 4.2
Turku 2026-11-02 3.5
Helsinki 2026-11-01 2.8
Helsinki 2026-11-02 1.9
```

