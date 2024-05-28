from __future__ import annotations  # needed for type annotations in > python 3.7
from typing import List, Union
from .producers import triplequantities as triplequantities
from .producers import ml as ml
from .quantities import output as q
from code_generation.friend_trees import FriendTreeConfiguration
from code_generation.modifiers import EraModifier


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
    quantities_map: Union[str, None] = None,
):

    configuration = FriendTreeConfiguration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
        quantities_map,
    )

    # fake factor configurations
    configuration.add_config_parameters(
        ["mmt", "emt", "met", "ett", "mtt"],
        {
            "era_2016preVFP": EraModifier(
                {
                    "2016preVFP": "1",
                    "2016postVFP": "0",
                    "2017": "0",
                    "2018": "0",
                }
            ),
            "era_2016postVFP": EraModifier(
                {
                    "2016preVFP": "0",
                    "2016postVFP": "1",
                    "2017": "0",
                    "2018": "0",
                }
            ),
            "era_2017": EraModifier(
                {
                    "2016preVFP": "0",
                    "2016postVFP": "0",
                    "2017": "1",
                    "2018": "0",
                }
            ),
            "era_2018": EraModifier(
                {
                    "2016preVFP": "0",
                    "2016postVFP": "0",
                    "2017": "0",
                    "2018": "1",
                }
            ),
        },
    )
    configuration.add_config_parameters(
        ["mmt"],
        {
            "model_file": "payloads/ml/wh_tautau/all_eras/mmt_best_net_EVTID.onnx",
            "feature_transformation_file": "payloads/ml/wh_tautau/all_eras/mmt_feature_transformation_EVTID.json",
                })
    configuration.add_config_parameters(
        ["emt"],
        {
            "model_file": "payloads/ml/wh_tautau/all_eras/emt_best_net_EVTID.onnx",
            "feature_transformation_file": "payloads/ml/wh_tautau/all_eras/emt_feature_transformation_EVTID.json",
                })
    configuration.add_config_parameters(
        ["met"],
        {
            "model_file": "payloads/ml/wh_tautau/all_eras/met_best_net_EVTID.onnx",
            "feature_transformation_file": "payloads/ml/wh_tautau/all_eras/met_feature_transformation_EVTID.json",
                })
    configuration.add_config_parameters(
        ["mtt"],
        {
            "model_file": "payloads/ml/wh_tautau/all_eras/mtt_best_net_EVTID.onnx",
            "feature_transformation_file": "payloads/ml/wh_tautau/all_eras/mtt_feature_transformation_EVTID.json",
                })
    configuration.add_config_parameters(
        ["ett"],
        {
            "model_file": "payloads/ml/wh_tautau/all_eras/ett_best_net_EVTID.onnx",
            "feature_transformation_file": "payloads/ml/wh_tautau/all_eras/ett_feature_transformation_EVTID.json",
                })
    configuration.add_producers(
        ["mmt", "emt", "met"],
        [
            ml.eras,
            ml.LLTTransformVars,
            ml.Evaluate_ORT_LLT,
        ],
    )
    configuration.add_producers(
        ["mtt", "ett"],
        [
            ml.eras,
            ml.LTTTransformVars,
            ml.Evaluate_ORT_LTT,
        ],
    )
    configuration.add_outputs(
        ["mmt", "emt", "met", "ett", "mtt"],
        [q.output_vector, q.predicted_class, q.predicted_max_value],
    )

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
