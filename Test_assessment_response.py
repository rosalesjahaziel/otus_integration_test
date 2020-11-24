import json, unittest
from regexValidation import AssessmentIdRegexValidation, AssessmentTypeRegexValidation, AssessmentGradingValidation, AssessmentDistrictValidation, AssessmentTypeNameValidation


class Test_assessment_by_id(unittest.TestCase):
    assessment_id = 202089
    FilePath = "assessmentResponse.json"
    assessments = None

    def setUp(self):
        print ("getting json file")      
        with open(self.FilePath) as json_file:
            data_json = json.loads(json_file.read())
        data = data_json.get("data", {})
        self.assessments = data.get("AssessmentSearch", [])

    def test_response_validation(self):
        print("searching id: " + str(self.assessment_id))
        for assessment in self.assessments:
            if assessment.get("assessment_id", 0) == self.assessment_id:
                print("validating Assesment id format")
                self.assertTrue(AssessmentIdRegexValidation("assessment_id", assessment.get("assessment_id", 0)).validate())
                print("validating Assesment type format")
                self.assertTrue(AssessmentTypeRegexValidation("assessment_type", assessment.get("assessment_type", 0)).validate())
                print("validating Assesment distric format")
                self.assertTrue(AssessmentDistrictValidation("district_id", assessment.get("district_id", 0)).validate())
                print("validating Assesment grading format")
                self.assertTrue(AssessmentGradingValidation("grading_scale_id", assessment.get("grading_scale_id", 0)).validate())
                print("validating Assesment type name format")
                self.assertTrue(AssessmentTypeNameValidation("__typename", assessment.get("__typename", 0)).validate())

    def tearDown(self):
        print ("Ending session")


class Test_assessment_response(unittest.TestCase):
    FilePath = "assessmentResponse.json"
    assessments = None

    def setUp(self):
        print ("getting json file")      
        with open(self.FilePath) as json_file:
            data_json = json.loads(json_file.read())
        data = data_json.get("data", {})
        self.assessments = data.get("AssessmentSearch", [])

    def test_response_validation(self):
        for idx, assessment in enumerate(self.assessments):
            print("\nValidating  assessment Id format: " + str(assessment.get("assessment_id", "")))
            try:                
                self.assertTrue(AssessmentIdRegexValidation("assessment_id", assessment.get("assessment_id", "")).validate())  
            except ValueError as e: 
                self.assertEqual(type(e), ValueError) 

            print ("validating assessment_type")            
            try:                
                self.assertTrue(AssessmentTypeRegexValidation("assessment_type", assessment.get("assessment_type", "")).validate())
            except ValueError as e: 
                self.assertEqual(type(e), ValueError)

            print ("validating district_id") 
            try:                
                self.assertTrue(AssessmentDistrictValidation("district_id", assessment.get("district_id", "")).validate())
            except ValueError as e: 
                self.assertEqual(type(e), ValueError)

            print ("validating grading_scale_id") 
            try:                
                self.assertTrue(AssessmentGradingValidation("grading_scale_id", assessment.get("grading_scale_id", "")).validate())
            except ValueError as e: 
                self.assertEqual(type(e), ValueError)

            print ("validating __typename") 
            try:                
                self.assertTrue(AssessmentTypeNameValidation("__typename", assessment.get("__typename", "")).validate())
            except ValueError as e: 
                self.assertEqual(type(e), ValueError)

    def tearDown(self):
        print ("\nEnding session")

if __name__ == '__main__':
    unittest.main()




