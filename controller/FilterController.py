from math import ceil

from PyQt5.QtCore import QObject, pyqtSlot

from utils.Constants import MATCH, NON_MATCH, NOT_SURE, COUNT_PER_PAGE, ALL
from view import Renderer


class FilterController(QObject):
    def __init__(self, main_page, data_frame):
        super(FilterController, self).__init__(None)
        self.main_page = main_page
        assert ('label' in data_frame.columns)
        self.data_frame = data_frame

    @pyqtSlot(str)
    def get_matching_tuple_pairs(self):
        """Gets tuple pairs whose label value is currently "MATCH"

        :param
            dataFrame: Data Frame consisting of matched and non-matched tuple pairs
        :return:
            Data frame with tuple pairs whose label value is currently NON-MATCH
        """
        # todo check data type of label column
        return self.data_frame[self.data_frame.label == MATCH]

    @pyqtSlot()
    def get_non_matched_tuple_pairs(self):
        """Gets tuple pairs whose label value is currently NON-MATCH

        :param
            dataFrame: Data Frame consisting of matched and non-matched tuple pairs
        :return:
            Data frame with tuple pairs whose label value is currently NON-MATCH
        """
        # todo check if assertion is correct thing to do
        return self.data_frame[self.data_frame.label == NON_MATCH]

    @pyqtSlot()
    def get_non_sure_tuple_pairs(self):
        """Gets tuple pairs whose label value is currently NON-MATCH

        :param
            dataFrame: Data Frame consisting of matched and non-matched tuple pairs
        :return:
            Data frame with tuple pairs whose label value is currently NON-MATCH
        """
        # todo check data type of label column
        return self.data_frame[self.data_frame.label == NOT_SURE]

    @pyqtSlot(str)
    def get_filtered_tuple_pairs(self, label):
        data = None
        if (label == MATCH):
            data = self.get_matching_tuple_pairs()
        elif (label == NON_MATCH):
            data = self.get_non_matched_tuple_pairs()
        elif (label == NOT_SURE):
            data = self.get_non_sure_tuple_pairs()
        elif (label == ALL):
            data = self.data_frame

        self.main_page.setHtml(
            Renderer.render_main_page(data, 1, COUNT_PER_PAGE, ceil(data.shape[0] / COUNT_PER_PAGE),
                                      self.data_frame[self.data_frame.label == MATCH].shape[0],
                                      self.data_frame[self.data_frame.label == NON_MATCH].shape[0],
                                      self.data_frame[self.data_frame.label == NOT_SURE].shape[0],
                                      self.data_frame.shape[0], label + " tuple pairs"))