# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("model")

# Create input/output pydantic models
input_model = create_model("model_input", **{'correctedCoreSpeed-1a': 79.95411682128906, 'amscChBasHealthStatus-1a': 0.0, 'bleedSingleOperation-1a': 0.0, 'bleedPrsovTmCmd-2a': 186.742919921875, 'sfyBasFaultWord1Bit13-2b': 0.0, 'bleedOutTemp-1a': 204.1374969482422, 'bleedOutTemp-1b': 204.2120819091797, 'bleedPrsovOpPosStatus-2a': 1.0, 'bleedPrsovTmCmd-1a': 184.16250610351562, 'bleedOverpressCas-1a': 0.0, 'correctedN1Speed-3a': 93.6253662109375, 'messageInhibitPhases-1': 5.0, 'bleedOutTemp-2b': 204.1145782470703, 'bleedOutTempTarget-1a': 203.875, 'amscChBasHealthStatus-2b': 0.0, 'bleedSwPress-2a': 48.61708450317383, 'bleedAcsBleedConfigStatus-1b': 1.0, 'sfyBasFaultWord1Bit13-1a': 0.0, 'bleedPrsovOpPosStatus-1a': 1.0, 'bleedSwPress-1a': 48.07875061035156, 'bleedSingleOperation-2b': 0.0, 'amscChBasHealthStatus-1b': 0.0, 'correctedCoreSpeed-3a': 79.96749877929688, 'bleedPrsovOpPosStatus-1b': 1.0, 'bleedOutTemp-2a': 204.1145782470703, 'bleedOutTempTarget-2b': 203.875, 'bleedSwPress-2b': 48.61708450317383, 'bleedSwPress-1b': 48.11541748046875, 'bleedPrsovFbk-1b': 0.19458332657814026, 'bleedAcsBleedConfigStatus-2b': 1.0, 'bleedPrsovOpPosStatus-2b': 1.0, 'bleedPrsovFbk-2b': 188.70957946777344, 'bleedPrsovTmCmd-1b': 0.0, 'bleedPrsovTmCmd-2b': 0.0, 'bleedOutTempTarget-1b': 203.875, 'correctedN1Speed-1a': 93.62765502929688, 'amscHprsovDrivF-2b': 0.0, 'amscPrsovDrivF-1a': 0.0, 'amscPrsovDrivF-1b': 0.0, 'bleedFavTmCmd-1a': 99.62291717529297, 'bleedFavTmCmd-1b': 0.0, 'bleedFavTmCmd-2a': 93.53791809082031, 'bleedFavTmCmd-2b': 93.53791809082031, 'bleedFavTmFbk-1a': 103.52208709716797, 'bleedFavTmFbk-1b': 0.4983333349227905, 'bleedFavTmFbk-2b': 96.9054183959961, 'bleedHprsovCmdStatus-1a': 0.0, 'bleedHprsovCmdStatus-1b': 0.0, 'bleedHprsovCmdStatus-2a': 0.0, 'bleedHprsovCmdStatus-2b': 0.0, 'bleedHprsovOpPosStatus-1a': 0.0, 'bleedHprsovOpPosStatus-1b': 0.0, 'bleedHprsovOpPosStatus-2a': 0.0, 'bleedHprsovOpPosStatus-2b': 0.0, 'bleedMonPress-1': 48.00958251953125, 'bleedMonPress-2': 49.0654182434082, 'bleedOnStatus-1a': 1.0, 'bleedOnStatus-1b': 1.0, 'bleedOnStatus-2b': 1.0, 'bleedPrecoolDiffPress-1a': 0.4493750035762787, 'bleedPrecoolDiffPress-1b': 0.46302083134651184, 'bleedPrecoolDiffPress-2': 0.43708333373069763, 'bleedPrsovClPosStatus-1a': 0.0, 'bleedPrsovClPosStatus-2a': 0.0, 'bleedPrsovFbk-1a': 186.49041748046875})
output_model = create_model("model_output", prediction=15)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)