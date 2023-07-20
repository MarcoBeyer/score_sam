import json
from catboost import CatBoostClassifier, Pool
import pandas as pd


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    data = pd.DataFrame.from_dict(event)
    cat_features = ['EmploymentDurationCurrentEmployer', 'Rating', 'CreditScoreEsEquifaxRisk', 'CreditScoreEeMini',
                    'CreditScoreEsMicroL', 'Country', 'CreditScoreFiAsiakasTietoRiskGrade', 'VerificationType',
                    'HomeOwnershipType', 'NewCreditCustomer', 'Education']
    print(data)
    model = CatBoostClassifier()
    model.load_model("score/bondora-model")
    test_data = Pool(data,
                     cat_features=cat_features,
                     )
    predictions = model.predict_proba(test_data)[:, 1]
    return {
        "statusCode": 200,
        "body": json.dumps(predictions.tolist()),
    }
