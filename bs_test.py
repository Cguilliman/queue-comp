from pystalk import BeanstalkClient
import time


def measure_beanstalkd_performance(host='localhost', port=11300, num_jobs=200_000):
    beanstalk = BeanstalkClient(host=host, port=port)

    # Measure put performance
    start_time = time.time()
    for i in range(num_jobs):
        beanstalk.put_job(f'job_{i}')
    end_time = time.time()
    elapsed_time_put = end_time - start_time
    print(f'Put operations: {num_jobs} in {elapsed_time_put} seconds')
    print(f'OPS for Put: {num_jobs / elapsed_time_put}')

    # Measure reserve performance
    start_time = time.time()
    for i in range(num_jobs):
        job = beanstalk.reserve_job(1)
        beanstalk.delete_job(job.job_id)
    end_time = time.time()
    elapsed_time_reserve = end_time - start_time
    print(f'Reserve operations: {num_jobs} in {elapsed_time_reserve} seconds')
    print(f'OPS for Reserve: {num_jobs / elapsed_time_reserve}')


if __name__ == "__main__":
    measure_beanstalkd_performance()
