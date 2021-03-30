import numpy as np
import pandas as pd


def calc_ledd(cm, pn, med_date):
    conmed = cm[cm.PATNO == pn]
    # get the active drugs for patient pn
    active = conmed[(conmed.STARTDT < med_date) & ((conmed.STOPDT >= med_date) | (pd.isnull(conmed.STOPDT)))]
    tot_add_meds = 0
    # check if any of the active meds are a function of levodopa dose
    if (active['LEDD'].str.contains('x') == True).any():
        # get rows that are a function of levodopa dose
        x_spec = active.iloc[np.where(active['LEDD'].str.contains('x') == True)]
        # remove rows from active that are a function of dose
        active = active.drop(x_spec.index.values)
        for i in np.arange(len(x_spec)):
            # pull all active levodopa drugs
            add_meds = active[(active.CMTRT.str.contains('SINE')) | #SINEMET
                              (active.CMTRT.str.contains('CARB')) | #CARBIDOPA
                              (active.CMTRT.str.contains('LEVO')) | #LEVODOPA
                              (active.CMTRT.str.contains('RYTA')) | #RYTARY
                              (active.CMTRT.str.contains('STAL')) | #STALEVO
                              (active.CMTRT.str.contains('MADO')) | #MADOPAR
                              (active.CMTRT.str.contains('BENS'))]  #BENSERAZID
            # pull multiplicative factor
            factor = pd.to_numeric(x_spec.iloc[i].LEDD[-4:])
            # calculate LEDD contribution from levodopa function drugs
            tot_add_meds += pd.to_numeric(add_meds.LEDD).sum() * factor

    return pd.to_numeric(active.LEDD).sum() + tot_add_meds