class Janken:
    gcp = {"G": 0, "C": 1, "P": 2}

    @classmethod
    def exec(cls, a, b):
        return (cls.gcp[a] - cls.gcp[b]) % 3