class OtherRemarksTableData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OtherRemarksTableData, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.counter = 0
            self.description = ""
            self.other_remarks_text = ""
            self._initialized = True

    def set_counter(self, counter):
        self.counter = counter

    def set_description(self, description):
        self.description = description

    def set_other_remarks(self, other_remarks_text):
        self.other_remarks_text = other_remarks_text

    def other_remarks_table_data(self):
        return [([self.counter, self.description, self.other_remarks_text])]
