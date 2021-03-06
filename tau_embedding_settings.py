from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List
from code_generation.rules import AppendProducer
from .producers import embedding as embedding
from .producers import scalefactors as scalefactors
from code_generation.configuration import Configuration


def setup_embedding(configuration: Configuration, scopes: List[str]):

    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=embedding.EmbeddingQuantities,
            samples=["embedding", "embedding_mc"],
        ),
    )

    # add embedding selection scalefactors
    configuration.add_config_parameters(
        scopes,
        {
            "embedding_selection_sf_file": "data/embedding/muon_2018UL.json.gz",
            "embedding_selection_trigger_sf": "m_sel_trg_kit_ratio",
            "embedding_selection_id_sf": "EmbID_pt_eta_bins",
        },
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=embedding.TauEmbeddingSelectionSF, samples=["embedding"]
        ),
    )
    # add muon scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "embedding_muon_sf_file": "data/embedding/muon_2018UL.json.gz",
            "embedding_muon_id_sf": "ID_pt_eta_bins",
            "embedding_muon_iso_sf": "Iso_pt_eta_bins",
        },
    )
    # add electron scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {
            "embedding_electron_sf_file": "data/embedding/electron_2018UL.json.gz",
            "embedding_electron_id_sf": "ID90_pt_eta_bins",
            "embedding_electron_iso_sf": "Iso_pt_eta_bins",
        },
    )
    # muon trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["mt"],
        {
            "singlemoun_trigger_sf": [
                {
                    "flagname": "trg_wgt_IsoMu24",
                    "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                },
                {
                    "flagname": "trg_wgt_IsoMu27",
                    "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                },
                {
                    "flagname": "trg_wgt_IsoMu24OrIsoMu27",
                    "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                },
            ]
        },
    )
    # electron trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["et"],
        {
            "singlelectron_trigger_sf": [
                {
                    "flagname": "trg_wgt_Ele27",
                    "embedding_trigger_sf": "Trg27_Iso_pt_eta_bins",
                },
                {
                    "flagname": "trg_wgt_Ele32",
                    "embedding_trigger_sf": "Trg32_Iso_pt_eta_bins",
                },
                {
                    "flagname": "trg_wgt_Ele35",
                    "embedding_trigger_sf": "Trg35_Iso_pt_eta_bins",
                },
                {
                    "flagname": "trg_wgt_Ele27OrEle32OrEle35",
                    "embedding_trigger_sf": "Trg_Iso_pt_eta_bins",
                },
            ]
        },
    )
    configuration.add_modification_rule(
        ["mt"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_1,
                embedding.TauEmbeddingMuonIsoSF_1,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["et"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingElectronIDSF_1,
                embedding.TauEmbeddingElectronIsoSF_1,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["em"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingElectronIDSF_1,
                embedding.TauEmbeddingElectronIsoSF_1,
                embedding.TauEmbeddingMuonIDSF_2,
                embedding.TauEmbeddingMuonIsoSF_2,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["mm"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_1,
                embedding.TauEmbeddingMuonIsoSF_1,
                embedding.TauEmbeddingMuonIDSF_2,
                embedding.TauEmbeddingMuonIsoSF_2,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["mt"],
        AppendProducer(
            producers=[
                embedding.MTGenerateSingleMuonTriggerSF,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["et"],
        AppendProducer(
            producers=[
                embedding.ETGenerateSingleElectronTriggerSF,
            ],
            samples=["embedding"],
        ),
    )

    return configuration
