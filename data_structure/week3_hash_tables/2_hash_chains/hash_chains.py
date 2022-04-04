# python3

from xml.dom.minidom import Element


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store the hash table as a dictionary
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        
        if query.type == "check":
            try:
                self.elems[query.ind]
            except KeyError:
                self.elems[query.ind] = []
            self.write_chain(self.elems[query.ind])
        else:
            cur_hash_key = self._hash_func(query.s)
            try:
                self.elems[cur_hash_key]
            except KeyError:
                self.elems[cur_hash_key] = []

            if query.type == 'add':
                if query.s not in self.elems[cur_hash_key]:
                    self.elems[cur_hash_key].insert(0, query.s)
            elif query.type == 'find':
                self.write_search_result(query.s in self.elems[cur_hash_key])
            else:
                for i in range(len(self.elems[cur_hash_key])):
                    if self.elems[cur_hash_key][i] == query.s:
                        self.elems[cur_hash_key].pop(i)
                        break

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
