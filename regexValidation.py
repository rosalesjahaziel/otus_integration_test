import re

class FieldValidator:

    regex = ""
    def __init__(self, field_name, field_value):
        self.field_name = field_name
        self.field_value = field_value

    def regex_validate(self):
        if self.regex:
            
            if(re.search(self.regex, str(self.field_value))):
                return True
        return False
        
    def type_validate(self):
        return True
    
    def length_validate(self):
        return True

    def validate(self):
        if self.field_value:
            if self.regex_validate() and self.type_validate() and self.length_validate():
                return True
        return False

class EmailRegexValidation(FieldValidator):
    regex = '^[a-z0-9]+[\._\-]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class NamesRegexValidation(FieldValidator):
    regex = '^[a-zA-Z\']*$'

class GradeRegexValidation(FieldValidator):
    regex = '^[0-5][\.][0,5]|[0-5]$'

class AssessmentIdRegexValidation(FieldValidator):
    regex = '^[0-9]{5,6}$'

class AssessmentTypeRegexValidation(FieldValidator):
    regex = '^[2,3]$'

class AssessmentDistrictValidation(FieldValidator):
    regex = '^85623$'

class AssessmentGradingValidation(FieldValidator):
    regex = '^751$'

class AssessmentTypeNameValidation(FieldValidator):
    regex = '^AssessmentSearch$'