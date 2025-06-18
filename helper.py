import pandas as pd
import numpy as np


def preprocess_data(data):
    """
    Preprocess the input data for the model.
    """
    data = data.copy()

    df = pd.DataFrame()
    df["Marital_status"] = np.asarray(data["Marital_status"]).reshape(-1, 1)[0]
    df["Application_mode"] = np.asarray(data["Application_mode"]).reshape(-1, 1)[0]
    df["Application_order"] = np.asarray(data["Application_order"]).reshape(-1, 1)[0]
    df["Course"] = np.asarray(data["Course"]).reshape(-1, 1)[0]
    df["Daytime_evening_attendance"] = np.asarray(
        data["Daytime_evening_attendance"]
    ).reshape(-1, 1)[0]
    df["Previous_qualification"] = np.asarray(data["Previous_qualification"]).reshape(
        -1, 1
    )[0]
    df["Previous_qualification_grade"] = np.asarray(
        data["Previous_qualification_grade"]
    ).reshape(-1, 1)[0]
    df["Nacionality"] = np.asarray(data["Nacionality"]).reshape(-1, 1)[0]
    df["Mothers_qualification"] = np.asarray(data["Mothers_qualification"]).reshape(
        -1, 1
    )[0]
    df["Fathers_qualification"] = np.asarray(data["Fathers_qualification"]).reshape(
        -1, 1
    )[0]
    df["Mothers_occupation"] = np.asarray(data["Mothers_occupation"]).reshape(-1, 1)[0]
    df["Fathers_occupation"] = np.asarray(data["Fathers_occupation"]).reshape(-1, 1)[0]
    df["Admission_grade"] = np.asarray(data["Admission_grade"]).reshape(-1, 1)[0]
    df["Displaced"] = np.asarray(data["Displaced"]).reshape(-1, 1)[0]
    df["Educational_special_needs"] = np.asarray(
        data["Educational_special_needs"]
    ).reshape(-1, 1)[0]
    df["Debtor"] = np.asarray(data["Debtor"]).reshape(-1, 1)[0]
    df["Tuition_fees_up_to_date"] = np.asarray(data["Tuition_fees_up_to_date"]).reshape(
        -1, 1
    )[0]
    df["Gender"] = np.asarray(data["Gender"]).reshape(-1, 1)[0]
    df["Scholarship_holder"] = np.asarray(data["Scholarship_holder"]).reshape(-1, 1)[0]
    df["Age_at_enrollment"] = np.asarray(data["Age_at_enrollment"]).reshape(-1, 1)[0]
    df["International"] = np.asarray(data["International"]).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_credited"] = np.asarray(
        data["Curricular_units_1st_sem_credited"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_enrolled"] = np.asarray(
        data["Curricular_units_1st_sem_enrolled"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_evaluations"] = np.asarray(
        data["Curricular_units_1st_sem_evaluations"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_approved"] = np.asarray(
        data["Curricular_units_1st_sem_approved"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_grade"] = np.asarray(
        data["Curricular_units_1st_sem_grade"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_1st_sem_without_evaluations"] = np.asarray(
        data["Curricular_units_1st_sem_without_evaluations"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_credited"] = np.asarray(
        data["Curricular_units_2nd_sem_credited"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_enrolled"] = np.asarray(
        data["Curricular_units_2nd_sem_enrolled"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_evaluations"] = np.asarray(
        data["Curricular_units_2nd_sem_evaluations"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_approved"] = np.asarray(
        data["Curricular_units_2nd_sem_approved"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_grade"] = np.asarray(
        data["Curricular_units_2nd_sem_grade"]
    ).reshape(-1, 1)[0]
    df["Curricular_units_2nd_sem_without_evaluations"] = np.asarray(
        data["Curricular_units_2nd_sem_without_evaluations"]
    ).reshape(-1, 1)[0]
    df["Unemployment_rate"] = np.asarray(data["Unemployment_rate"]).reshape(-1, 1)[0]
    df["Inflation_rate"] = np.asarray(data["Inflation_rate"]).reshape(-1, 1)[0]
    df["GDP"] = np.asarray(data["GDP"]).reshape(-1, 1)[0]

    return df
