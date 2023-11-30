import redis
import time


def measure_redis_performance(host='localhost', port=6379, db=0, num_ops=200_000):
    r = redis.StrictRedis(host=host, port=port, db=db)

    # Flush existing data (optional, be cautious)
    r.flushdb()

    # Measure SET operation performance
    start_time = time.time()
    for i in range(num_ops):
        r.set(f'key_{i}', f'value_{i}')
    end_time = time.time()
    elapsed_time_set = end_time - start_time
    print(f'SET operations: {num_ops} in {elapsed_time_set} seconds')
    print(f'OPS for SET: {num_ops / elapsed_time_set}')

    # Measure GET operation performance
    start_time = time.time()
    for i in range(num_ops):
        value = r.get(f'key_{i}')
    end_time = time.time()
    elapsed_time_get = end_time - start_time
    print(f'GET operations: {num_ops} in {elapsed_time_get} seconds')
    print(f'OPS for GET: {num_ops / elapsed_time_get}')

    # Measure INCR operation performance
    start_time = time.time()
    for i in range(num_ops):
        r.incr(f'counter_{i}')
    end_time = time.time()
    elapsed_time_incr = end_time - start_time
    print(f'INCR operations: {num_ops} in {elapsed_time_incr} seconds')
    print(f'OPS for INCR: {num_ops / elapsed_time_incr}')


if __name__ == "__main__":
    measure_redis_performance()
