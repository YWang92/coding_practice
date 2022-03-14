# python3

from collections import namedtuple
import math
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    workers = [_ for _ in range(n_workers)]
    last_parent_id = math.floor(n_workers/2) - 1

    for job in jobs:
        next_worker = workers[0]
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
        # update the priority queue using SiftDown
        for i in range(last_parent_id + 1):
            parent_id = i
            while parent_id <= last_parent_id:
                lchild_id, rchild_id = 2*parent_id + 1, 2*parent_id + 2
                
                t1, t2 = next_free_time[workers[parent_id]], next_free_time[workers[lchild_id]]

                if rchild_id > n_workers - 1:
                    t3 = t1 + t2 + 10
                else:
                    t3 = next_free_time[workers[rchild_id]]
                
                if t2 < t3:
                    if t1 > t2 or (t1 == t2 and workers[parent_id] > workers[lchild_id]):
                        workers[parent_id], workers[lchild_id] = workers[lchild_id], workers[parent_id]
                        parent_id = lchild_id
                    else:
                        break
                elif t3 < t2:
                    if t1 > t3 or (t1 == t3 and workers[parent_id] > workers[rchild_id]):
                        workers[parent_id], workers[rchild_id] = workers[rchild_id], workers[parent_id]
                        parent_id = rchild_id
                    else:
                        break
                else:
                    if workers[lchild_id] < workers[rchild_id]:
                        if t1 > t2 or (t1 == t2 and workers[parent_id] > workers[lchild_id]):
                            workers[parent_id], workers[lchild_id] = workers[lchild_id], workers[parent_id]
                            parent_id = lchild_id
                        else:
                            break
                    elif workers[rchild_id] < workers[lchild_id]:
                        if t1 > t3 or (t1 == t3 and workers[parent_id] > workers[rchild_id]):
                            workers[parent_id], workers[rchild_id] = workers[rchild_id], workers[parent_id]
                            parent_id = rchild_id
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
