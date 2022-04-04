# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Worker:
    def __init__(self, id, next_free_time = 0):
        self.id = id
        self.next_free_time = next_free_time


def worker_priority(worker1, worker2):
    if worker1.next_free_time == worker2.next_free_time:
        if worker1.id > worker2.id:
            return True
    elif worker1.next_free_time > worker2.next_free_time:
        return True
    else:
        return False


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    workers = [Worker(_, 0) for _ in range(n_workers)]

    for job in jobs:
        next_worker = workers[0]
        result.append(AssignedJob(next_worker.id, next_worker.next_free_time))
        next_worker.next_free_time += job

        parent, child = 0, 1
        while child < n_workers:
            r_child = child + 1
            if r_child < n_workers:
                if worker_priority(workers[child], workers[r_child]):
                    child = r_child

            if worker_priority(workers[parent], workers[child]):
                workers[parent], workers[child] = workers[child], workers[parent]
                parent = child
                child = 2*parent + 1
            else:
                break

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
