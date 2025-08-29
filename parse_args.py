class Parser():
    def __init__(self, argc, argv):
        self.argv = argv
        self.argc = argc
        self.opts = []
        self.retopts = []

    def run(self, *args):
        for opt in range(self.argc):
            option = self.parse_opts(opt)
            if option != None:
                self.retopts.append(option)

        return self.retopts

    def parse_opts(self, i):
        for j in self.opts:
            if self.argv[i] == j:
                return (j, self.argv[i+1])

    def add_opt(self, *args):
        for i in args:
            self.opts.append(i)