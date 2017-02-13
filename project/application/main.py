import pandas as pd

from project.domain.domain_cleaning import Iris
from project.domain.machine_learning import SepalWidthPredictor

# Define configuration
config_file = "template.ini"


# List analytical steps
training = Iris(config_file).infere_missing_values()
predictor = SepalWidthPredictor().fit(training)
## you may add here additional steps



# Below you will find manual testing of the prediction
test = pd.DataFrame([(1.9, 3.2, 2.3),
                     (0.2, 1.3, 3.2)],
                    columns=SepalWidthPredictor.FEATURES)
prediction = predictor.predict(test)
print(prediction)


