import luigi


# ╔═══════════════════╗ #
# ║   LUIGI CONFIG    ║ #
# ╚═══════════════════╝ #

# ──────────────────────── DATA SERVICES CONFIG ──────────────────────── #


class DataServices(luigi.Config):
    example_variable = luigi.Parameter()


# ╔═══════════════════╗ #
# ║    LUIGI TASKS    ║ #
# ╚═══════════════════╝ #

# ──────────────────────── EXAMPLE TASK 1 ──────────────────────── #


class ExampleTask1(luigi.Task):
    example_variable = DataServices().example_variable

    def output(self):
        raise NotImplementedError

    def requires(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


# ──────────────────────── EXAMPLE TASK 2 ──────────────────────── #


class ExampleTask2(luigi.Task):
    example_variable = DataServices().example_variable

    def output(self):
        raise NotImplementedError

    def requires(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


# ╔═══════════════════╗ #
# ║   WRAPPER TASKS   ║ #
# ╚═══════════════════╝ #

# ──────────────────────── DATA WRAPPER TASKS ──────────────────────── #


class DataTasks(luigi.WrapperTask):
    def requires(self):
        yield ExampleTask1()
        yield ExampleTask2()
