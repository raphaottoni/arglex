import re
from Assessments import Assessments
from Authority import Authority
from Causation import Causation
from Conditionals import Conditionals
from Contrast import Contrast
from Difficulty import Difficulty
from Doubt import Doubt
from Emphasis import Emphasis
from Generalization import Generalization
from Inconsistency import Inconsistency
from Inyourshoes import Inyourshoes
from Necessity import Necessity
from Possibility import Possibility
from Priority import Priority
from Rhetoricalquestion import Rhetoricalquestion
from Structure import Structure
from Wants import Wants
from Priority import Priority

# class that will count Assessments lexicons
class Classifier:

  #constructor
  def __init__(self):
    self.assessments = Assessments()
    self.authority = Authority()
    self.causation = Causation()
    self.conditionals = Conditionals()
    self.contrast = Contrast()
    self.difficulty = Difficulty()
    self.doubt = Doubt()
    self.emphasis = Emphasis()
    self.generalization = Generalization()
    self.inconsistency = Inconsistency()
    self.inyourshoes = Inyourshoes()
    self.necessity = Necessity()
    self.possibility = Possibility()
    self.priority = Priority()
    self.rhetoricalquestion = Rhetoricalquestion()
    self.structure = Structure()
    self.wants = Wants()
    self.priority = Priority()


  # function to count Assessments n-grams from text
  def analyse(self,text):

    result = []

    # counter of ngrams matched
    ngrams = 0

    # Analyse the text for each category
    result.append(self.assessments.analyse(text))
    result.append(self.authority.analyse(text))
    result.append(self.causation.analyse(text))
    result.append(self.conditionals.analyse(text))
    result.append(self.contrast.analyse(text))
    result.append(self.difficulty.analyse(text))
    result.append(self.doubt.analyse(text))
    result.append(self.emphasis.analyse(text))
    result.append(self.generalization.analyse(text))
    result.append(self.inconsistency.analyse(text))
    result.append(self.inyourshoes.analyse(text))
    result.append(self.necessity.analyse(text))
    result.append(self.possibility.analyse(text))
    result.append(self.priority.analyse(text))
    result.append(self.rhetoricalquestion.analyse(text))
    result.append(self.structure.analyse(text))
    result.append(self.wants.analyse(text))
    result.append(self.priority.analyse(text))

    return result


