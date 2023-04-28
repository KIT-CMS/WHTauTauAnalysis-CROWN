from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for loosest selection of muons
####################

MuonPtCut = Producer(
    name="MuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["global"],
)
MuonEtaCut = Producer(
    name="MuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["global"],
)
MuonDxyCut = Producer(
    name="MuonDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_muon_dxy})",
    input=[nanoAOD.Muon_dxy],
    output=[],
    scopes=["global"],
)
MuonDzCut = Producer(
    name="MuonDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_muon_dz})",
    input=[nanoAOD.Muon_dz],
    output=[],
    scopes=["global"],
)
MuonIsTrackerOrIsGlobalCut = Producer(
    name="MuonIsTrackerOrIsGlobalCut",
    call="physicsobject::muon::CutIsTrackerOrIsGlobal({df}, {input}, {output})",
    input=[nanoAOD.Muon_isTracker, nanoAOD.Muon_isGlobal],
    output=[],
    scopes=["global"],
)
MuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{muon_id}")',
    input=[],
    output=[],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
BaseMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["global"],
    subproducers=[
        MuonPtCut,
        MuonEtaCut,
        MuonDxyCut,
        MuonDzCut,
        MuonIsTrackerOrIsGlobalCut,
        # MuonIDCut
    ],
)
# MuonPtCut_fake = Producer(
#     name="MuonPtCut_fake",
#     call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
#     input=[nanoAOD.Muon_pt],
#     output=[],
#     scopes=["eem"],
# )
# MuonEtaCut_fake = Producer(
#     name="MuonEtaCut_fake",
#     call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
#     input=[nanoAOD.Muon_eta],
#     output=[],
#     scopes=["eem"],
# )
# BaseMuons_fake = ProducerGroup(
#     name="BaseMuons_fake",
#     call="physicsobject::CombineMasks({df}, {output}, {input})",
#     input=[],
#     output=[q.base_muons_mask_fake],
#     scopes=["eem"],
#     subproducers=[
#         MuonPtCut_fake,
#         MuonEtaCut_fake,
#     ],
# )
####################
# Set of producers used for more specific selection of muons in channels
####################
MuonIsoCut = Producer(
    name="MuonIsoCut",
    call="physicsobject::muon::CutIsolation({df}, {output}, {input}, {muon_iso_cut})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=["emt", "met", "mmt", "mme", "mtt"],
)
GoodMuonPtCut = Producer(
    name="GoodMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
GoodMuonEtaCut = Producer(
    name="GoodMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
GoodMuonIsoCut = Producer(
    name="GoodMuonIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {muon_iso_cut})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
GoodMuons = ProducerGroup(
    name="GoodMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
    subproducers=[
        GoodMuonPtCut,
        GoodMuonEtaCut,
        GoodMuonIsoCut,
        MuonIDCut,
    ],
)
NumberOfGoodMuons = Producer(
    name="NumberOfGoodMuons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.good_muons_mask],
    output=[q.nmuons],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
VetoMuons = Producer(
    name="VetoMuons",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {muon_index_in_triple})",
    input=[q.good_muons_mask, q.leptontriple],
    output=[q.veto_muons_mask],
    scopes=["emt", "met", "mmt", "mtt", "mme", "eem", "ett"],
)
VetoSecondMuon = Producer(
    name="VetoSecondMuon",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {second_muon_index_in_triple})",
    input=[q.veto_muons_mask, q.leptontriple],
    output=[q.veto_muons_mask_2],
    scopes=["mmt", "mme"],
)

ExtraMuonsVeto = Producer(
    name="ExtraMuonsVeto",
    call="physicsobject::LeptonVetoFlag({df}, {output}, {input})",
    input={
        "mme": [q.veto_muons_mask_2],
        "eem": [q.veto_muons_mask],
        "emt": [q.veto_muons_mask],
        "met": [q.veto_muons_mask],
        "mtt": [q.veto_muons_mask],
        "ett": [q.good_muons_mask],
        "mmt": [q.veto_muons_mask_2],
    },
    output=[q.muon_veto_flag],
    scopes=[
        "emt",
        "met",
        "mmt",
        "mtt",
        "ett",
        "mme",
        "eem",
    ],
)

####################
# Set of producers used for di-muon veto
####################

DiMuonVetoPtCut = Producer(
    name="DiMuonVetoPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_dimuonveto_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["global"],
)
DiMuonVetoIDCut = Producer(
    name="DiMuonVetoIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{dimuonveto_id}")',
    input=[],
    output=[],
    scopes=["global"],
)
DiMuonVetoMuons = ProducerGroup(
    name="DiMuonVetoMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=MuonEtaCut.output + MuonDxyCut.output + MuonDzCut.output + MuonIsoCut.output,
    output=[],
    scopes=["global"],
    subproducers=[
        DiMuonVetoPtCut,
        DiMuonVetoIDCut,
    ],
)
DiMuonVeto = ProducerGroup(
    name="DiMuonVeto",
    call="physicsobject::CheckForDiLeptonPairs({df}, {output}, {input}, {dileptonveto_dR})",
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_charge,
    ],
    output=[q.dimuon_veto],
    scopes=["global"],
    subproducers=[DiMuonVetoMuons],
)
