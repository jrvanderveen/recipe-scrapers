from ._abstract import AbstractScraper


class Tasty(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasty.co"

    def title(self):
<<<<<<< HEAD
        return self.schema.title()
=======
        return self.schema.title().replace(" Recipe by tasty", "")
>>>>>>> 58dcae1... Added tasty.co parser

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
<<<<<<< HEAD
        return self.schema.instructions()
=======
        return self.schema.instructions().replace("\n", "")
>>>>>>> 58dcae1... Added tasty.co parser

    def ratings(self):
        return self.schema.ratings()
