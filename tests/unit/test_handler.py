import json

import pytest

from score import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "Age": [
            31
        ],
        "AppliedAmount": [
            850
        ],
        "Country": [
            "EE"
        ],
        "DebtToIncome": [
            0
        ],
        "Education": [
            5
        ],
        "EmploymentDurationCurrentEmployer": [
            "UpTo5Years"
        ],
        "FreeCash": [
            1150
        ],
        "HomeOwnershipType": [
            1
        ],
        "IncomeTotal": [
            1300
        ],
        "LiabilitiesTotal": [
            150
        ],
        "LoanDuration": [
            18
        ],
        "MonthlyPayment": [
            63.46
        ],
        "NewCreditCustomer": [
            1
        ],
        "ProbabilityOfDefault": [
            0.242749835456393
        ],
        "Rating": [
            "D"
        ],
        "VerificationType": [
            4
        ],
        "CreditScoreEsMicroL": ["M"],
        "CreditScoreEsEquifaxRisk": ["NaN"],
        "CreditScoreFiAsiakasTietoRiskGrade": ["5"],
        "CreditScoreEeMini": ["NaN"],
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert len(data) == 1
    assert data > [0.8]
    print(data)
