class AllMatchesInfo:
    def __init__(self):
        self.parking = None
        self.statute = None
        self.field_verified_document = None
        self.match_info_protocol = None
        self.support_services = None
        self.medical_point = None
        self.stretcher = None
        self.field_fenced = None
        self.secured_passage = None
        self.other_remarks = None


class FourthLeague(AllMatchesInfo):
    def __init__(self):
        super().__init__()
        self.security_director = None
        self.announcer = None


class RegionalLeague(AllMatchesInfo):
    def __init__(self):
        super().__init__()
        self.club_coordinator = None
