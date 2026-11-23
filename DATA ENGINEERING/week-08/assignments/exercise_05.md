# Exercise 5

Turku Airport observations from FMI are station `101065`, in ten-minute steps. The file is `week-08/assignments/turku-airport-obs.xml`.

Use xmlstarlet on `week-08/assignments/turku-airport-obs.xml` before you extract values.

1. List the element structure.
2. Find which tags and attributes carry temperature
3. Note how the times are written.

Then use xmlstarlet to extract hourly temperature over the file.

Save the command and it's output in `week-08/student-work/homework/answers/exercise_05.md`.
______
**ANSWER:**
* Code:
```bash
xmlstarlet sel -N omso="http://inspire.ec.europa.eu/schemas/omso/3.0" -N om="http://www.opengis.net/om/2.0" -N wml2="http://www.opengis.net/waterml/2.0" -t -m "//omso:PointTimeSeriesObservation[contains(om:observedProperty/@xlink:href, 'param=temperature')]//wml2:MeasurementTVP[contains(wml2:time, ':00:00Z')]" -v "wml2:time" -o " " -v "wml2:value" -n turku-airport-obs.xml
```
* Results:
```text
2026-11-09T23:00:00Z 4.8
2026-11-10T00:00:00Z 5.3
2026-11-10T01:00:00Z 5.3
2026-11-10T02:00:00Z 5.6
2026-11-10T03:00:00Z 5.9
2026-11-10T04:00:00Z 6.0
2026-11-10T05:00:00Z 5.8
2026-11-10T06:00:00Z 5.3
2026-11-10T07:00:00Z 5.5
2026-11-10T08:00:00Z 5.8
2026-11-10T09:00:00Z 6.2
2026-11-10T10:00:00Z 6.5
```