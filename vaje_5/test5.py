class Vozel:
    """
    Osnovni sestavni del verižnega seznama.
    """
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        if self.naslednji is not None:
            return '{} -> {}'.format(self.podatek, self.naslednji)
        else:
            return '{} -> X'.format(self.podatek)


v = Vozel(1)
w = Vozel(2)
v.naslednji()
print(v.naslednji())

def vrni_seznam(prvi):
    return None