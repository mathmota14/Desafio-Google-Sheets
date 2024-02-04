import os.path
import math

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SAMPLE_SPREADSHEET_ID = "13K1VCIX41I8HVpdllr_9Si6jhUVhL7awRkBRrVhcYnY"
SAMPLE_RANGE_NAME = "engenharia_de_software!A2:H27"

def main():
    # The credentials are used to be able to log in to the account
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port = 0)
        
        # A token file will be created the first time you use   
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials = creds)

        sheet = service.spreadsheets()
        # A dictionary with informations about the spreadsheet
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range = SAMPLE_RANGE_NAME)
            .execute()
        )
        # A list of lists containing the spreadsheet rows
        values = result["values"]
        # Getting the total number of classes in the semester
        number_of_classes = values[0][0]
        number_of_classes = int(number_of_classes.replace("Total de aulas no semestre: ", ""))
        # Removing the first two rows of the spreadsheet as it doesn't contain the students information
        students_information = values[2:]

        # The number of absences that the student can't exceed
        max_absence = int(number_of_classes * 0.25)
        # A list containing the situation of the student
        situation = []
        # A list containing the arithmetic mean of each student
        total_arithmetic_mean = []

        # Check how the student’s situation will be
        for i in students_information:
            student_absence = int(i[2])
            student_arithmetic_mean = (int(i[3]) + int(i[4]) + int(i[5])) / 3

            if student_absence > max_absence:
                situation.append(["Reprovado por Falta"])
                total_arithmetic_mean.append(student_arithmetic_mean)

            elif student_arithmetic_mean >= 70:
                situation.append(["Aprovado"])
                total_arithmetic_mean.append(student_arithmetic_mean)

            elif 50 <= student_arithmetic_mean < 70:
                situation.append(["Exame Final"])
                total_arithmetic_mean.append(student_arithmetic_mean)

            else:
                situation.append(["Reprovado por Nota"])
                total_arithmetic_mean.append(student_arithmetic_mean)

        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range = "G4", valueInputOption="USER_ENTERED", body={"values": situation}).execute()

        # A list containing the grades for final approval, 0 if the student didn't go to the final exam
        grade_for_final_approval = []

        # If a student goes for the final exam then it's calculated the minimum grade they must have to be approved
        for j in range(len(situation)):
            situation_type = situation[j][0]
            student_arithmetic_mean = total_arithmetic_mean[j]
            gaf = 0

            if situation_type == "Exame Final":
                gaf = 100 - student_arithmetic_mean
                grade_for_final_approval.append([math.ceil(gaf)])
            else:
                grade_for_final_approval.append([0])

        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range = "H4", valueInputOption="USER_ENTERED", body={"values": grade_for_final_approval}).execute()

    except HttpError as err:
        return err
        
if __name__ == "__main__":
    main()