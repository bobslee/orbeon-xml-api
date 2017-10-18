class RunnerBuilderMerge:

    def __init__(self, runner, builder):
        self.runner = runner
        self.builder = builder

    # TODO move Runner merge() implementation to this function.
    def merge(self):
        return self.runner.merge(self.builder)
