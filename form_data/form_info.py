class AllMatchesInfo:
    def __init__(self):
        self._parking = None
        self._statute = None
        self._field_verified_document = None
        self._match_info_protocol = None
        self._support_services = None
        self._medical_point = None
        self._stretcher = None
        self._field_fenced = None
        self._secured_passage = None
        self._other_remarks = None

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, parking):
        self._parking = parking

    @property
    def statute(self):
        return self._statute

    @statute.setter
    def statute(self, statute):
        self._statute = statute

    @property
    def field_verified_document(self):
        return self._field_verified_document

    @field_verified_document.setter
    def field_verified_document(self, field_verified_document):
        self._field_verified_document = field_verified_document

    @property
    def match_info_protocol(self):
        return self._match_info_protocol

    @match_info_protocol.setter
    def match_info_protocol(self, match_info_protocol):
        self._match_info_protocol = match_info_protocol

    @property
    def support_services(self):
        return self._support_services

    @support_services.setter
    def support_services(self, support_services):
        self._support_services = support_services

    @property
    def medical_point(self):
        return self._medical_point

    @medical_point.setter
    def medical_point(self, medical_point):
        self._medical_point = medical_point

    @property
    def stretcher(self):
        return self._stretcher

    @stretcher.setter
    def stretcher(self, stretcher):
        self._stretcher = stretcher

    @property
    def field_fenced(self):
        return self._field_fenced

    @field_fenced.setter
    def field_fenced(self, field_fenced):
        self._field_fenced = field_fenced

    @property
    def secured_passage(self):
        return self._secured_passage

    @secured_passage.setter
    def secured_passage(self, secured_passage):
        self._secured_passage = secured_passage

    @property
    def other_remarks(self):
        return self._other_remarks

    @other_remarks.setter
    def other_remarks(self, other_remarks):
        self._other_remarks = other_remarks


class FourthLeague(AllMatchesInfo):
    def __init__(self):
        super().__init__()
        self._security_director = None
        self._announcer = None

    @property
    def security_director(self):
        return self._security_director

    @security_director.setter
    def security_director(self, security_director):
        self._security_director = security_director

    @property
    def announcer(self):
        return self._announcer

    @announcer.setter
    def announcer(self, announcer):
        self._announcer = announcer


class RegionalLeague(AllMatchesInfo):
    def __init__(self):
        super().__init__()
        self._club_coordinator = None

    @property
    def club_coordinator(self):
        return self._club_coordinator

    @club_coordinator.setter
    def club_coordinator(self, club_coordinator):
        self._club_coordinator = club_coordinator
