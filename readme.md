
For tests used 200k of messages in every case

| Configuration                    | SET Ops Time (s) | SET Ops/s   | GET Ops Time (s) | GET Ops/s   | INCR Ops Time (s) | INCR Ops/s  |
|----------------------------------|------------------|-------------|------------------|-------------|-------------------|-------------|
| Redis: rdb [save 2 10]           | 26.07            | 7672.19     | 31.52            | 6344.60     | 25.67             | 7790.63     |
| Redis: rdb [save 20 10000]       | 33.71            | 5932.56     | 35.03            | 5709.30     | 31.97             | 6256.77     |
| Redis: aof [appendonly everysec] | 32.65            | 6124.85     | 32.06            | 6239.17     | 33.12             | 6038.65     |
| Beanstalkd                       | 28.40            | 7041.85     | 60.60            | 3300.11     | -                 | -           |
