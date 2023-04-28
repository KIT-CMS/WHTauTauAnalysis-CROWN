from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
from .producers import jets as jets
from .producers import met as met
from .producers import muons as muons
from .producers import triplequantities as triplequantities
from .producers import tripleselection as tripleselection
from .producers import scalefactors as scalefactors
from .producers import taus as taus
from .producers import triggers as triggers
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from .tau_triggersetup import add_diTauTriggerSetup
from .tau_variations import add_tauVariations
from .jet_variations import add_jetVariations

# from .tau_embedding_settings import setup_embedding
from .btag_variations import add_btagVariations
from .jec_data import add_jetCorrectionData
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):

    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )
    # first add default parameters necessary for all scopes
    configuration.add_config_parameters(
        "global",
        {
            "PU_reweighting_file": EraModifier(
                {
                    "2016": "",
                    "2017": "data/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz",
                    "2018": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz",
                }
            ),
            "PU_reweighting_era": EraModifier(
                {
                    "2016": "",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                }
            ),
            "PU_reweighting_variation": "nominal",
            "golden_json_file": EraModifier(
                {
                    "2016": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                }
            ),
            "met_filters": EraModifier(
                {
                    "2016": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                }
            ),
        },
    )
    # Tau base selection:
    # configuration.add_config_parameters(
    #     "global",
    #     {
    #         "min_tau_pt": 30.0,
    #         "max_tau_eta": 2.3,
    #         "max_tau_dz": 0.2,
    #     },
    # )
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "ett", "mtt"],
        {
            "tau_dms": "0,1,10,11",
            "tau_sf_file": EraModifier(
                {
                    "2016": "data/jsonpog-integration/POG/TAU/2016postVFP_UL/tau.json.gz",
                    "2017": "data/jsonpog-integration/POG/TAU/2017_UL/tau.json.gz",
                    "2018": "data/jsonpog-integration/POG/TAU/2018_UL/tau.json.gz",
                }
            ),
            "tau_ES_json_name": "tau_energy_scale",
            "tau_id_algorithm": "DeepTau2017v2p1",
            "tau_ES_shift_DM0": "nom",
            "tau_ES_shift_DM1": "nom",
            "tau_ES_shift_DM10": "nom",
            "tau_ES_shift_DM11": "nom",
            "tau_elefake_es_DM0_barrel": "nom",
            "tau_elefake_es_DM0_endcap": "nom",
            "tau_elefake_es_DM1_barrel": "nom",
            "tau_elefake_es_DM1_endcap": "nom",
            "tau_mufake_es": "nom",
        },
    )
    # jet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_jet_pt": 30,
            "max_jet_eta": 4.7,
            "jet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "jet_puid": EraModifier(
                {
                    "2016preVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2016postVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2017": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2018": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                }
            ),
            "jet_puid_max_pt": 50,  # recommended to apply puID only for jets below 50 GeV
            "jet_reapplyJES": False,
            "jet_jes_sources": '{""}',
            "jet_jes_shift": 0,
            "jet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "jet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/jet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/jet_jerc.json.gz"',
                }
            ),
            "jet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"',
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                }
            ),
            "jet_jes_tag_data": '""',
            "jet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"',
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                }
            ),
            "jet_jec_algo": '"AK4PFchs"',
        },
    )
    # bjet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_bjet_pt": 20,
            "max_bjet_eta": EraModifier(
                {
                    "2016": 2.4,
                    "2017": 2.5,
                    "2018": 2.5,
                }
            ),
            "btag_cut": EraModifier(  # medium
                {
                    "2016": 0.3093,
                    "2017": 0.3040,
                    "2018": 0.2783,
                }
            ),
        },
    )
    # bjet scale factors
    configuration.add_config_parameters(
        scopes,
        {
            "btag_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
                    "2017": "data/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
                    "2018": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
                }
            ),
            "btag_sf_variation": "central",
            "btag_corr_algo": "deepJet_shape",
        },
    )
    # leptonveto base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_dielectronveto_pt": 15.0,
            "dielectronveto_id": "Electron_cutBased",
            "dielectronveto_id_wp": 1,
            "min_dimuonveto_pt": 15.0,
            "dimuonveto_id": "Muon_looseId",
            "dileptonveto_dR": 0.15,
        },
    )

    # di tau id weights
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "ett", "mtt"],
        {
            "vsjet_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSjet",
                    "tau_3_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_3".format(
                        wp=wp
                    ),
                    "tau_2_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_2".format(
                        wp=wp
                    ),
                    "vsjet_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_3_vsjet_id_outputname": "id_tau_vsJet_{wp}_3".format(wp=wp),
                    "tau_2_vsjet_id_outputname": "id_tau_vsJet_{wp}_2".format(wp=wp),
                    "vsjet_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    "VVVLoose": 1,
                    "VVLoose": 2,
                    "VLoose": 3,
                    "Loose": 4,
                    "Medium": 5,
                    "Tight": 6,
                    "VTight": 7,
                    "VVTight": 8,
                }.items()
            ],
            "vsele_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSe",
                    "tau_3_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_3".format(
                        wp=wp
                    ),
                    "tau_2_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_2".format(
                        wp=wp
                    ),
                    "vsele_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_3_vsele_id_outputname": "id_tau_vsEle_{wp}_3".format(wp=wp),
                    "tau_2_vsele_id_outputname": "id_tau_vsEle_{wp}_2".format(wp=wp),
                    "vsele_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    "VVLoose": 2,
                    "VLoose": 3,
                    "Loose": 4,
                    "Medium": 5,
                    "Tight": 6,
                    "VTight": 7,
                    "VVTight": 8,
                }.items()
            ],
            "vsmu_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSmu",
                    "tau_3_vsmu_sf_outputname": "id_wgt_tau_vsMu_{wp}_3".format(wp=wp),
                    "tau_2_vsmu_sf_outputname": "id_wgt_tau_vsMu_{wp}_2".format(wp=wp),
                    "vsmu_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_3_vsmu_id_outputname": "id_tau_vsMu_{wp}_3".format(wp=wp),
                    "tau_2_vsmu_id_outputname": "id_tau_vsMu_{wp}_2".format(wp=wp),
                    "vsmu_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    "VLoose": 1,
                    "Loose": 2,
                    "Medium": 3,
                    "Tight": 4,
                }.items()
            ],
            "tau_sf_vsele_barrel": "nom",  # or "up"/"down" for up/down variation
            "tau_sf_vsele_endcap": "nom",  # or "up"/"down" for up/down variation
            "tau_sf_vsmu_wheel1": "nom",
            "tau_sf_vsmu_wheel2": "nom",
            "tau_sf_vsmu_wheel3": "nom",
            "tau_sf_vsmu_wheel4": "nom",
            "tau_sf_vsmu_wheel5": "nom",
        },
    )
    # ETT/MTT tau id sf variations
    configuration.add_config_parameters(
        ["ett", "mtt"],
        {
            "tau_sf_vsjet_tauDM0": "nom",
            "tau_sf_vsjet_tauDM1": "nom",
            "tau_sf_vsjet_tauDM10": "nom",
            "tau_sf_vsjet_tauDM11": "nom",
            "tau_vsjet_sf_dependence": "dm",  # or "dm", "eta"
        },
    )
    configuration.add_config_parameters(
        scopes,
        {
            "ggHNNLOweightsRootfile": "data/htxs/NNLOPS_reweight.root",
            "ggH_generator": "powheg",
            "zptmass_file": EraModifier(
                {
                    "2016": "data/zpt/htt_scalefactors_legacy_2016.root",
                    "2017": "data/zpt/htt_scalefactors_legacy_2017.root",
                    "2018": "data/zpt/htt_scalefactors_legacy_2018.root",
                }
            ),
            "zptmass_functor": "zptmass_weight_nom",
            "zptmass_arguments": "z_gen_mass,z_gen_pt",
        },
    )

    # add muon scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "mtt", "mme", "eem"],
        {
            "mc_muon_sf_file": "data/embedding/muon_2018UL.json.gz",
            "mc_muon_id_sf": "ID_pt_eta_bins",
            "mc_muon_iso_sf": "Iso_pt_eta_bins",
            "mc_muon_id_extrapolation": 1.0,  # for nominal case
            "mc_muon_iso_extrapolation": 1.0,  # for nominal case
        },
    )
    # add electron scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["emt", "met", "ett", "mme", "eem"],
        {
            "mc_electron_sf_file": "data/embedding/electron_2018UL.json.gz",
            "mc_electron_id_sf": "ID90_pt_eta_bins",
            "mc_electron_iso_sf": "Iso_pt_eta_bins",
            "mc_electron_id_extrapolation": 1.0,  # for nominal case
            "mc_electron_iso_extrapolation": 1.0,  # for nominal case
        },
    )
    # muon trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "mtt", "mme", "eem"],
        {
            "singlemuon_trigger_sf_mc": [
                {
                    "flagname": "trg_wgt_single_mu24",
                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                },
                {
                    "flagname": "trg_wgt_single_mu27",
                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                },
                {
                    "flagname": "trg_wgt_single_mu24ormu27",
                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                },
            ]
        },
    )
    # electron trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["emt", "met", "ett", "mme", "eem"],
        {
            "singlelectron_trigger_sf_mc": [
                {
                    "flagname": "trg_wgt_single_ele32",
                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                    "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                },
                {
                    "flagname": "trg_wgt_single_ele35",
                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                    "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                },
                {
                    "flagname": "trg_wgt_single_ele32orele35",
                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                    "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                },
            ]
        },
    )
    # MT / ET tau id sf variations
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "ett", "mtt"],
        {
            "tau_sf_vsjet_tau30to35": "nom",
            "tau_sf_vsjet_tau35to40": "nom",
            "tau_sf_vsjet_tau40to500": "nom",
            "tau_sf_vsjet_tau500to1000": "nom",
            "tau_sf_vsjet_tau1000toinf": "nom",
            "tau_vsjet_sf_dependence": "pt",  # or "dm", "eta"
        },
    )
    # Muon scale factors configuration / right now we use this scale factors (official)
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "mtt", "mme", "eem"],
        {
            "muon_sf_file": EraModifier(
                {
                    "2016": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                }
            ),
            "muon_id_sf_name": "NUM_MediumID_DEN_TrackerMuons",
            "muon_iso_sf_name": "NUM_TightRelIso_DEN_MediumID",
            "muon_sf_year_id": EraModifier(
                {
                    "2016": "2016postVFP_UL",
                    "2017": "2017_UL",
                    "2018": "2018_UL",
                }
            ),
            "muon_sf_varation": "sf",  # "sf" is nominal, "systup"/"systdown" are up/down variations
        },
    )
    # electron scale factors configuration
    configuration.add_config_parameters(
        ["emt", "met", "ett", "mme", "eem"],
        {
            "ele_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz",
                    "2017": "data/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz",
                    "2018": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz",
                }
            ),
            "ele_id_sf_name": "UL-Electron-ID-SF",
            "ele_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                }
            ),
            "ele_sf_varation": "sf",  # "sf" is nominal, "sfup"/"sfdown" are up/down variations
        },
    )
    # muon base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_muon_pt": 15.0,
            "max_muon_eta": 2.4,
            "max_muon_dxy": 0.045,
            "max_muon_dz": 0.2,
            # "muon_id": "Muon_mediumId",
        },
    )
    # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_ele_pt": 10.0,
            "max_ele_eta": 2.5,
            "max_ele_dxy": 0.045,
            "max_ele_dz": 0.2,
            # "ele_id": "Electron_mvaFall17V2noIso_WP90",
        },
    )
    # in the channels for the signal extraction, the base selection is also taken into account for the base masks to estimate the jet to lepton fake contribution. so execpt of the tau id working point, one can choose the good particles properties here
    # EMT scope electron and selection
    configuration.add_config_parameters(
        ["emt"],
        {
            "min_tau_pt": 20.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,  # vloose, 7 (vtight in paper)
            "vsele_tau_id_bit": 1,  # vloose, 6 (tight) in paper
            "vsmu_tau_id_bit": 1,  # vloose, 4 (tight) in paper
            "electron_index_in_triple": 0,
            "min_electron_pt": 15.0,  # 15 in paper
            "max_electron_eta": 2.5,  # in paper 2.1
            "electron_iso_cut": 0.15,  # 0.15 in paper
            "max_ele_iso": 0.15,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "muon_index_in_triple": 1,
            "muon_id": "Muon_mediumId",
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.15,
            "deltaR_jet_veto": 0.15,
            "tripleselection_min_dR_leptau": 0.5,
            "tripleselection_min_dR_leplep": 0.3,
            "p4_miss_sf": 0.69,
        },
    )
    # MET scope electron and selection
    configuration.add_config_parameters(
        ["met"],
        {
            "min_tau_pt": 20.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,  # vloose, 7 (vtight in paper)
            "vsele_tau_id_bit": 1,  # vloose, 6 (tight) in paper
            "vsmu_tau_id_bit": 1,  # vloose, 4 (tight) in paper
            "electron_index_in_triple": 1,
            "min_electron_pt": 15.0,  # 15 in paper
            "max_electron_eta": 2.5,  # in paper 2.1
            "electron_iso_cut": 0.5,  # 0.15 in paper
            "max_ele_iso": 0.15,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "muon_index_in_triple": 0,
            "muon_id": "Muon_mediumId",
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.15,
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_leptau": 0.5,
            "tripleselection_min_dR_leplep": 0.3,
            "p4_miss_sf": 0.69,
        },
    )
    # MMT scope electron and selection, also for fake rate measurements
    configuration.add_config_parameters(
        ["mmt"],
        {
            "min_tau_pt": 20.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,  # vvvloose, 7 (vtight in paper)
            "vsele_tau_id_bit": 1,  # vvloose, 6 (tight) in paper
            "vsmu_tau_id_bit": 1,  # vloose, 4 (tight) in paper
            "muon_id": "Muon_mediumId",
            "muon_index_in_triple": 0,
            "second_muon_index_in_triple": 1,
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.15,
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_leptau": 0.0,
            "tripleselection_min_dR_leplep": 0.3,
            "min_electron_pt": 15.0,  # 15 in paper
            "max_electron_eta": 2.5,  # in paper 2.1
            "electron_iso_cut": 0.15,  # 0.15 in paper
            "max_ele_iso": 0.15,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "p4_miss_sf": 0.69,
        },
    )
    # ETT scope electron and selection, also for fake rate measurements
    configuration.add_config_parameters(
        ["ett"],
        {
            "min_tau_pt": 20.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,  # vloose, 7 (vtight in paper)
            "vsele_tau_id_bit": 1,  # vloose, 6 (tight) in paper
            "vsmu_tau_id_bit": 1,  # vloose, 4 (tight) in paper
            "electron_index_in_triple": 0,
            "min_electron_pt": 28.0,
            "max_electron_eta": 2.1,
            "electron_iso_cut": 0.15,  # 0.15 in paper
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_leptau": 0.5,
            "tripleselection_min_dR_tautau": 0.5,
            "muon_id": "Muon_mediumId",
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.15,
            "p4_miss_sf": 0.47,
        },
    )
    # MTT scope electron and selection, also for fake rate measurements
    configuration.add_config_parameters(
        ["mtt"],
        {
            "min_tau_pt": 20.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,  # vloose, 7 (vtight in paper)
            "vsele_tau_id_bit": 1,  # vloose, 6 (tight) in paper
            "vsmu_tau_id_bit": 1,  # vloose, 4 (tight) in paper
            "muon_index_in_triple": 0,
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.5,
            "muon_id": "Muon_mediumId",
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_leptau": 0.5,
            "tripleselection_min_dR_tautau": 0.5,
            "min_electron_pt": 15.0,
            "max_electron_eta": 2.5,
            "electron_iso_cut": 0.15,  # 0.15 in paper
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "p4_miss_sf": 0.47,
        },
    )
    # MME scope electron and selection, also for fake rate measurements
    configuration.add_config_parameters(
        ["mme"],
        {
            "muon_index_in_triple": 0,
            "second_muon_index_in_triple": 1,
            "electron_index_in_triple": 2,
            "min_muon_pt": 15.0,
            "max_muon_eta": 2.4,
            "muon_iso_cut": 0.15,
            "muon_id": "Muon_mediumId",
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_lep1lep1": 0.3,
            "tripleselection_min_dR_lep1lep2": 0.3,
            "min_electron_pt": 10.0,
            "max_electron_eta": 2.5,
            "electron_iso_cut": 0.15,  # 0.15 in paper
            "p4_miss_sf": 0.69,
        },
    )
    # EEM scope electron and selection, also for fake rate measurements
    configuration.add_config_parameters(
        ["eem"],
        {
            "electron_index_in_triple": 0,
            "second_electron_index_in_triple": 1,
            "muon_index_in_triple": 2,
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "min_electron_pt": 10.0,
            "max_electron_eta": 2.5,
            "electron_iso_cut": 0.15,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR_lep1lep1": 0.3,
            "tripleselection_min_dR_lep1lep2": 0.3,
            "muon_iso_cut": 0.15,
            "muon_id": "Muon_mediumId",
            "p4_miss_sf": 0.69,
        },
    )
    # # EMT TrueGenTriple
    # configuration.add_config_parameters(
    #     ["emt"],
    #     {
    #         "truegen_mother_pdgid_23": SampleModifier(
    #             {"rem_htautau": 25, "tt": 6, "vv": 24}, default=None
    #         ),
    #         "truegen_mother_pdgid_1": SampleModifier(
    #             {"rem_htautau": 24, "tt": 6, "vv": 24}, default=None
    #         ),
    #         "truegen_daughter_1_pdgid": 11,
    #         "truegen_daugher_2_pdgid": 15,
    #         "truegen_daugher_3_pdgid": 15,
    #     },
    # )
    ## all scopes misc settings
    configuration.add_config_parameters(
        scopes,
        {
            "deltaR_jet_veto": 0.5,
            "tripleselection_min_dR": 0.5,
        },
    )
    ## all scopes MET selection
    configuration.add_config_parameters(
        scopes,
        {
            "propagateLeptons": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "propagateJets": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "recoil_corrections_file": EraModifier(
                {
                    "2016": "data/recoil_corrections/Type1_PuppiMET_2016.root",
                    "2017": "data/recoil_corrections/Type1_PuppiMET_2017.root",
                    "2018": "data/recoil_corrections/Type1_PuppiMET_2018.root",
                }
            ),
            "recoil_systematics_file": EraModifier(
                {
                    "2016": "data/recoil_corrections/PuppiMETSys_2016.root",
                    "2017": "data/recoil_corrections/PuppiMETSys_2017.root",
                    "2018": "data/recoil_corrections/PuppiMETSys_2018.root",
                }
            ),
            "applyRecoilCorrections": SampleModifier({"wj": True}, default=False),
            "apply_recoil_resolution_systematic": False,
            "apply_recoil_response_systematic": False,
            "recoil_systematic_shift_up": False,
            "recoil_systematic_shift_down": False,
            "min_jetpt_met_propagation": 15,
        },
    )

    configuration.add_config_parameters(
        scopes,
        {
            "ggHNNLOweightsRootfile": "data/htxs/NNLOPS_reweight.root",
            "ggH_generator": "powheg",
            "zptmass_file": EraModifier(
                {
                    "2016": "data/zpt/htt_scalefactors_legacy_2016.root",
                    "2017": "data/zpt/htt_scalefactors_legacy_2017.root",
                    "2018": "data/zpt/htt_scalefactors_legacy_2018.root",
                }
            ),
            "zptmass_functor": "zptmass_weight_nom",
            "zptmass_arguments": "z_gen_mass,z_gen_pt",
        },
    )

    configuration.add_producers(
        "global",
        [
            # event.RunLumiEventFilter,
            event.SampleFlags,
            event.Lumi,
            event.npartons,
            event.MetFilter,
            event.PUweights,
            muons.BaseMuons,
            electrons.BaseElectrons,
            jets.JetEnergyCorrection,
            jets.GoodJets,
            jets.GoodBJets,
            event.DiLeptonVeto,
            met.MetBasics,
        ],
    )
    ## add prefiring
    if era != "2018":
        configuration.add_producers(
            "global",
            [
                event.PrefireWeight,
            ],
        )
    # common
    configuration.add_producers(
        ["emt", "met"],
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.ExtraMuonsVeto,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            tripleselection.LVTau3Uncorrected,
            tripleselection.LVTau3,
            #  scalefactors
            scalefactors.Tau_3_VsJetTauID_lt_SF,
            scalefactors.Tau_3_VsEleTauID_SF,
            scalefactors.Tau_3_VsMuTauID_SF,
            # electrons
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
        ],
    )
    configuration.add_producers(
        "emt",
        [
            tripleselection.EMTTripleSelection,
            # tripleselection.EMTTripleSelectionWOEle,
            tripleselection.LVEl1,
            tripleselection.LVMu2,
            tripleselection.LVEl1Uncorrected,
            tripleselection.LVMu2Uncorrected,
            triplequantities.EMTTripleQuantities,
            genparticles.EMTGenTripleQuantities,
            scalefactors.Muon_2_ID_SF,
            scalefactors.EleID_SF,
            scalefactors.Muon_2_Iso_SF,
            scalefactors.EMTGenerateSingleMuonTriggerSF_MC,
            scalefactors.EMTGenerateSingleElectronTriggerSF_MC,
            triggers.EMTGenerateSingleElectronTriggerFlags,
            triggers.EMTGenerateSingleMuonTriggerFlags,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        "met",
        [
            tripleselection.METTripleSelection,
            tripleselection.LVEl2,
            tripleselection.LVMu1,
            tripleselection.LVEl2Uncorrected,
            tripleselection.LVMu1Uncorrected,
            triplequantities.METTripleQuantities,
            genparticles.METGenTripleQuantities,
            #  scalefactors
            scalefactors.Muon_1_ID_SF,
            scalefactors.EleID_SF,
            scalefactors.Muon_1_Iso_SF,
            triggers.METGenerateSingleElectronTriggerFlags,
            triggers.METGenerateSingleMuonTriggerFlags,
            scalefactors.METGenerateSingleMuonTriggerSF_MC,
            scalefactors.METGenerateSingleElectronTriggerSF_MC,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        "mmt",
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.VetoSecondMuon,
            muons.ExtraMuonsVeto,
            electrons.GoodElectrons,
            electrons.ExtraElectronsVeto,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            tripleselection.LVTau3Uncorrected,
            tripleselection.LVTau3,
            #  scalefactors
            scalefactors.Tau_3_VsJetTauID_lt_SF,
            scalefactors.Tau_3_VsEleTauID_SF,
            scalefactors.Tau_3_VsMuTauID_SF,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.MMTTripleSelection,
            # tripleselection.EMTTripleSelectionWOEle,
            tripleselection.LVMu2,
            tripleselection.LVMu1,
            tripleselection.LVMu2Uncorrected,
            tripleselection.LVMu1Uncorrected,
            triplequantities.MMTTripleQuantities,
            genparticles.MMTGenTripleQuantities,
            #  scalefactors
            scalefactors.Muon_1_ID_SF,
            scalefactors.Muon_1_Iso_SF,
            scalefactors.Muon_2_ID_SF,
            scalefactors.Muon_2_Iso_SF,
            triggers.MMTGenerateSingleMuonTriggerFlags,
            scalefactors.MMTGenerateSingleMuonTriggerSF_MC,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        ["ett"],
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            muons.GoodMuons,
            muons.ExtraMuonsVeto,
            taus.TauEnergyCorrection,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            tripleselection.LVTau2Uncorrected,
            tripleselection.LVTau2,
            tripleselection.LVTau3Uncorrected,
            tripleselection.LVTau3,
            #  scalefactors
            scalefactors.Tau_2_VsJetTauID_tt_SF,
            scalefactors.Tau_2_VsEleTauID_SF,
            scalefactors.Tau_2_VsMuTauID_SF,
            scalefactors.Tau_3_VsJetTauID_tt_SF,
            scalefactors.Tau_3_VsEleTauID_SF,
            scalefactors.Tau_3_VsMuTauID_SF,
            # electrons
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.ETTTripleSelection,
            tripleselection.LVEl1,
            tripleselection.LVEl1Uncorrected,
            triplequantities.ETTTripleQuantities,
            genparticles.ETTGenTripleQuantities,
            scalefactors.EleID_SF,
            scalefactors.ETTGenerateSingleElectronTriggerSF_MC,
            triggers.ETTGenerateSingleElectronTriggerFlags,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        ["mtt"],
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            electrons.GoodElectrons,
            electrons.ExtraElectronsVeto,
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.ExtraMuonsVeto,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            tripleselection.LVTau2Uncorrected,
            tripleselection.LVTau2,
            tripleselection.LVTau3Uncorrected,
            tripleselection.LVTau3,
            #  scalefactors
            scalefactors.Tau_2_VsJetTauID_tt_SF,
            scalefactors.Tau_2_VsEleTauID_SF,
            scalefactors.Tau_2_VsMuTauID_SF,
            scalefactors.Tau_3_VsJetTauID_tt_SF,
            scalefactors.Tau_3_VsEleTauID_SF,
            scalefactors.Tau_3_VsMuTauID_SF,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.MTTTripleSelection,
            tripleselection.LVMu1,
            tripleselection.LVMu1Uncorrected,
            triplequantities.MTTTripleQuantities,
            genparticles.MTTGenTripleQuantities,
            scalefactors.Muon_1_ID_SF,
            scalefactors.Muon_1_Iso_SF,
            scalefactors.MTTGenerateSingleMuonTriggerSF_MC,
            triggers.MTTGenerateSingleMuonTriggerFlags,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        "mme",
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.VetoSecondMuon,
            muons.ExtraMuonsVeto,
            electrons.GoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            # electrons.BaseElectrons_fake,
            # electrons.GoodElectrons,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.MMETripleSelection,
            tripleselection.LVMu2,
            tripleselection.LVMu1,
            tripleselection.LVEl3,
            tripleselection.LVEl3Uncorrected,
            tripleselection.LVMu2Uncorrected,
            tripleselection.LVMu1Uncorrected,
            triplequantities.MMETripleQuantities,
            genparticles.MMEGenTripleQuantities,
            #  scalefactors
            scalefactors.Muon_1_ID_SF,
            scalefactors.Muon_1_Iso_SF,
            scalefactors.Muon_2_ID_SF,
            scalefactors.Muon_2_Iso_SF,
            scalefactors.EleID_SF,
            triggers.MMEGenerateSingleMuonTriggerFlags,
            scalefactors.MMEGenerateSingleMuonTriggerSF_MC,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_producers(
        ["eem"],
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            genparticles.GenMatching,
            # muons taus
            # muons.BaseMuons_fake,
            muons.VetoMuons,
            muons.ExtraMuonsVeto,
            muons.GoodMuons,
            scalefactors.MuonIDIso_SF,
            # electrons
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.EEMTripleSelection,
            tripleselection.LVEl1,
            tripleselection.LVEl1Uncorrected,
            tripleselection.LVEl2,
            tripleselection.LVEl2Uncorrected,
            tripleselection.LVMu3,
            tripleselection.LVMu3Uncorrected,
            triplequantities.EEMTripleQuantities,
            genparticles.EEMGenTripleQuantities,
            scalefactors.EleID_SF,
            scalefactors.EEMGenerateSingleElectronTriggerSF_MC,
            triggers.EEMGenerateSingleElectronTriggerFlags,
            # genparticles.EMTTrueGenTriple,
        ],
    )
    configuration.add_modification_rule(
        "emt",
        RemoveProducer(
            producers=[
                scalefactors.Tau_3_VsMuTauID_SF,
                scalefactors.Tau_3_VsJetTauID_lt_SF,
                scalefactors.Tau_3_VsEleTauID_SF,
                genparticles.EMTGenTripleQuantities,
                triplequantities.tau_gen_match_3,
                scalefactors.EMTGenerateSingleMuonTriggerSF_MC,
                scalefactors.EMTGenerateSingleElectronTriggerSF_MC,
                #          genparticles.EMTTrueGenTriple,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "met",
        RemoveProducer(
            producers=[
                scalefactors.Tau_3_VsMuTauID_SF,
                scalefactors.Tau_3_VsJetTauID_lt_SF,
                scalefactors.Tau_3_VsEleTauID_SF,
                genparticles.METGenTripleQuantities,
                triplequantities.tau_gen_match_3,
                scalefactors.METGenerateSingleMuonTriggerSF_MC,
                scalefactors.METGenerateSingleElectronTriggerSF_MC,
                #          genparticles.EMTTrueGenTriple,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "mmt",
        RemoveProducer(
            producers=[
                scalefactors.Tau_3_VsMuTauID_SF,
                scalefactors.Tau_3_VsJetTauID_lt_SF,
                scalefactors.Tau_3_VsEleTauID_SF,
                genparticles.MMTGenTripleQuantities,
                triplequantities.tau_gen_match_3,
                scalefactors.MMTGenerateSingleMuonTriggerSF_MC,
                #          genparticles.EMTTrueGenTriple,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "ett",
        RemoveProducer(
            producers=[
                scalefactors.Tau_2_VsMuTauID_SF,
                scalefactors.Tau_2_VsJetTauID_tt_SF,
                scalefactors.Tau_2_VsEleTauID_SF,
                scalefactors.Tau_3_VsMuTauID_SF,
                scalefactors.Tau_3_VsJetTauID_tt_SF,
                scalefactors.Tau_3_VsEleTauID_SF,
                genparticles.ETTGenTripleQuantities,
                triplequantities.tau_gen_match_3,
                triplequantities.tau_gen_match_2,
                scalefactors.ETTGenerateSingleElectronTriggerSF_MC,
                #          genparticles.EMTTrueGenTriple,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "mtt",
        RemoveProducer(
            producers=[
                scalefactors.Tau_2_VsMuTauID_SF,
                scalefactors.Tau_2_VsJetTauID_tt_SF,
                scalefactors.Tau_2_VsEleTauID_SF,
                scalefactors.Tau_3_VsMuTauID_SF,
                scalefactors.Tau_3_VsJetTauID_tt_SF,
                scalefactors.Tau_3_VsEleTauID_SF,
                genparticles.MTTGenTripleQuantities,
                triplequantities.tau_gen_match_3,
                triplequantities.tau_gen_match_2,
                scalefactors.MTTGenerateSingleMuonTriggerSF_MC,
                #          genparticles.EMTTrueGenTriple,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "mme",
        RemoveProducer(
            producers=[
                genparticles.MMEGenTripleQuantities,
                scalefactors.MMEGenerateSingleMuonTriggerSF_MC,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "eem",
        RemoveProducer(
            producers=[
                genparticles.EEMGenTripleQuantities,
                scalefactors.EEMGenerateSingleElectronTriggerSF_MC,
            ],
            samples="data",
        ),
    )
    # configuration.add_modification_rule(
    #     "eem",
    #     ReplaceProducer(
    #         producers=[muons.BaseMuons, muons.BaseMuons_fake],
    #         samples=[sample for sample in available_sample_types],
    #     ),
    # )
    configuration.add_modification_rule(
        ["emt", "met", "mmt", "ett", "mtt", "mme", "eem"],
        RemoveProducer(
            producers=[
                scalefactors.btagging_SF,
            ],
            samples=["data", "embedding", "embedding_mc"],
        ),
    )
    configuration.add_modification_rule(
        ["emt", "met", "mmt", "ett", "mtt"],
        ReplaceProducer(
            producers=[taus.TauEnergyCorrection, taus.TauEnergyCorrection_data],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "global",
        ReplaceProducer(
            producers=[jets.JetEnergyCorrection, jets.JetEnergyCorrection_data],
            samples="data",
        ),
    )

    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[event.npartons],
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["dyjets", "wjets", "electroweak_boson"]
            ],
        ),
    )
    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[event.PUweights],
            samples=["data", "embedding", "embedding_mc"],
        ),
    )

    configuration.add_modification_rule(
        scopes,
        RemoveProducer(
            producers=[
                genparticles.GenMatching,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=[event.GGH_NNLO_Reweighting, event.GGH_WG1_Uncertainties],
            samples="ggh_htautau",
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(producers=event.QQH_WG1_Uncertainties, samples="vbf_htautau"),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=event.TopPtReweighting, samples=["ttbar", "rem_ttbar"]
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(producers=event.ZPtMassReweighting, samples="dyjets"),
    )
    # changes needed for data
    # global scope
    configuration.add_modification_rule(
        "global",
        AppendProducer(
            producers=jets.RenameJetsData, samples=["embedding", "embedding_mc"]
        ),
    )
    configuration.add_modification_rule(
        "global",
        AppendProducer(producers=event.JSONFilter, samples=["data", "embedding"]),
    )

    configuration.add_outputs(
        scopes,
        [
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_ggh_htautau,
            q.is_vbf_htautau,
            q.is_diboson,
            q.is_whtautau,
            q.is_rem_ttbar,
            q.is_triboson,
            q.is_rem_VH,
            q.is_ggZZ,
            nanoAOD.run,
            q.lumi,
            q.npartons,
            nanoAOD.event,
            q.puweight,
            q.pt_1,
            q.pt_2,
            q.pt_3,
            q.eta_1,
            q.eta_2,
            q.eta_3,
            q.phi_1,
            q.phi_2,
            q.phi_3,
            q.njets,
            q.jpt_1,
            q.jpt_2,
            q.jeta_1,
            q.jeta_2,
            q.jphi_1,
            q.jphi_2,
            q.jtag_value_1,
            q.jtag_value_2,
            q.mjj,
            q.m_vis,
            q.deltaR_12,
            q.deltaR_13,
            q.deltaR_23,
            q.deltaPhi_12,
            q.deltaPhi_13,
            q.deltaPhi_WH,
            q.eta_vis,
            q.phi_vis,
            q.scalarPtSum,
            q.pt_vis,
            q.nbtag,
            q.bpt_1,
            q.bpt_2,
            q.beta_1,
            q.beta_2,
            q.bphi_1,
            q.bphi_2,
            q.btag_value_1,
            q.btag_value_2,
            q.btag_weight,
            q.mass_1,
            q.mass_2,
            q.mass_3,
            q.dxy_1,
            q.dxy_2,
            q.dz_1,
            q.dz_2,
            q.dz_3,
            q.q_1,
            q.q_2,
            q.q_3,
            q.iso_1,
            q.iso_2,
            q.iso_3,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_pt_3,
            q.gen_eta_3,
            q.gen_phi_3,
            q.gen_mass_3,
            q.gen_pdgid_3,
            q.gen_m_vis,
            # q.truegentriple,
            q.met,
            q.metphi,
            q.pfmet,
            q.pfmetphi,
            q.met_uncorrected,
            q.metphi_uncorrected,
            q.pfmet_uncorrected,
            q.pfmetphi_uncorrected,
            q.metSumEt,
            q.metcov00,
            q.metcov01,
            q.metcov10,
            q.metcov11,
            q.mt_1,
            q.mt_2,
            q.mt_3,
            q.genbosonmass,
            q.gen_match_1,
            q.gen_match_2,
            q.gen_match_3,
        ],
    )

    # add genWeight for everything but data
    if sample != "data":
        configuration.add_outputs(
            scopes,
            nanoAOD.genWeight,
        )
    if sample == "dyjets":
        configuration.add_outputs(
            scopes,
            q.ZPtMassReweightWeight,
        )
    if sample in ["rem_ttbar", "ttbar"]:
        configuration.add_outputs(
            scopes,
            q.topPtReweightWeight,
        )
    configuration.add_outputs(
        "emt",
        [
            q.muon_is_mediumid_2,
            q.electron_is_nonisowp90_1,
            q.nelectrons,
            q.nmuons,
            q.ntaus,
            scalefactors.Tau_3_VsJetTauID_lt_SF.output_group,
            scalefactors.Tau_3_VsEleTauID_SF.output_group,
            scalefactors.Tau_3_VsMuTauID_SF.output_group,
            triplequantities.VsJetTauIDFlag_3.output_group,
            triplequantities.VsEleTauIDFlag_3.output_group,
            triplequantities.VsMuTauIDFlag_3.output_group,
            q.taujet_pt_3,
            # q.gen_taujet_pt_2,
            q.decaymode_3,
            q.tau_gen_match_3,
            q.muon_veto_flag,
            q.electron_veto_flag,
            q.id_wgt_ele_wp90nonIso_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_2,
            triggers.EMTGenerateSingleMuonTriggerFlags.output_group,
            triggers.EMTGenerateSingleElectronTriggerFlags.output_group,
            scalefactors.EMTGenerateSingleElectronTriggerSF_MC.output_group,
            scalefactors.EMTGenerateSingleMuonTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
        ],
    )
    configuration.add_outputs(
        "met",
        [
            q.muon_is_mediumid_1,
            q.electron_is_nonisowp90_2,
            q.nelectrons,
            q.nmuons,
            q.ntaus,
            scalefactors.Tau_3_VsJetTauID_lt_SF.output_group,
            scalefactors.Tau_3_VsEleTauID_SF.output_group,
            scalefactors.Tau_3_VsMuTauID_SF.output_group,
            triplequantities.VsJetTauIDFlag_3.output_group,
            triplequantities.VsEleTauIDFlag_3.output_group,
            triplequantities.VsMuTauIDFlag_3.output_group,
            q.taujet_pt_3,
            # q.gen_taujet_pt_2,
            q.decaymode_3,
            q.tau_gen_match_3,
            q.muon_veto_flag,
            q.electron_veto_flag,
            q.id_wgt_ele_wp90nonIso_2,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            triggers.METGenerateSingleMuonTriggerFlags.output_group,
            triggers.METGenerateSingleElectronTriggerFlags.output_group,
            scalefactors.METGenerateSingleElectronTriggerSF_MC.output_group,
            scalefactors.METGenerateSingleMuonTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
        ],
    )
    configuration.add_outputs(
        "mmt",
        [
            q.muon_is_mediumid_1,
            q.muon_is_mediumid_2,
            q.nmuons,
            q.ntaus,
            scalefactors.Tau_3_VsJetTauID_lt_SF.output_group,
            scalefactors.Tau_3_VsEleTauID_SF.output_group,
            scalefactors.Tau_3_VsMuTauID_SF.output_group,
            triplequantities.VsJetTauIDFlag_3.output_group,
            triplequantities.VsEleTauIDFlag_3.output_group,
            triplequantities.VsMuTauIDFlag_3.output_group,
            q.taujet_pt_3,
            q.decaymode_3,
            q.tau_gen_match_3,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_2,
            triggers.MMTGenerateSingleMuonTriggerFlags.output_group,
            scalefactors.MMTGenerateSingleMuonTriggerSF_MC.output_group,
            q.muon_veto_flag,
            q.electron_veto_flag,
            q.m_tt,
            q.pt_W,
        ],
    )
    configuration.add_outputs(
        "ett",
        [
            q.electron_is_nonisowp90_1,
            q.nelectrons,
            q.ntaus,
            scalefactors.Tau_2_VsJetTauID_tt_SF.output_group,
            scalefactors.Tau_2_VsEleTauID_SF.output_group,
            scalefactors.Tau_2_VsMuTauID_SF.output_group,
            scalefactors.Tau_3_VsJetTauID_tt_SF.output_group,
            scalefactors.Tau_3_VsEleTauID_SF.output_group,
            scalefactors.Tau_3_VsMuTauID_SF.output_group,
            triplequantities.VsJetTauIDFlag_2.output_group,
            triplequantities.VsEleTauIDFlag_2.output_group,
            triplequantities.VsMuTauIDFlag_2.output_group,
            triplequantities.VsJetTauIDFlag_3.output_group,
            triplequantities.VsEleTauIDFlag_3.output_group,
            triplequantities.VsMuTauIDFlag_3.output_group,
            q.taujet_pt_2,
            q.taujet_pt_3,
            q.decaymode_2,
            q.decaymode_3,
            q.tau_gen_match_2,
            q.tau_gen_match_3,
            q.muon_veto_flag,
            q.electron_veto_flag,
            q.id_wgt_ele_wp90nonIso_1,
            triggers.ETTGenerateSingleElectronTriggerFlags.output_group,
            scalefactors.ETTGenerateSingleElectronTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
            q.pt_123,
        ],
    )
    configuration.add_outputs(
        "mtt",
        [
            q.nmuons,
            q.ntaus,
            q.muon_is_mediumid_1,
            scalefactors.Tau_2_VsJetTauID_tt_SF.output_group,
            scalefactors.Tau_2_VsEleTauID_SF.output_group,
            scalefactors.Tau_2_VsMuTauID_SF.output_group,
            scalefactors.Tau_3_VsJetTauID_tt_SF.output_group,
            scalefactors.Tau_3_VsEleTauID_SF.output_group,
            scalefactors.Tau_3_VsMuTauID_SF.output_group,
            triplequantities.VsJetTauIDFlag_2.output_group,
            triplequantities.VsEleTauIDFlag_2.output_group,
            triplequantities.VsMuTauIDFlag_2.output_group,
            triplequantities.VsJetTauIDFlag_3.output_group,
            triplequantities.VsEleTauIDFlag_3.output_group,
            triplequantities.VsMuTauIDFlag_3.output_group,
            q.taujet_pt_2,
            q.taujet_pt_3,
            q.decaymode_2,
            q.decaymode_3,
            q.tau_gen_match_2,
            q.tau_gen_match_3,
            q.muon_veto_flag,
            q.electron_veto_flag,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            triggers.MTTGenerateSingleMuonTriggerFlags.output_group,
            scalefactors.MTTGenerateSingleMuonTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
            q.pt_123,
        ],
    )
    configuration.add_outputs(
        "eem",
        [
            q.id_wgt_ele_wp90nonIso_1,
            q.id_wgt_ele_wp90nonIso_2,
            q.electron_is_nonisowp90_1,
            q.electron_is_nonisowp90_2,
            q.muon_is_mediumid_3,
            q.muon_is_tracker_3,
            q.id_wgt_mu_3,
            q.iso_wgt_mu_3,
            q.is_global_3,
            triggers.EEMGenerateSingleElectronTriggerFlags.output_group,
            scalefactors.EEMGenerateSingleElectronTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
            q.muon_veto_flag,
            q.electron_veto_flag,
        ],
    )
    configuration.add_outputs(
        "mme",
        [
            q.id_wgt_ele_wp90nonIso_3,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_2,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            q.electron_is_nonisowp90_3,
            q.muon_is_mediumid_1,
            q.muon_is_mediumid_2,
            triggers.MMEGenerateSingleMuonTriggerFlags.output_group,
            scalefactors.MMEGenerateSingleMuonTriggerSF_MC.output_group,
            q.m_tt,
            q.pt_W,
            q.muon_veto_flag,
            q.electron_veto_flag,
        ],
    )
    if "data" not in sample and "embedding" not in sample:
        configuration.add_outputs(
            scopes,
            [
                nanoAOD.HTXS_Higgs_pt,
                nanoAOD.HTXS_Higgs_y,
                nanoAOD.HTXS_njets30,
                nanoAOD.HTXS_stage_0,
                nanoAOD.HTXS_stage1_2_cat_pTjet30GeV,
                nanoAOD.HTXS_stage1_2_fine_cat_pTjet30GeV,
            ],
        )

    #########################
    # Lepton to tau fakes energy scalefactor shifts  #
    #########################
    if "dyjets" in sample:
        configuration.add_shift(
            SystematicShift(
                name="tauMuFakeEsDown",
                shift_config={
                    "mt": {
                        "tau_mufake_es": "down",
                    }
                },
                producers={"mt": [taus.TauPtCorrection_muFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauMuFakeEsUp",
                shift_config={
                    "mt": {
                        "tau_mufake_es": "up",
                    }
                },
                producers={"mt": [taus.TauPtCorrection_muFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongBarrelDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_barrel": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongBarrelUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_barrel": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongEndcapDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_endcap": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongEndcapUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_endcap": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroBarrelDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_barrel": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroBarrelUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_barrel": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroEndcapDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_endcap": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroEndcapUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_endcap": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            ),
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data", "embedding", "embedding_mc"]
            ],
        )

    #########################
    # MET Shifts
    #########################
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnUp",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredUp",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredUp",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnDown",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredDown",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredDown",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    #########################
    # Prefiring Shifts
    #########################
    if era != "2018":
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringDown",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Dn",
                },
                scopes=["global"],
            )
        )
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringUp",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Up",
                },
                scopes=["global"],
            )
        )
    #########################
    # MET Recoil Shifts
    #########################
    # configuration.add_shift(
    #     SystematicShift(
    #         name="metRecoilResponseUp",
    #         shift_config={
    #             ("et", "mt", "tt", "em", "ee", "mm"): {
    #                 "apply_recoil_resolution_systematic": False,
    #                 "apply_recoil_response_systematic": True,
    #                 "recoil_systematic_shift_up": True,
    #                 "recoil_systematic_shift_down": False,
    #             },
    #         },
    #         producers={
    #             ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
    #         },
    #     ),
    #     samples=[
    #         sample
    #         for sample in available_sample_types
    #         if sample not in ["data", "embedding", "embedding_mc"]
    #     ],
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="metRecoilResponseDown",
    #         shift_config={
    #             ("et", "mt", "tt", "em", "ee", "mm"): {
    #                 "apply_recoil_resolution_systematic": False,
    #                 "apply_recoil_response_systematic": True,
    #                 "recoil_systematic_shift_up": False,
    #                 "recoil_systematic_shift_down": True,
    #             },
    #         },
    #         producers={
    #             ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
    #         },
    #     ),
    #     samples=[
    #         sample
    #         for sample in available_sample_types
    #         if sample not in ["data", "embedding", "embedding_mc"]
    #     ],
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="metRecoilResolutionUp",
    #         shift_config={
    #             ("et", "mt", "tt", "em", "ee", "mm"): {
    #                 "apply_recoil_resolution_systematic": True,
    #                 "apply_recoil_response_systematic": False,
    #                 "recoil_systematic_shift_up": True,
    #                 "recoil_systematic_shift_down": False,
    #             },
    #         },
    #         producers={
    #             ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
    #         },
    #     ),
    #     samples=[
    #         sample
    #         for sample in available_sample_types
    #         if sample not in ["data", "embedding", "embedding_mc"]
    #     ],
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="metRecoilResolutionDown",
    #         shift_config={
    #             ("et", "mt", "tt", "em", "ee", "mm"): {
    #                 "apply_recoil_resolution_systematic": True,
    #                 "apply_recoil_response_systematic": False,
    #                 "recoil_systematic_shift_up": False,
    #                 "recoil_systematic_shift_down": True,
    #             },
    #         },
    #         producers={
    #             ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
    #         },
    #     ),
    #     samples=[
    #         sample
    #         for sample in available_sample_types
    #         if sample not in ["data", "embedding", "embedding_mc"]
    #     ],
    # )
    #########################
    # Pileup Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="PileUpUp",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "up"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="PileUpDown",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "down"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    #########################
    # TauID scale factor shifts, channel dependent # Tau energy scale shifts, dm dependent
    #########################
    add_tauVariations(configuration, sample)
    #########################
    # Import triggersetup   #
    #########################
    add_diTauTriggerSetup(configuration)
    #########################
    # Add additional producers and SFs related to embedded samples
    #########################
    # setup_embedding(configuration, scopes)

    #########################
    # Jet energy resolution and jet energy scale
    #########################
    add_jetVariations(configuration, available_sample_types, era)

    #########################
    # btagging scale factor shape variation
    #########################
    add_btagVariations(configuration, available_sample_types)

    #########################
    # Jet energy correction for data
    #########################
    add_jetCorrectionData(configuration, era)

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
