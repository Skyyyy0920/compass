# End-to-end results — `artifacts\devO`

| method | n | Acc | mean score | Pass^2 | Pass@2 | steps | max-steps | refetch/ep | blocked/ep | peak prompt tok | compactions/ep | compressor tok/ep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| compass_v2 | 30 | 66.7% | 0.90 | - | - | 20.3 | 3% | 2.6 | 1.4 | 6923 | 2.2 | 21120 |
| full | 30 | 90.0% | 0.99 | - | - | 20.4 | 0% | 1.9 | 1.2 | 11275 | 0.0 | 0 |
| openclaw | 30 | 76.7% | 0.90 | - | - | 24.1 | 3% | 6.6 | 3.1 | 7047 | 3.1 | 24788 |