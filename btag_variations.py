from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors


def add_btagVariations(configuration, available_sample_types):
    #########################
    # btagging shape uncertainties
    #########################
    configuration.add_shift(
        SystematicShift(
            name="btagJesUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "up_jes"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagJesDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "down_jes"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "up_hf"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "down_hf"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats1Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "up_hfstats1"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats1Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_hfstats1"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats2Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "up_hfstats2"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats2Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_hfstats2"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "up_lf"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "down_lf"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats1Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "up_lfstats1"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats1Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_lfstats1"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats2Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "up_lfstats2"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats2Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_lfstats2"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr1Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "up_cferr1"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr1Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_cferr1"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr2Up",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"btag_sf_variation": "up_cferr2"},
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr2Down",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {
                    "btag_sf_variation": "down_cferr2"
                },
            },
            producers={("emt", "met", "mmt", "mtt", "ett"): scalefactors.btagging_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
