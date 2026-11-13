import os
import pkg_resources
import json
import collections
from hippounit import tests

from TestLoader import ModelLoader
base_directory = 'validation_results/'


config = {
    "target_distances": [
        100,
        200,
        300
    ],
    "tolerance": 50,
    "type": "double exponential synapse",
    "EPSC_amplitude": 0.03, 
    "tau_rise": 0.1,
    "tau_decay": 3.0
}

if __name__ == "__main__":
    
    mods_path = os.path.join(".", "Mods")
    my_model = ModelLoader()

    my_model.v_init = -65
    my_model.celsius = 34
    
    with open('target_features/feat_PSP_attenuation_target_data.json') as f:
        observation = json.load(f, object_pairs_hook=collections.OrderedDict)

   
    test = tests.PSPAttenuationTest(observation=observation,
                                    config=config,
                                    save_all=False,
                                    show_plot=True,
                                    base_directory=base_directory)


    test.npool = 10
    score = test.judge(my_model)
    print(score.summary)
