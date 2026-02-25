from collections import defaultdict
from dataset import load_dataset, prune
class WordLadderSolver:

    def __init__(self, words, number_of_changes=1, number_of_guesses=10):
        self.words = words
        self.number_of_changes = number_of_changes
        self.number_of_guesses = number_of_guesses
        self.buckets = self._build_buckets(words, number_of_changes)

    def _build_buckets(self, words, number_of_changes):
        buckets = defaultdict(list)

        for word in self.words:
            for bucket_key in self._get_bucket_keys(word, number_of_changes):
                buckets[bucket_key].append(word)
        return buckets

    def _get_bucket_keys(self, word, number_of_changes):
        bucket_keys = []
        if number_of_changes > len(word) or number_of_changes < 0:
            return []

        if number_of_changes == 0:
            return [word]

        if number_of_changes == len(word):
            return ["*" * len(word)]

        for i in range(len(word) - number_of_changes + 1): #Only go up to the max changes
            for b in self._get_bucket_keys(word[i+1:], number_of_changes - 1 ):
                bucket_keys.append(word[:i] + "*" + b)

        return bucket_keys


    def _is_near(self, original, number_of_changes):
        for bucket in self._get_bucket_keys(original, self.number_of_changes):
            for word in self.buckets.get(bucket, []):
                if word != original:
                    yield word

    def solve_fully(self, start, end):
        if start == end:
            return [start]

        if self.number_of_changes > len(start) or self.number_of_changes < 0:
            raise Exception("Number of changes must be between 0 and the length of the word")

        paths = defaultdict(list)
        current_level = {start}
        visited = set({start})
        depth = 1

        while current_level and depth <= self.number_of_guesses:
            next_level = set()
            for word in current_level:
                for near in self._is_near(word, number_of_changes=self.number_of_changes):
                    if near not in visited:
                        paths[near].append(word)
                        visited.add(near)
                        if near != end:
                            next_level.add(near)

            current_level = next_level
            depth += 1

        def reconstruct_path(curr, path):
            if len(path) > self.number_of_guesses:
                return

            if curr == start:
                yield path[::-1]

            for word in paths[curr]:
                yield from reconstruct_path(word, path + [word])

        yield from reconstruct_path(end, [end])

org_dataset = load_dataset()
ds = prune(4, org_dataset)
wordladder = WordLadderSolver(ds)
path = wordladder.solve_fully("need", "seam")
lst = [p for p in path]
print(lst)