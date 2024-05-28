from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, ExtendedVectorProducer

# resolved tautau analysis
eras = Producer(
    name="eras",
    call='quantities::eras({df}, {output}, "{era_2016preVFP}","{era_2016postVFP}", "{era_2017}", "{era_2018}")',
    input=[],
    output=[q.era_2016preVFP, q.era_2016postVFP, q.era_2017, q.era_2018],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_1 = Producer(
    name="Transform_pt_1",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_1,
    ],
    output=[q.transformed_pt_1],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_2 = Producer(
    name="Transform_pt_2",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_2,
    ],
    output=[q.transformed_pt_2],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_3 = Producer(
    name="Transform_pt_3",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_3,
    ],
    output=[q.transformed_pt_3],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_eta_1 = Producer(
    name="Transform_eta_1",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.eta_1,
    ],
    output=[q.transformed_eta_1],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_eta_2 = Producer(
    name="Transform_eta_2",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.eta_2,
    ],
    output=[q.transformed_eta_2],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_eta_3 = Producer(
    name="Transform_eta_3",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.eta_3,
    ],
    output=[q.transformed_eta_3],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_deltaR_12 = Producer(
    name="Transform_deltaR_12",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.deltaR_12,
    ],
    output=[q.transformed_deltaR_12],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_deltaR_13 = Producer(
    name="Transform_deltaR_13",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.deltaR_13,
    ],
    output=[q.transformed_deltaR_13],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_deltaR_23 = Producer(
    name="Transform_deltaR_23",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.deltaR_23,
    ],
    output=[q.transformed_deltaR_23],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_m_vis = Producer(
    name="Transform_m_vis",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.m_vis,
    ],
    output=[q.transformed_m_vis],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_phi_1 = Producer(
    name="Transform_phi_1",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.phi_1,
    ],
    output=[q.transformed_phi_1],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_decaymode_3 = Producer(
    name="Transform_decaymode_3",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "i")',
    input=[
        q.decaymode_3,
    ],
    output=[q.transformed_decaymode_3],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_phi_3 = Producer(
    name="Transform_phi_3",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.phi_3,
    ],
    output=[q.transformed_phi_3],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_phi_2 = Producer(
    name="Transform_phi_2",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.phi_2,
    ],
    output=[q.transformed_phi_2],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_phi_1 = Producer(
    name="Transform_phi_1",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.phi_1,
    ],
    output=[q.transformed_phi_1],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_Lt = Producer(
    name="Transform_Lt",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.Lt,
    ],
    output=[q.transformed_Lt],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_era_2016preVFP = Producer(
    name="Transform_era_2016preVFP",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "i")',
    input=[
        q.era_2016preVFP,
    ],
    output=[q.transformed_era_2016preVFP],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_era_2016postVFP = Producer(
    name="Transform_era_2016postVFP",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "i")',
    input=[
        q.era_2016postVFP,
    ],
    output=[q.transformed_era_2016postVFP],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_era_2017 = Producer(
    name="Transform_era_2017",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "i")',
    input=[
        q.era_2017,
    ],
    output=[q.transformed_era_2017],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_era_2018 = Producer(
    name="Transform_era_2018",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "i")',
    input=[
        q.era_2018,
    ],
    output=[q.transformed_era_2018],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_met = Producer(
    name="Transform_met",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.met,
    ],
    output=[q.transformed_met],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_m_tt = Producer(
    name="Transform_m_tt",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.m_tt,
    ],
    output=[q.transformed_m_tt],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_mjj = Producer(
    name="Transform_mjj",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.mjj,
    ],
    output=[q.transformed_mjj],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_mt_1 = Producer(
    name="Transform_mt_1",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.mt_1,
    ],
    output=[q.transformed_mt_1],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_mt_2 = Producer(
    name="Transform_mt_2",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.mt_2,
    ],
    output=[q.transformed_mt_2],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_mt_3 = Producer(
    name="Transform_mt_3",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.mt_3,
    ],
    output=[q.transformed_mt_3],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_vis = Producer(
    name="Transform_pt_vis",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_vis,
    ],
    output=[q.transformed_pt_vis],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_W = Producer(
    name="Transform_pt_W",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_W,
    ],
    output=[q.transformed_pt_W],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_metphi = Producer(
    name="Transform_metphi",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.metphi,
    ],
    output=[q.transformed_metphi],
    scopes=["mmt", "emt", "met", "ett", "mtt"],
)
Transform_pt_123met = Producer(
    name="Transform_pt_123met",
    call='ml::StandardTransformer({df}, {input}, {output}, "{feature_transformation_file}", "f")',
    input=[
        q.pt_123met,
    ],
    output=[q.transformed_pt_123met],
    scopes=["ett", "mtt"],
)
LLTTransformVars = ProducerGroup(
    name="LLTTransformVars",
    call=None,
    input=None,
    output=None,
    scopes=["mmt", "emt", "met"],
    subproducers=[
        Transform_pt_1,
        Transform_pt_2,
        Transform_pt_3,
        Transform_eta_1,
        Transform_eta_2,
        Transform_eta_3,
        Transform_m_vis,
        Transform_decaymode_3,
        Transform_phi_1,
        Transform_phi_2,
        Transform_phi_3,
        Transform_Lt,
        Transform_deltaR_13,
        Transform_deltaR_23,
        Transform_deltaR_12,
        Transform_era_2016preVFP,
        Transform_era_2016postVFP,
        Transform_era_2017,
        Transform_era_2018,
        Transform_met,
        Transform_m_tt,
        Transform_mjj,
        Transform_mt_1,
        Transform_mt_2,
        Transform_mt_3,
        Transform_pt_vis,
        Transform_pt_W,
        Transform_metphi,
    ],
)
LTTTransformVars = ProducerGroup(
    name="LTTTransformVars",
    call=None,
    input=None,
    output=None,
    scopes=["mtt", "ett"],
    subproducers=[
        Transform_pt_1,
        Transform_pt_2,
        Transform_pt_3,
        Transform_eta_1,
        Transform_eta_2,
        Transform_eta_3,
        Transform_m_vis,
        Transform_decaymode_3,
        Transform_phi_1,
        Transform_phi_2,
        Transform_phi_3,
        Transform_Lt,
        Transform_deltaR_13,
        Transform_deltaR_23,
        Transform_deltaR_12,
        Transform_era_2016preVFP,
        Transform_era_2016postVFP,
        Transform_era_2017,
        Transform_era_2018,
        Transform_met,
        Transform_m_tt,
        Transform_mjj,
        Transform_mt_1,
        Transform_mt_2,
        Transform_mt_3,
        Transform_pt_vis,
        Transform_pt_W,
        Transform_metphi,
        Transform_pt_123met,
    ],
)
Evaluate_ORT_LLT = Producer(
    name="Evaluate_ORT_LLT",
    call='ml::GenericOnnxEvaluator<27>({df}, onnxSessionManager, {output}, "{model_file}", {input_vec})',
    input=[
        q.transformed_era_2016preVFP,
        q.transformed_era_2016postVFP,
        q.transformed_era_2017,
        q.transformed_era_2018,
        q.transformed_pt_3,
        q.transformed_decaymode_3,
        q.transformed_eta_3,
        q.transformed_phi_3,
        q.transformed_deltaR_13,
        q.transformed_deltaR_23,
        q.transformed_pt_1,
        q.transformed_eta_1,
        q.transformed_phi_1,
        q.transformed_pt_2,
        q.transformed_eta_2,
        q.transformed_phi_2,
        q.transformed_m_vis,
        q.transformed_Lt,
        q.transformed_met,
        q.transformed_m_tt,
        q.transformed_mjj,
        q.transformed_mt_1,
        q.transformed_mt_2,
        q.transformed_mt_3,
        q.transformed_pt_vis,
        q.transformed_pt_W,
        q.transformed_metphi,
    ],
    output=[q.output_vector, q.predicted_class, q.predicted_max_value],
    scopes=["mmt", "emt", "met"],
)
Evaluate_ORT_LTT = Producer(
    name="Evaluate_ORT_LTT",
    call='ml::GenericOnnxEvaluator<28>({df}, onnxSessionManager, {output}, "{model_file}", {input_vec})',
    input=[
        q.transformed_era_2016preVFP,
        q.transformed_era_2016postVFP,
        q.transformed_era_2017,
        q.transformed_era_2018,
        q.transformed_pt_3,
        q.transformed_decaymode_3,
        q.transformed_eta_3,
        q.transformed_phi_3,
        q.transformed_deltaR_13,
        q.transformed_deltaR_23,
        q.transformed_pt_1,
        q.transformed_eta_1,
        q.transformed_phi_1,
        q.transformed_pt_2,
        q.transformed_eta_2,
        q.transformed_phi_2,
        q.transformed_m_vis,
        q.transformed_Lt,
        q.transformed_met,
        q.transformed_m_tt,
        q.transformed_mjj,
        q.transformed_mt_1,
        q.transformed_mt_2,
        q.transformed_mt_3,
        q.transformed_pt_vis,
        q.transformed_pt_W,
        q.transformed_metphi,
        q.transformed_pt_123met,
    ],
    output=[q.output_vector, q.predicted_class, q.predicted_max_value],
    scopes=["ett", "mtt"],
)
