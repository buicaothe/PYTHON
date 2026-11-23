# Exercise 1

1. Use xmlstarlet to check that `week-08/materials/readings.xml` is well-formed.

2. Use xmlstarlet to print each different element path in `week-08/materials/readings.xml` once, including the attributes.

Save the command and its output in `week-08/student-work/homework/answers/exercise_01.md`.
______________
**ANSWERS:**
1. well-formed:
   * coomands: `xmlstarlet val readings.xml`
   * Result:  `readings.xml - valid`
2. print each different element path:
  * commands: 
```bash
xmlstarlet el -a readings.xml | sort -u
```

  * Results:
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