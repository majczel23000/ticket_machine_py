from model.Label import Label
from common.labels_data import labelsData

class LabelFactory:
    def createLabel(self, parent, code, font):
        return Label(parent, code, labelsData[code]['geometry'], font, labelsData[code]['alignment'],labelsData[code][
            'text'])
